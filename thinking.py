import os 
from dotenv import load_dotenv

load_dotenv()

cMN = os.getenv("CLAUDE_MODEL_NAME")
cAK = os.getenv("CLAUDE_API_KEY")

import anthropic    
from datetime import datetime

client = anthropic.Anthropic(api_key=cAK)


user_prompt = """
You are a senior digital marketing consultant.

A client's e-commerce website has experienced the following issues over the past three months:

- Website traffic has decreased by 35%
- Conversion rate has dropped from 3.8% to 1.7%
- Bounce rate has increased to 72%
- Mobile visitors account for 80% of all traffic

Recommend a recovery strategy.

For each recommendation:

- Explain why it should be prioritized.
- Describe its expected business impact.
- Identify any risks or trade-offs.
"""

# response = client.messages.create(
#         model=cMN,
#         max_tokens=1025,
#         thinking = {
#             "type":"enabled", #"enabled"/"disabled"
#             "budget_tokens": 1024,

#             #"display":"summarized" #"full"/"none"
#         },
#         messages=[
#             {
#                 "role":"user",
#                 "content":user_prompt
#             }
#         ]
# )

# for block in response.content:
#     if block.type=="thinking":
#         print(f"\nThinking: {block.thinking}")
#     elif block.type=="text":
#         print(f"\nResponse: {block.text}")


#STREAM OUTPUT WITH THINKING ADAPTIVE THINKING
# with client.messages.stream(
#     model = cMN,
#     max_tokens = 1300,
#     thinking = {"type": "adaptive", "display": "summarized"},
#     messages = [
#         {
#             "role": "user",
#             "content": user_prompt
#         }
#     ] 
# ) as stream:
#     for event in stream:
#         if event.type == "content_block_start":
#             print(f"\nStarting {event.content_block.type} block...")
#         elif event.type == "content_block_delta":
#             if event.delta.type == "thinking_delta":
#                 print(event.delta.thinking, end="", flush=True)
#             elif event.delta.type == "text_delta":
#                 print(event.delta.text, end="", flush=True)