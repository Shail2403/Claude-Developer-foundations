import os
from dotenv import load_dotenv
load_dotenv()

cMN = os.getenv("CLAUDE_MODEL_NAME")
cAK = os.getenv("CLAUDE_API_KEY")

import anthropic
client = anthropic.Anthropic(api_key=cAK)

#MESSAGES API WITH THE WEB SEARCH TOOL
response = client.messages.create(
    model = cMN,
    max_tokens = 50,
    messages = [
        {
            "role": "user",
            "content": "India cricket team tour of Japan 2026 stadium name?"
        }
    ],
    tools = [{"type": "web_search_20260318", "name": "web_search"}]
)

for block in response.content:
    if block.type == "text":
        print(block.text)

    elif block.type == "web_search_tool_result":

        print("\n" + "-" * 80)
        print("Search Results")
        print("-" * 80)

        for result in block.content:

            print(f"Title : {result.title}")
            print(f"URL   : {result.url}")
            print(f"Date  : {result.page_age}")
            print()

