import os 
from dotenv import load_dotenv

load_dotenv()

cMN = os.getenv("CLAUDE_MODEL_NAME")
cAK = os.getenv("CLAUDE_API_KEY")

import anthropic 

client = anthropic.Anthropic(api_key=cAK)

# from anthropic.lib import files_from_dir
# skill = client.beta.skills.create(
#     files=files_from_dir("./Managed-Agents/skills/indic-data-auditor")
# )
# print("Skill ID:", skill.id)
# print("Latest Version:", skill.latest_version_id)

# skills = client.beta.skills.list(
#     betas=["skills-2025-10-02"]
# )
skills =client.beta.skills.list()
skill = next(
    (
        skill
        for skill in skills.data
        if skill.display_name == "indic-data-auditor"
    ),
    None
)

#CREATE MEMORY STORE
store = client.beta.memory_stores.create(
    name="Bhashini-Vendor-Audit-Store",
    description="Persistent audit logs, vendor history, and approved Bhashini/ULCA dataset exceptions.",
)
print(f"Memory Store ID: {store.id}")


#ENVIRONMENT
environment = client.beta.environments.create(
    name="ai4b-audit-env",
    config={
        "type": "cloud",
        "networking": {"type": "unrestricted"},
    },
)
print(f"Environment ID: {environment.id}")


#AGENT 1
agent_one = client.beta.agents.create(
    name="Indic-Auditor-Agent-1",
    model=cMN,
    system="""
    You are an AI4Bharat Data Governance Specialist.
    Your job is to manage vendor compliance profiles and record policy exceptions
    into persistent memory (/mnt/memory/) for use across the Bhashini mission.
    """,
    tools=[
        {"type": "agent_toolset_20260401"},
    ],
)
print(f"Agent #1 ID: {agent_one.id}")


#SESSION 1
session_one = client.beta.sessions.create(
    agent=agent_one.id,
    environment_id=environment.id,
    resources=[
        {
            "type": "memory_store",
            "memory_store_id": store.id,
            "access": "read_write",
            "instructions": "Persistent vendor compliance records and approved data collection waivers. Always check and update before concluding.",
        }
    ],
    title="Session 1 - Record Vendor Policies",
)
print(f"Session #1 ID: {session_one.id}")


#EXECUTE AGENT 1
with client.beta.sessions.events.stream(session_one.id) as stream:
    client.beta.sessions.events.send(
        session_one.id,
        events=[
            {
                "type": "user.message",
                "content": [
                    {
                        "type": "text",
                        "text": """Please create a compliance profile in persistent memory for data collection vendor 'VaniCorp':
                            1. Vendor Name: VaniCorp
                            2. Project: Konkani-Marathi Border Dialect Speech Dataset
                            3. Approved Special Waivers (Signed by MeitY DMU):
                            - Sampling rate of 24kHz is APPROVED (standard is 16kHz minimum).
                            - Speaker balance of 45% Female / 55% Male is ACCEPTABLE for this remote border region.
                            4. Strictly Enforced Rules (No Waivers):
                            - Must use standard native Devanagari script (NO Latin/English transliteration allowed).
                            - All spoken numbers MUST be fully written out in native script (digits like '100' are strictly rejected).
                            - Transcriptions must be 100% verbatim.
                            Save these vendor notes into persistent memory so our review agents can reference them in future sessions.""",
                    },
                ],
            },
        ],
    )

    for event in stream:
        match event.type:
            case "agent.message":
                for block in event.content:
                    print(block.text, end="")
            case "agent.tool_use":
                print(f"\n[Using tool: {event.name}]")
            case "session.status_idle":
                print("\n\nSession #1 Finished: Vendor memory saved.")
                break


#AGENT 2
agent_two = client.beta.agents.create(
    name="Indic-Auditor-Agent-2",
    model=cMN,
    system="""
    You are a strict AI4Bharat Data Auditor.
    Your sole job is to enforce ULCA quality standards for Indian language datasets (MT, ASR, TTS, OCR).
    Check persistent memory for any vendor-specific profiles or approved waivers.
    Reject non-compliant submissions and format your output strictly using the provided audit report template.
    """,
    skills=[
        {"type": "anthropic", "skill_id": "docx"},
        {"type": "anthropic", "skill_id": "pdf"},
        {
            "type": "custom",
            "skill_id": skill.id,
            "version": skill.latest_version_id,
        },
    ],
    tools=[
        {"type": "agent_toolset_20260401"},
    ],
)


#SESSION 2
session_two = client.beta.sessions.create(
    agent=agent_two.id,
    environment_id=environment.id,
    resources=[
        {
            "type": "memory_store",
            "memory_store_id": store.id,
            "access": "read_write",
            "instructions": "Vendor compliance records and historical waivers. Always check memory before running the audit checklist.",
        }
    ],
    title="Session 2 - Audit VaniCorp Batch",
)
print(f"Session #2 ID: {session_two.id}")

with client.beta.sessions.events.stream(session_two.id) as stream:
    client.beta.sessions.events.send(
        session_two.id,
        betas=["skills-2025-10-02"],
        events=[
            {
                "type": "user.message",
                "content": [
                    {
                        "type": "text",
                        "text": """We just received a new speech dataset submission from vendor 'VaniCorp' for the Konkani-Marathi border dialect:
                            Submission Details:
                            - Audio Format: 24kHz Uncompressed WAV, clean acoustic setup.
                            - Demographics: 45% Female, 55% Male speakers.
                            - Transcription Style: Verbatim, but all spoken numbers are written as numerical digits (e.g. '500' instead of 'पाचशे').
                            - Script: Latin/English transliteration was used for unfamiliar dialect words.

                            Please:
                            1. Check your persistent memory for VaniCorp's profile and approved waivers.
                            2. Cross-reference this submission against the Bhashini ULCA data quality checklist and standards in your skills.
                            3. Identify which parts are approved by waiver and which violate mandatory ULCA rules.
                            4. Generate the final audit report as a professionally formatted Microsoft Word (.docx) document and save it as an output file.""",
                    },
                ],
            },
        ],
    )

    for event in stream:
        match event.type:
            case "agent.message":
                for block in event.content:
                    print(block.text, end="")
            case "agent.tool_use":
                print(f"\n[Using tool: {event.name}]")
            case "session.status_idle":
                print("\n\nSession #2 Finished: Audit complete.")
                break


#RETRIEVE AND DOWNLOAD GENERATED WORD (.DOCX) AUDIT REPORT
files = client.beta.files.list(
    scope_id=session_two.id,
    betas=["managed-agents-2026-04-01"],
)

for file in files.data:
    if file.filename.endswith(".docx"):
        print(f"Downloading {file.filename}...")
        metadata = client.beta.files.retrieve_metadata(file.id)
        content = client.beta.files.download(file.id)
        content.write_to_file(metadata.filename)
        print(f"Saved: {metadata.filename}")

print("\nAll done!")