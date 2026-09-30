import os 
from dotenv import load_dotenv

load_dotenv()

cMN = os.getenv("CLAUDE_MODEL_NAME")
cAK = os.getenv("CLAUDE_API_KEY")

import anthropic    

client = anthropic.Anthropic(api_key=cAK)

#IMPLEMENT WEATHER API CALL
import requests

def get_current_weather(location: str):

    response = requests.get(
        f"https://wttr.in/{location}",
        params={
            "format": "j1"
        }
    )

    response.raise_for_status()

    return response.json()


#IMPLEMENT SUM FUNCTION
def calculate_sum(a: int, b: int) -> str:
    return str(a*a + b*b)


#USING MESSAGES API
messages = [
    {
        "role": "user",
        "content": "What is the weather in Goa like currently?"
    }
]

while True:

    response = client.beta.messages.create(

        model=cMN,

        max_tokens=4096,

        messages=messages,

        mcp_servers=[
            {
                "type": "url",
                "url": "https://learn.microsoft.com/api/mcp",
                "name": "Microsoft Learn"
            }
        ],

        tools=[

            {
                "type": "tool_search_tool_bm25_20251119", #natural lang search
                "name": "tool_search_tool_bm25"
            },

            {
                "type": "mcp_toolset",
                "mcp_server_name": "Microsoft Learn",
                "default_config": {
                    "enabled": True,
                    "defer_loading": True  #not load upfrontly
                }
            },

            {
                "name": "GetCurrentWeather",
                "description": "Retrieve the current weather information for a specified location using the wttr.in weather service.",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "City or location to retrieve the weather for."
                        }
                    },
                    "required": ["location"]
                },
                "defer_loading": True
            },

            {
                "name": "CalculateStarSum",
                "description": "Calculate the sum of two integer numbers and return the result.",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "a": {
                            "type": "integer",
                            "description": "First integer."
                        },
                        "b": {
                            "type": "integer",
                            "description": "Second integer."
                        }
                    },
                    "required": ["a", "b"]
                },
                "defer_loading": True
            }

        ],

        betas=["mcp-client-2025-11-20"]

    )


    # Add Claude's response to the conversation
    messages.append(
        {
            "role": "assistant",
            "content": response.content
        }
    )

    tool_used = False


    # Process every content block
    for block in response.content:

        if block.type == "text":

            print(block.text)

        elif block.type == "tool_use":

            tool_used = True

            print(f"\nInvoking Tool: {block.name}\n")

            # Local Weather Tool
            if block.name == "GetCurrentWeather":

                result = get_current_weather(
                    block.input["location"]
                )

            # Local Calculator Tool
            elif block.name == "CalculateSum":

                result = calculate_sum(
                    block.input["a"],
                    block.input["b"]
                )

            # Skip MCP tools
            else:

                # MCP tools are executed server-side by Claude
                continue

            
            # Return tool result
            messages.append(
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": str(result)
                        }
                    ]
                }
            )

    # Exit if no local tool was invoked
    if not tool_used:
        break