import os 
from dotenv import load_dotenv

load_dotenv()

cMN = os.getenv("CLAUDE_MODEL_NAME")
cAK = os.getenv("CLAUDE_API_KEY")

import anthropic    

client = anthropic.Anthropic(api_key=cAK)


#CREATE AGENT
agent = client.beta.agents.create(
    name="MLearnBot-MCP-Agent",
    model=cMN,
    mcp_servers=[
        {
            "type": "url",
            "name": "Microsoft Learn",
            "url": "https://learn.microsoft.com/api/mcp",
        },
    ],
    system="Suggest user only official source url or links, no long responses.",
    tools=[
        {"type": "agent_toolset_20260401"},
        {"type": "mcp_toolset",  "mcp_server_name": "Microsoft Learn", "default_config": {"enabled": True}}
    ],
)

print(f"Agent ID: {agent.id}, version: {agent.version}")


environment = client.beta.environments.create(
    name="quickstart-envv",
    config={
        "type": "cloud",
        "networking": {"type": "unrestricted"},
    },
)
print(f"Environment ID: {environment.id}")

session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    title="Quickstart sessionn",
)

print(f"Session ID: {session.id}")

# #FETCH FROM CLAUDE IF ALREADY CREATED
# agents = client.beta.agents.list()
# agent = next(
#     a for a in agents.data
#     if a.name == "MLearnBot-MCP-Agent"
# )

# environments = client.beta.environments.list()
# environment = next(
#     e for e in environments.data
#     if e.name == "quickstart-env"
# )

# sessions = client.beta.sessions.list()
# session = next(
#     s for s in sessions.data
#     if s.name == "Quickstart session"
# )


#EXECUTE AGENT
with client.beta.sessions.events.stream(session.id) as stream:
            # Send the user message after the stream opens
            client.beta.sessions.events.send(
                session.id,
                events=[
                    {
                        "type": "user.message",
                        "content": [
                            {
                                "type": "text",
                                "text": """Provide Information using the MS Learn MCP Server - What is the Microsoft AI-103 Certification?
                                           Provide appropriate links to MS Learn Webpages wherever possible""",
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