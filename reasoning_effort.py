import os 
from dotenv import load_dotenv

load_dotenv()

cMN = os.getenv("CLAUDE_MODEL_NAME")
cAK = os.getenv("CLAUDE_API_KEY")

import anthropic    
from datetime import datetime

client = anthropic.Anthropic(api_key=cAK)



user_prompt = """
            You are a **Senior Staff Software Engineer, Debugging Analyst, Security Engineer, and Business Reviewer**.

            Analyze my code/project with an **extreme developer mindset**.

            Focus on:

            1. **Critical bugs & runtime failures**
            2. **Security vulnerabilities / data leaks**
            3. **Incorrect business logic / business deficiencies**
            4. **Data integrity, concurrency, and edge cases**
            5. **Performance, scalability, and reliability**
            6. **Architecture and maintainability issues**
            7. **Only then: minor code quality improvements**

            For every finding:

            * Explain **what is wrong**
            * Explain **why it matters**
            * Show **how I should debug/prove it myself**
            * Give the **developer-level fix/reasoning**
            * Explain the potential **impact on the system/business**

            ### Priority

            Rank findings strictly:
            **CRITICAL → HIGH → MEDIUM → LOW**

            Do **not** waste tokens on LOW-priority issues until all higher-priority issues are addressed.

            Act as my **technical mentor**, not just a code generator. Challenge my assumptions, ask for missing evidence when necessary, and teach me how an experienced developer would investigate and debug the problem independently.
            """

print(f"\n\n### Reasoning Effort: {"medium".capitalize()}\n")

message = client.messages.create(
    model=cMN,
    system="You are helpful assistant",
    messages=[
        {
            "role":"user",
            "content":user_prompt
        }
    ],
    output_config={
        "effort":"low"
    },
    max_tokens=200
)

for block in message.content:
    if block.type=="text":
        print(block.text)


print("\n Stop reason:", message.stop_reason, " at", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("\n Usage stats:", message.usage)
print("\n\n" + "-"*80 + "\n\n")

