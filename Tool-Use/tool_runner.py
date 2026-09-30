import os
from dotenv import load_dotenv
load_dotenv()

cMN = os.getenv("CLAUDE_MODEL_NAME")
cAK = os.getenv("CLAUDE_API_KEY")

import anthropic
client = anthropic.Anthropic(api_key=cAK)


#DEFINING THE USER-DEFINED FUNCTIONS
import json
import requests
from anthropic import beta_tool

@beta_tool
def get_weather(location: str) -> str:
    """Get the current weather in a given location.
    
    Args:
        location: The city whose weather details need to be fetched
    """

    response = requests.get(
            f"https://wttr.in/{location}",
            params={
                "format": "j1"
            }
        )
    
    response.raise_for_status()
    
    return str(response.json())


@beta_tool
def calculate_sum(a: int, b: int) -> str:
    """Add two numbers together.

    Args:
        a: First number
        b: Second number
    """
    return str(a)+" "+str(b)


#IMPLEMENT THE TOOL RUNNER WITH ANTHROPIC CLIENT
runner = client.beta.messages.tool_runner(
    model = cMN,
    max_tokens = 1900,
    tools = [get_weather, calculate_sum],
    messages = [
        {
            "role": "user",
            "content": "What's the weather like in Bermuda Triangle? Also, what's 15 + 27"
        }
    ]
)

for message in runner:
    if message.role == "assistant":

        for block in message.content:

            if block.type == "text":

                print("\n Assistant")
                print("-"*80)
                print(block.text)

            elif block.type == "tool_use":
                print("\nTool Call")
                print("-" * 80)

                print(f"Tool : {block.name}")

                print("Arguments:")

                for key, value in block.input.items():
                    print(f"  {key}: {value}")

    print("\n" + "=" * 80 + "\n")




















#ParsedBetaMessage[TypeVar](id='msg_011CfKdJdUL7otE9D4hJxrKT', container=None, content=[BetaToolUseBlock(id='toolu_01AJr4BforzCQY9yRTtMv3Ps', input={'location': 'Bermuda Triangle'}, name='get_weather', type='tool_use', caller=BetaDirectCaller(type='direct'), toolset_name=None), BetaToolUseBlock(id='toolu_01VEeMpU9PpWHR2jCKAHY1rW', input={'a': 15, 'b': 27}, name='calculate_sum', type='tool_use', caller=BetaDirectCaller(type='direct'), toolset_name=None)], context_management=None, diagnostics=None, model='claude-haiku-4-5-20251001', role='assistant', stop_details=None, stop_reason='tool_use', stop_sequence=None, type='message', usage=BetaUsage(cache_creation=BetaCacheCreation(ephemeral_1h_input_tokens=0, ephemeral_5m_input_tokens=0), cache_creation_input_tokens=0, cache_read_input_tokens=0, fallback_credit=None, inference_geo='not_available', input_tokens=706, iterations=None, output_tokens=110, output_tokens_details=None, server_tool_use=None, service_tier='standard', speed=None), input_transformations=None)
#ParsedBetaMessage[TypeVar](id='msg_011CfKdJvZF82pS89KezRvi8', container=None, content=[ParsedBetaTextBlock[TypeVar](citations=None, text="Great! Here's what I found:\n\n**Weather in Bermuda Triangle:**\nThe weather data shows conditions near the Bermuda Triangle area (around Turks and Caicos Islands):\n\n- **Current conditions:** Overcast with a temperature of 29°C (84°F)\n- **Humidity:** 76%\n- **Wind:** 27 km/h (17 mph) from the ESE\n- **Pressure:** 1015 mb\n- **Visibility:** 10 km\n\n**Forecast highlights:**\n- Temperatures remain consistently around 29°C (84-85°F)\n- Mostly overcast conditions with occasional light rain showers or patchy rain\n- Wind speeds vary between 17-27 km/h\n- Some isolated thunderstorms possible\n- High humidity levels (75-79%)\n\nThe weather looks fairly typical for the tropical Atlantic region with warm, humid conditions and occasional precipitation.\n\n**Math:** 15 + 27 = **42**", type='text', parsed_output=None)], context_management=None, diagnostics=None, model='claude-haiku-4-5-20251001', role='assistant', stop_details=None, stop_reason='end_turn', stop_sequence=None, type='message', usage=BetaUsage(cache_creation=BetaCacheCreation(ephemeral_1h_input_tokens=0, ephemeral_5m_input_tokens=0), cache_creation_input_tokens=0, cache_read_input_tokens=0, fallback_credit=None, inference_geo='not_available', input_tokens=13132, iterations=None, output_tokens=224, output_tokens_details=None, server_tool_use=None, service_tier='standard', speed=None), input_transformations=None)