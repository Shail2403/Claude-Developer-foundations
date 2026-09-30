import os 
from dotenv import load_dotenv

load_dotenv()

cMN = os.getenv("CLAUDE_MODEL_NAME")
cAK = os.getenv("CLAUDE_API_KEY")

import anthropic    

client = anthropic.Anthropic(api_key=cAK)


#IMPLEMENT THE WEATHER API CALL
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

#IMPLEMENT THE AGENT LOOP
messages = [
    {
        "role": "user",
        "content": "Give me code snippet to create Foundry Client using SDK via MSLearn Docs?"
    }
]

while True:
    response = client.beta.messages.create(
        model = cMN,
        max_tokens = 2555,
        betas = ["mcp-client-2025-11-20"],
        messages = messages,
        mcp_servers = [
            {
                        "type": "url",
                        "url": "https://learn.microsoft.com/api/mcp",
                        "name": "MSLearnMCPServer"
            }
        ],
        tools = [
            {"type": "mcp_toolset", "mcp_server_name": "MSLearnMCPServer"},
            {
                        "name": "GetCurrentWeather",
                        "description": "Retrieve the current weather information for a specified location using the wttr.in weather service.",
                        "input_schema": {
                            "type": "object",
                            "properties": {
                                "location": {
                                    "type": "string",
                                    "description": "City or location to retrieve the weather for, for example London, New York, or Mumbai."
                                },
                            },
                            "required": ["location"]
                    }
            },
        ]
    )

    messages.append(
        {
            "role": "assistant",
            "content": response.content
        }
    )

    tool_used = False

    for block in response.content:
        if block.type == "text":
            print(block.text + "\n\n")

        elif block.type == "tool_use":

            tool_used = True

            if block.name == "GetCurrentWeather":

                print("Invoking GetCurrentWeather Tool \n\n")
                weather = get_current_weather(
                    block.input["location"]
                )

                messages.append(
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "tool_result",
                                "tool_use_id": block.id,
                                "content": str(weather)
                            }
                        ]
                    }
                )

    if not tool_used:
        break