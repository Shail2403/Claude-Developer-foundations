import os 
from dotenv import load_dotenv

load_dotenv()

cMN = os.getenv("CLAUDE_MODEL_NAME")
cAK = os.getenv("CLAUDE_API_KEY")

import anthropic    

client = anthropic.Anthropic(api_key=cAK)

##UPLOAD PDF USING FILES API
#with open("./Managed-Agents/Docs/AI4Bharat_DataReport.pdf", "rb") as f:
#    file_upload = client.beta.files.upload(file=("AI4Bharat_DataReport.pdf", f, "application/pdf"))
#    print(file_upload.id)


files = client.beta.files.list(
    betas=["files-api-2025-04-14"]
)
file_upload = next(
    (
        file
        for file in files.data
        if file.filename == "AI4Bharat_DataReport.pdf"
    ),
    None,
)


#CREATE AGENT
agent = client.beta.agents.create(
    name="PDF-Analysis-Agent",
    model=cMN,
    system="You are a helpful AI Assistant.",
    tools=[
        {"type": "agent_toolset_20260401"},
    ],
)

print(f"Agent ID: {agent.id}, version: {agent.version}")


#ENVIRONMENT
environment = client.beta.environments.create(
    name="pdf-env",
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
    title="pdf session",
)

print(f"Session ID: {session.id}")


#EXECUTE AGENT
with client.beta.sessions.events.stream(session.id) as stream:
            # Send the user message after the stream opens
            client.beta.sessions.events.send(
                session.id,
                betas = ["files-api-2025-04-14"],
                events=[
                    {
                        "type": "user.message",
                        "content": [
                            {
                              "type": "document",
                              "source": {"type": "file", "file_id": file_upload.id}    
                            },
                            {
                                "type": "text",
                                #"text": """I'm reading the sections on OCR and Text-to-Speech data collection. Based on the graphs and visual charts provided in those sections, what are the exact numbers shown for Hindi versus Tamil, and what key trends do these images highlight?""",
                                "text":"""Analyze all images given in pdf and give short summary """
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

