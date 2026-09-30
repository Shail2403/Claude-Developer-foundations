import os
from dotenv import load_dotenv
load_dotenv()

cMN = os.getenv("CLAUDE_MODEL_NAME")
cAK = os.getenv("CLAUDE_API_KEY")

import anthropic
client = anthropic.Anthropic(api_key=cAK)

#WEB FETCH TOOL USE WITH THE CLAUDE API
response = client.messages.create(
    model=cMN,
    max_tokens=555,
    messages=[
        {
            "role": "user",
            "content": " Summarize the repository, identify the major folders, and explain what a learner can expect to find - https://github.com/kuljotSB/Claude-Certified-Developer-CCDV-F ",
        }
    ],
    tools=[{"type": "web_fetch_20260318", "name": "web_fetch", "max_uses": 3}],
)

for block in response.content:
    if block.type == "text":
        print(block.text)