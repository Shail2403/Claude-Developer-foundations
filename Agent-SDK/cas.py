# import statements
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, ResultMessage
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

os.environ["ANTHROPIC_API_KEY"] = os.getenv("CLAUDE_API_KEY")
cMN = os.getenv("CLAUDE_MODEL_NAME")


async def main():

    async for message in query(
        prompt="Review utils.py for bugs that would cause crashes. Fix any issues you find.",
        options=ClaudeAgentOptions(
            model=cMN,
            allowed_tools=["Read", "Edit", "Glob"], #Write,Bash,Powershell
            permission_mode="acceptEdits",
        ),
    ):

        if isinstance(message, AssistantMessage):

            for block in message.content:

                if hasattr(block, "text"):
                    print(block.text)

                elif hasattr(block, "name"):
                    print(f"Tool: {block.name}")

        elif isinstance(message, ResultMessage):

            print(f"\nCompleted: {message.subtype}")


asyncio.run(main())





# python3 Agent-SDK/cas.py 
# Tool: Glob
# Tool: Read
# I found **two crash-inducing bugs** in utils.py:

# 1. **`calculate_average` (line 5)**: Division by zero if an empty list is passed
# 2. **`get_user_name` (line 9)**: KeyError if user dict doesn't have "name" key, or TypeError if user is None

# Let me fix these:
# Tool: Edit
# Tool: Edit
# Tool: Read
# ## Summary of Fixes

# ### Bug #1: Division by Zero in `calculate_average()`
# **Issue:** Calling `calculate_average([])` would crash with `ZeroDivisionError` when dividing by 0.

# **Fix:** Added a guard clause to check if the list is empty and raise a descriptive `ValueError` instead.

# ### Bug #2: Unsafe Dict Access in `get_user_name()`
# **Issues:** 
# - Passing `None` → crashes with `TypeError`
# - Passing a non-dict object → crashes with `TypeError`
# - Missing "name" key → crashes with `KeyError`
# - Non-string name value → crashes with `AttributeError`

# **Fix:** Added comprehensive input validation:
# - Check that `user` is not None and is a dictionary
# - Check that "name" key exists in the dictionary
# - Check that the value is a string before calling `.upper()`

# Both functions now provide clear, descriptive error messages instead of cryptic Python exceptions.

# Completed: success
