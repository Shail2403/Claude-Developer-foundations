import os
from dotenv import load_dotenv

load_dotenv()

cMN = os.getenv("CLAUDE_MODEL_NAME")
cAK = os.getenv("CLAUDE_API_KEY")

from langchain_anthropic import ChatAnthropic
from langchain.agents import create_agent
from anthropic.types import WebSearchTool20260209Param


# ============================================================
# MODEL
# ============================================================

model = ChatAnthropic(
    model=cMN,
    api_key=cAK
)


# ============================================================
# WEB SEARCH TOOL
# ============================================================

search_tool = WebSearchTool20260209Param(
    name="web_search",
    type="web_search_20260209",
    max_uses=2,
)


# ============================================================
# RESEARCH AGENT
# ============================================================

research_agent = create_agent(
    model=model,
    tools=[search_tool],
    system_prompt="""
    You are a senior market research analyst.

    Research the given topic using web search when
    current information is required.

    Return concise findings with sources.
    """
)


# ============================================================
# WRITER AGENT
# ============================================================

writer_agent = create_agent(
    model=model,
    tools=[],
    system_prompt="""
    You are an expert marketing content writer.

    Based on the research provided to you,
    create professional and engaging marketing content.
    """
)


# ============================================================
# FINAL CLAUDE AGENT
# ============================================================

final_agent = create_agent(
    model=model,
    tools=[],
    system_prompt="""
    You are the final editor.

    Take the research and written content provided to you
    and produce the final polished response.

    Keep it concise and coherent.
    """
)


# ============================================================
# USER REQUEST
# ============================================================

user_query = """
We are launching a new AI-powered fitness smartwatch
called FitSense AI.

Identify:

- Target audience
- Customer pain points
- Current fitness wearable trends

Then create a professional LinkedIn launch announcement.
"""


# ============================================================
# STEP 1 — RESEARCH
# ============================================================

research_result = research_agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": user_query
        }
    ]
})

research_text = research_result["messages"][-1].text


# ============================================================
# STEP 2 — WRITE
# ============================================================

writer_result = writer_agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": f"""
            User request:

            {user_query}

            Research findings:

            {research_text}

            Based on these findings, create the LinkedIn
            launch announcement.
            """
        }
    ]
})

writer_text = writer_result["messages"][-1].text


# ============================================================
# STEP 3 — FINAL CLAUDE
# ============================================================

final_result = final_agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": f"""
            Original request:

            {user_query}

            Research:

            {research_text}

            Draft:

            {writer_text}

            Produce the final polished response.
            """
        }
    ]
})

final_text = final_result["messages"][-1].text


print("\n================ FINAL RESPONSE ================\n")
print(final_text)