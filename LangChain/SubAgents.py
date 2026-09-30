import os 
from dotenv import load_dotenv

load_dotenv()

cMN = os.getenv("CLAUDE_MODEL_NAME")
cAK = os.getenv("CLAUDE_API_KEY")


#INSTANTIATE THE CHATANTHROPIC CLASS
from langchain_anthropic import ChatAnthropic

model = ChatAnthropic(
    model_name = cMN,
    api_key = cAK
)


#CREATE WEB SEARCH TOOL
from anthropic.types import WebSearchTool20260209Param

# Anthropic Web Search tool
search_tool = WebSearchTool20260209Param(
    name="web_search",
    type="web_search_20260209",
    max_uses=2,
    allowed_callers=["direct"] #added for model automatic calling
)


#CREATE RESEARCH SUBAGENT
from langchain.agents import create_agent

# Give ONLY the research agent web search
#research_model = model.bind_tools([search_tool])

research_agent = create_agent(
    #model=research_model,
    model=model,
    #tools=[],
    tools=[search_tool],
    system_prompt="""
        You are a senior news research analyst.

        Use web search for recent events, breaking news,
        companies, markets, regulations, and their impact.

        Always cite your findings.
        """
)


#CREATE CONTENT WRITE SUBAGENT
content_writer = create_agent(
    model=model,
    tools=[],
    system_prompt="""
        You are an expert news and business content writer.

        Create:

        - News explainers
        - Event summaries
        - Business analysis
        - LinkedIn posts
        - Breaking-news content

        Write clearly, factually, and engagingly.
        """
)


#WRAP THE SUBAGENTS AS TOOLS
from langchain.tools import tool

@tool
def research(query: str) -> str:
    """
    Research recent news and business events about stock market.
    """

    print("\n" + "=" * 60)
    print("Executing Research Agent")
    print("=" * 60)
    print(query)
    print()

    result = research_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": query
                }
            ]
        }
    )

    answer = result["messages"][-1].text

    print("\nResearch Agent Finished.\n")

    return answer


@tool
def write_marketing_copy(prompt: str) -> str:
    """
    Create news and business content.
    """

    print("\n" + "=" * 60)
    print("Executing Content Writer Agent")
    print("=" * 60)
    print(prompt)
    print()

    result = content_writer.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
    )

    answer = result["messages"][-1].text

    print("\nContent Writer Finished.\n")

    return answer


#CREATE SUPERVISOR AGENT
supervisor = create_agent(
    model=model,

    tools=[
        research,
        write_marketing_copy
    ],

    system_prompt="""
           You are the News Research Supervisor.

            Delegate work to the appropriate specialist.

            Use:

            - research()
                For recent events, companies, markets, regulations, and causes.

            - write_marketing_copy()
                For news explainers, summaries and LinkedIn posts.

            Combine the results into one final response.
            """
)


#INVOKE SUPERVISOR AGENT
response = supervisor.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": 
                    """
                    Research the recent PB Fintech (Policybazaar) stock crash.

                    Find:

                    - What happened
                    - Why the stock fell sharply
                    - What IRDAI proposed
                    - Potential business impact
                    - What happened after the crash

                    Then create a concise LinkedIn post explaining the event.
                    Use current sources and clearly distinguish facts from analysis.
                    """
            }
        ]
    }
)

print("\n" + "=" * 60)
print("FINAL RESPONSE")
print("=" * 60)
print(response["messages"][-1].text)

