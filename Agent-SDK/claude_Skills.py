import os
import asyncio

from claude_agent_sdk import (
    query,
    ClaudeAgentOptions,
    ResultMessage,
    AssistantMessage
)
from dotenv import load_dotenv

load_dotenv()

os.environ["ANTHROPIC_API_KEY"] = os.getenv("CLAUDE_API_KEY")
cMN = os.getenv("CLAUDE_MODEL_NAME")

async def main():

    options = ClaudeAgentOptions(
        model = cMN,
        cwd=os.getcwd(),
        setting_sources=["project"],
        skills=["marketing-review"],
        system_prompt="You are a professional marketing reviewer and employer of marketing company which prefers ANIME style posts so generally find anime contexts in linkedin posts while reviewing for increasing genZ reach.",
        max_turns=5,
        max_budget_usd=0.40,
        allowed_tools=["Read","Grep"],
        disallowed_tools=["Write","Edit"],
        permission_mode="default"
    )

    async for message in query(
        prompt="""
Review and improve this LinkedIn announcement.

"We're unbelievably excited to launch the most revolutionary AI smartwatch ever created! Buy now before you miss out forever!"
""",
        options=options,
    ):

        if isinstance(message, AssistantMessage):
        
            for block in message.content:

                if hasattr(block, "text") and block.text:
                    print(block.text)

                elif hasattr(block, "name"):
                    print(f"\n Tool Used: {block.name}")

        elif isinstance(message, ResultMessage):

            print("\n" + "=" * 80)
            print("FINAL RESPONSE")
            print("=" * 80)

            print(message.result)

            print("\nCompleted:", message.subtype)

asyncio.run(main())










# # LinkedIn Announcement Review & Improvement 🎨

# ## 🚨 Current Issues:

# 1. **Generic corporate hype** - "unbelievably excited," "most revolutionary" are overused phrases
# 2. **Fear-mongering tactics** - "before you miss out forever" feels pushy and inauthentic
# 3. **No personality** - Lacks voice, humor, or relatability for gen Z
# 4. **Zero cultural alignment** - Missing anime/pop culture references that resonate with younger audiences
# 5. **Lazy copywriting** - Screams "AI-generated marketing copy"

# ---

# ## ✨ Improved Versions (Anime-Inspired):

# ### **Option 1: "Main Character Energy" (Playful)**
# > Just dropped our AI smartwatch and honestly? It's giving protagonist vibes 🔥

# > Imagine your watch knowing what you need before you even ask (core memory moment 📍). While everyone else is grinding, yours is literally working 10 steps ahead.

# > Not us hyping it up unnecessarily—the specs speak for themselves. Check it out if you're ready to level up your tech game.

# > [Link]

# ---

# ### **Option 2: "Anime Plot Development" (Story-Driven)**
# > Plot twist: Your smartwatch just got a villain arc upgrade 👀

# > We spent months in our "training montage" to create something that actually slaps. This isn't another gimmick—it's your new daily W.

# > Real talk: if you've been waiting for tech that matches your energy, this is it.

# > [Link]

# ---

# ### **Option 3: "Power-Up Moment" (Gen Z Gaming Energy)**
# > New equipment unlocked: AI smartwatch 🎮✨

# > It's not just a gadget—it's your party member that runs the calculations while you focus on the big picture. Think of it as having a support character that actually supports you.

# > Available now. Your next level-up is waiting.

# > [Link]

# ---

# ## 🎯 Key Improvements Made:
# ✅ Removed aggressive sales language  
# ✅ Added anime/gaming references (main character, training montage, power-up)  
# ✅ Used authentic gen Z language  
# ✅ Created storytelling instead of hype  
# ✅ Built curiosity vs. FOMO  
# ✅ Maintained professionalism with personality  

# Which vibe resonates most with your brand? I can refine further! 🚀

# ================================================================================
# FINAL RESPONSE
# ================================================================================
# # LinkedIn Announcement Review & Improvement 🎨

# ## 🚨 Current Issues:

# 1. **Generic corporate hype** - "unbelievably excited," "most revolutionary" are overused phrases
# 2. **Fear-mongering tactics** - "before you miss out forever" feels pushy and inauthentic
# 3. **No personality** - Lacks voice, humor, or relatability for gen Z
# 4. **Zero cultural alignment** - Missing anime/pop culture references that resonate with younger audiences
# 5. **Lazy copywriting** - Screams "AI-generated marketing copy"

# ---

# ## ✨ Improved Versions (Anime-Inspired):

# ### **Option 1: "Main Character Energy" (Playful)**
# > Just dropped our AI smartwatch and honestly? It's giving protagonist vibes 🔥

# > Imagine your watch knowing what you need before you even ask (core memory moment 📍). While everyone else is grinding, yours is literally working 10 steps ahead.

# > Not us hyping it up unnecessarily—the specs speak for themselves. Check it out if you're ready to level up your tech game.

# > [Link]

# ---

# ### **Option 2: "Anime Plot Development" (Story-Driven)**
# > Plot twist: Your smartwatch just got a villain arc upgrade 👀

# > We spent months in our "training montage" to create something that actually slaps. This isn't another gimmick—it's your new daily W.

# > Real talk: if you've been waiting for tech that matches your energy, this is it.

# > [Link]

# ---

# ### **Option 3: "Power-Up Moment" (Gen Z Gaming Energy)**
# > New equipment unlocked: AI smartwatch 🎮✨

# > It's not just a gadget—it's your party member that runs the calculations while you focus on the big picture. Think of it as having a support character that actually supports you.

# > Available now. Your next level-up is waiting.

# > [Link]

# ---

# ## 🎯 Key Improvements Made:
# ✅ Removed aggressive sales language  
# ✅ Added anime/gaming references (main character, training montage, power-up)  
# ✅ Used authentic gen Z language  
# ✅ Created storytelling instead of hype  
# ✅ Built curiosity vs. FOMO  
# ✅ Maintained professionalism with personality  

# Which vibe resonates most with your brand? I can refine further! 🚀

# Completed: success