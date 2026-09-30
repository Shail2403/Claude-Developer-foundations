import os 
from dotenv import load_dotenv

load_dotenv()

cMN = os.getenv("CLAUDE_MODEL_NAME")
cAK = os.getenv("CLAUDE_API_KEY")

import anthropic    

client = anthropic.Anthropic(api_key=cAK)

from anthropic.types import TextBlock

with open("./Model-Capabilities/Docs/file1.txt", "r") as f:
    file1 = f.read()

with open("./Model-Capabilities/Docs/file2.txt", "r") as f:
    file2 = f.read()

response = client.messages.create(
    model = cMN,
    max_tokens = 500,
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "document",
                    "source": {
                        "type": "text",
                        "media_type": "text/plain",
                        "data": file1
                    },
                    "title": "file1.txt",
                    "context": "This is the first document about GreenSteel Ltd. Sustainability overview.",
                    "citations": {"enabled": True}
                },
                {
                    "type": "document",
                    "source": {
                        "type": "text",
                        "media_type": "text/plain",
                        "data": file2
                    },
                    "title": "file2.txt",
                    "context": "This is the first document about Ecologistics International Sustainability overview.",
                    "citations": {"enabled": True}
                },
                {
                    "type": "text",
                    "text": "Please give me a sustainability overview for GreenSteel Ltd. Do not exceed 50 words."
                }
            ]
        }
    ]
)

print("\n" + "=" * 80)
print("Claude Response")
print("=" * 80)

for block in response.content:

    #answer=""
    if block.type != "text":
        continue
        #answer+=block.text

    print(block.text)

    if block.citations:
        print("\n📖 Citations:")

        for citation in block.citations:
            print(f"  • Source : {citation.document_title}")
            print(f"    Text   : {citation.cited_text}") #original file text

    print()