import os 
from dotenv import load_dotenv

load_dotenv()

cMN = os.getenv("CLAUDE_MODEL_NAME")
cAK = os.getenv("CLAUDE_API_KEY")

import anthropic    

client = anthropic.Anthropic(api_key=cAK)


#UPLOAD MARKETING SKILL
from anthropic.lib import files_from_dir

skill = client.beta.skills.create(
    files=files_from_dir("./Managed-Agents/skills/indic-data-auditor")
)

print("Skill ID:", skill.id)
print("Latest Version:", skill.latest_version_id) #skill.latest_version)

#CREATE AGENT
agent = client.beta.agents.create(
    name="Indic-Data-Auditor-Agent",
    model=cMN,
    system="""
                You are a strict AI4Bharat Data Auditor. 
                Your sole job is to enforce ULCA quality standards for Indian language datasets (MT, ASR, TTS, OCR). 
                You must reject non-compliant data and output your feedback strictly using the provided audit report template.
                """,
    skills = [
        {
            "type": "anthropic",
            "skill_id": "docx" 
        },
        {
                    "type": "anthropic",
                    "skill_id": "pdf" 
        },
        {
            "type": "custom",
            "skill_id": skill.id,
            "version": skill.latest_version_id  #skill.latest_version
        }
    ],
    tools=[
        {"type": "agent_toolset_20260401"},
    ],
)

print(f"Agent ID: {agent.id}, version: {agent.version}")


#ENVIRONMENT
environment = client.beta.environments.create(
    name="ai4b-env",
    config={
        "type": "cloud",
        "networking": {"type": "unrestricted"},
    },
)

print(f"Environment ID: {environment.id}")


#SESSION
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    title="ai4b session",
)

print(f"Session ID: {session.id}")


#EXECUTE AGENT
with client.beta.sessions.events.stream(session.id) as stream:
            # Send the user message after the stream opens
            client.beta.sessions.events.send(
                session.id,
                betas = ["skills-2025-10-02"],
                events=[
                    {
                        "type": "user.message",
                        "content": [
                            {
                                "type": "text",
                                "text": """Please audit the following proposed vendor data collection plan for a new Marathi ASR (Automatic Speech Recognition) dataset:
                                                - Audio Format: 8kHz, MP3 format, recorded in outdoor environments.
                                                - Demographics: 75% Male, 25% Female speakers from a single district.
                                                - Transcription Rule: Verbatim, but all spoken numbers will be typed as digits (e.g., '100' instead of 'शंभर').
                                                - Script: Latin/English transliteration will be used for hard-to-spell words.
                                                Use the Bhashini ULCA data standards, the data quality checklist, and the audit report template provided in your skills to evaluate this submission. 
                                                Identify all critical blockers, explain why it fails the standards, and provide exact remediation steps. Finally, generate the completed audit report as a professionally formatted Microsoft Word (.docx) document and save it as an output file."""
                            },
                        ],
                    },
                ],
            )

            # Process streaming events
            for event in stream:
                match event.type:
                    case "agent.message":
                        for block in event.content:
                            print(block.text, end="")
                    case "agent.tool_use":
                        print(f"\n[Using tool: {event.name}]")
                    case "session.status_idle":
                        print("\n\nAgent finished.")
                        break


files = client.beta.files.list(
    scope_id=session.id,
    betas=["managed-agents-2026-04-01"],
)

for file in files.data:

    if file.filename.endswith(".docx"):

        print(f"Downloading {file.filename}...")

        metadata = client.beta.files.retrieve_metadata(file.id)

        content = client.beta.files.download(file.id)

        content.write_to_file(metadata.filename)

        print("Done!")