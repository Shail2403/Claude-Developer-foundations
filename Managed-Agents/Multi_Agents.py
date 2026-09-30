import os 
from dotenv import load_dotenv

load_dotenv()

cMN = os.getenv("CLAUDE_MODEL_NAME")
cAK = os.getenv("CLAUDE_API_KEY")

import anthropic 

client = anthropic.Anthropic(api_key=cAK)

#CREATE RESEARCHER AGENT
researcher_agent = client.beta.agents.create(
    name="ResearcherBot-Agent",
    model=cMN,
    system="""You are a knowledgeable researcher. Your task is to gather information and provide insights on a given topic.
              You should use reliable sources and present the information in a clear and concise manner.""",
    tools=[
        {"type": "agent_toolset_20260401"},
    ],
)

print(f"Agent ID: {researcher_agent.id}, version: {researcher_agent.version}")


#CREATE WRITER AGENT
writer_agent = client.beta.agents.create(
    name="WriterBot-Agent",
    model=cMN,
    system="""You are a creative writer. Your task is to write an essay on a given topic.
              You should focus on clarity, coherence, and engaging storytelling""",
)

print(f"Agent ID: {writer_agent.id}, version: {writer_agent.version}")


#CREATE COORDINATOR AGENT
coordinator_agent = client.beta.agents.create(
    name="EditorialBot-Head",
    model=cMN,
    system= """
              You are the Editorial Head Agent which whill coordinate and delegate work to the 
              researcher agent for researching topics and the writer agent for synthesizing the topics researched
              in a refined output which could be an article, essay etc. 
            """,
    tools=[
        {"type": "agent_toolset_20260401"},
    ],
    multiagent={
        "type": "coordinator",
        "agents": [
            {"type": "agent", "id": researcher_agent.id},
            {"type": "agent", "id": writer_agent.id}
        ]
    }
)

print(f"Agent ID: {coordinator_agent.id}, version: {coordinator_agent.version}")


#ENVIRONMENT
environment = client.beta.environments.create(
    name="multiAgentBot-env",
    config={
        "type": "cloud",
        "networking": {"type": "unrestricted"},
    },
)

print(f"Environment ID: {environment.id}")


#SESSION
session = client.beta.sessions.create(
    agent=coordinator_agent.id,
    environment_id=environment.id,
    title="multiAgentBot-session"
)


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
                                "text": """write an essay about the use of AI or AI Agents in large Banking  Projects and security flaws or to keep in head(give as List) especially to Devs.
                                           Don't perform a lot of research, use only one instance of researcher agent
                                           and rather make it quick pls. Keep the essay/article really short under 250 words pls
                                        """,
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