import os 
from dotenv import load_dotenv

load_dotenv()

cMN = os.getenv("CLAUDE_MODEL_NAME")
cAK = os.getenv("CLAUDE_API_KEY")


#IMPLEMENT WEATHER API CALLER
import requests
from typing import Annotated     #typing_extensions->Annotated
from fastapi import Depends

def get_current_weather(
        location: Annotated[str, ..., "Location for which the weather condition needs to be fetched"]
    ):

    response = requests.get(
        f"https://wttr.in/{location}",
        params={
            "format": "j1"
        }
    )

    response.raise_for_status()

    return response.json()


from langchain_anthropic import ChatAnthropic
# model = ChatAnthropic(
#     model_name = cMN,
#     api_key = cAK
# )


#BUILD MODEL WITH TOOL
# from langchain_core.messages import HumanMessage, ToolMessage

# model_with_tools = model.bind_tools([get_current_weather])

# # User message
# messages = [
#     HumanMessage("What is the weather of กรุงเทพมหานคร currently like?")
# ]

# # First model call
# response = model_with_tools.invoke(messages)

# # Add assistant message containing tool call
# messages.append(response)

# #EXECUTE EVERY REQUESTED TOOL CALL
# for tool_call in response.tool_calls:

#     if tool_call["name"] == "get_current_weather":

#         result = get_current_weather(**tool_call["args"])

#         messages.append(
#             ToolMessage(
#                 content=str(result),
#                 tool_call_id=tool_call["id"]
#             )
#         )

# #SECOND MODEL CALL FOR TOOL OUTPUT SUMMARIZATION
# final_response = model_with_tools.invoke(messages)

# print(final_response.content)


#MCP SERVER
from anthropic.types.beta import BetaMCPToolsetParam

mcp_servers = [
    {
        "type": "url",
        "url": "https://learn.microsoft.com/api/mcp",
        "name": "Microsoft Learn",
    }
]

mcp_tool = BetaMCPToolsetParam(
    type="mcp_toolset",
    mcp_server_name="Microsoft Learn",
)


#RECREATE MODEL
model = ChatAnthropic(
    model_name = cMN,
    api_key = cAK,
    mcp_servers = mcp_servers
)


#INVOKE MODEL
response = model.invoke(
    "Compare Azure Functions and Container Apps for a FastAPI backend with bursty traffic, focusing on scaling, networking, and cost.",
    tools = [mcp_tool]
)

print(response.text)