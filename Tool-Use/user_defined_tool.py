import os
from dotenv import load_dotenv
load_dotenv()

cMN = os.getenv("CLAUDE_MODEL_NAME")
cAK = os.getenv("CLAUDE_API_KEY")

import anthropic
client = anthropic.Anthropic(api_key=cAK)


#DEFINE TOOL SCHEMA
tools = [
    {
        "name": "GetCurrentWeather",
        "description": "Retrieve the current weather information for a specified location using the wttr.in weather service.",
        "input_schema": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "City or location to retrieve the weather for, for example London, New York, or Mumbai."
                }
            },
            "required": ["location"]
        }
    }
]


#WEATHER API CALL 
import requests

def get_curr_weather(location:str):

    response=requests.get(
        f"https://wttr.in/{location}",
        params={
            "format":"j1"
        }
    )

    response.raise_for_status()
    return response.json()


#AGENT LOOP
messages=[
    {
        "role":"user",
        "content":"What's weather like in Bermuda Triangle today?"
    }
]

while True:
    response=client.messages.create(
        model=cMN,
        max_tokens=1400,
        tools=tools,
        tool_choice={"type":"auto"},
        messages=messages
    )
    messages.append(
        {
            "role":"assistant",
            "content":response.content
        }
    )

    tool_used=False

    for block in response.content:
        if block.type == "text":
            print(block.text + "\n\n")

        elif block.type == "tool_use":

            tool_used = True

            if block.name == "GetCurrentWeather":

                print("Invoking GetCurrentWeather Tool \n\n")
                weather = get_curr_weather(
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