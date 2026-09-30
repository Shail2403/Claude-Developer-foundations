import os 
from dotenv import load_dotenv

load_dotenv()

cMN = os.getenv("CLAUDE_MODEL_NAME")
cAK = os.getenv("CLAUDE_API_KEY")

import anthropic    

client = anthropic.Anthropic(api_key=cAK)


#CREATE AGENT
# agent = client.beta.agents.create(
#     name="BotAssistant-Managed-Agent",
#     model=cMN,
#     system="You are a helpful AI Assistant.",
#     tools=[
#         {"type": "agent_toolset_20260401"},
#     ],
# )

# print(f"Agent ID: {agent.id}, version: {agent.version}")


#CREATE SANDBOXED ENVIRONMENT
# environment = client.beta.environments.create(
#     name="quickstart-env",
#     config={
#         "type":"cloud",#self_hosted
#         "networking":{"type":"unrestricted"},
#         #  [
#         #         {
#         #             "type": "web_search",
#         #             "name": "web_search",
#         #             "allowed_domains": [
#         #                 "docs.anthropic.com",
#         #                 "platform.claude.com",
#         #                 "github.com",
#         #             ],
#         #         },
#         #         {
#         #             "type": "web_fetch",
#         #             "name": "web_fetch",
#         #             "allowed_domains": [
#         #                 "docs.anthropic.com",
#         #                 "platform.claude.com",
#         #                 "github.com",
#         #             ],
#     },
# )

# print(f"Environment ID: {environment.id}")


#FETCH FROM CLAUDE IF ALREADY CREATED
agents = client.beta.agents.list()
agent = next(
    a for a in agents.data
    if a.name == "BotAssistant-Managed-Agent"
)

environments = client.beta.environments.list()
environment = next(
    e for e in environments.data
    if e.name == "quickstart-env"
)


#CREATE SESSION
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    title="Quickstart session",
)

print(f"Session ID: {session.id}")


#START AGENT LOOP
chat = True

while chat:
    user_query = input("Enter ""exit"" or your user query to continue")

    if user_query == "exit":
        chat = False
    else:
        with client.beta.sessions.events.stream(session.id) as stream:
            # Send the user message after the stream opens
            client.beta.sessions.events.send(
                session.id,
                events=[
                    {
                        "type": "user.message",
                        "content": [
                            {
                                "type": "text",
                                "text": user_query,
                            },
                        ],
                    },
                ],
            )

            # Process streaming events
            for event in stream:
                match event.type:
                    case "agent.message":
                        for block in event.content:
                            print(block.text, end="")
                    case "agent.tool_use":
                        print(f"\n[Using tool: {event.name}]")
                    case "session.status_idle":
                        print("\n\nAgent finished.")
                        break










#                     Session ID: sesn_01VQaEGJqrNCZ1w8ucPrcSdq
# Enter exit or your user query to continueWrite python code to list my whole folderstructer and lis tof file sin very interactive and ui and iconic way and run that pytohn code so i can see on localhost 9000
# I'll create an interactive web application with a beautiful file explorer UI that runs on localhost:9000. Let me build this for you!
# [Using tool: write]
# Now let me run the Flask application:
# [Using tool: bash]
# Perfect! ✅ Your **Interactive File Explorer** is now running on **http://localhost:9000**!

# ## 🎯 Features Available:

# ✨ **Interactive UI Elements:**
# - 📁 **Expandable folder tree** - Click the arrows to expand/collapse
# - 📄 **File icons** - Different emoji icons for different file types (Python 🐍, Images 🖼️, Zips 📦, etc.)
# - 🎨 **Color-coded display** - Hover effects and selections
# - 📊 **Live statistics** - Shows folder count, file count, and total items
# - 🎯 **File sizes** - Shows size for each file
# - 🔍 **Path navigation** - Navigate to any folder path
# - 🏠 **Quick buttons** - Root, Home, and Refresh buttons
# - 📍 **Breadcrumb display** - Shows current location
# - 💻 **Smooth animations** - Nice transitions and hover effects

# ## 📝 How to Use:

# 1. **Browse** - Expand folders by clicking the ▼ arrow
# 2. **Navigate** - Double-click a folder to navigate into it
# 3. **Enter path** - Type any path in the input field and click "📂 Navigate"
# 4. **Quick access** - Use the buttons for Root, Home, or to Refresh

# The server is running in the background and will display all folder structures with icons in a beautiful, interactive interface! 

# Open your browser and go to: **http://localhost:9000** 🌐

# Agent finished.
# Enter exit or your user query to continue