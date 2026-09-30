# import statements
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, ResultMessage
import os
from dotenv import load_dotenv
import asyncio
from anthropic import beta_tool
import httpx
from typing import Any

load_dotenv()

os.environ["ANTHROPIC_API_KEY"] = os.getenv("CLAUDE_API_KEY")
cMN = os.getenv("CLAUDE_MODEL_NAME")

async def main():

    async for message in query(
        prompt="Give me python code snippet for Microsoft Foundry SDK Client Creation using the MSLearn MCP Server",
        options=ClaudeAgentOptions(
            model=cMN,
            mcp_servers = {"MSLearnMCPServer": {
                               "type": "http",
                               "url": "https://learn.microsoft.com/api/mcp"
                           }},
            allowed_tools = ["mcp__MSLearnMCPServer__*", "Read", "Edit", "Glob", "WebSearch", "WebFetch"]
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




# Tool: ToolSearch
# Tool: mcp__MSLearnMCPServer__microsoft_code_sample_search
# Tool: mcp__MSLearnMCPServer__microsoft_docs_search
# Here are the Python code snippets for Microsoft Foundry SDK Client Creation based on official Microsoft Learn documentation:

# ## 1. **AIProjectClient** (Foundry-Native Operations)

# ```python
# from azure.identity import DefaultAzureCredential
# from azure.ai.projects import AIProjectClient

# # Format: "https://resource_name.services.ai.azure.com/api/projects/project_name"
# FOUNDRY_PROJECT_ENDPOINT = "https://<your-foundry-account>.services.ai.azure.com/api/projects/<your-project>"

# # Create project client to call Foundry API
# project = AIProjectClient(
#     endpoint=FOUNDRY_PROJECT_ENDPOINT,
#     credential=DefaultAzureCredential(),
# )

# print(f"Project client created successfully: {project}")
# ```

# ## 2. **FoundryChatClient** (Agent Framework Integration)

# ```python
# import os
# from agent_framework.foundry import FoundryChatClient
# from azure.identity import DefaultAzureCredential

# # Using environment variables
# client = FoundryChatClient(
#     project_endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
#     model=os.environ["FOUNDRY_MODEL"],
#     credential=DefaultAzureCredential(),
# )

# # Or with explicit configuration
# client = FoundryChatClient(
#     project_endpoint="https://your-project.services.ai.azure.com",
#     model="gpt-4o-mini",
#     credential=DefaultAzureCredential(),
# )

# print("FoundryChatClient created successfully")
# ```

# ## 3. **AIProjectClient with OpenAI-Compatible Client**

# ```python
# import os
# from azure.identity import DefaultAzureCredential
# from azure.ai.projects import AIProjectClient

# # Create Foundry project client
# endpoint = os.getenv("FOUNDRY_PROJECT_ENDPOINT")

# with DefaultAzureCredential() as credential:
#     project = AIProjectClient(
#         endpoint=endpoint,
#         credential=credential,
#     )
    
#     # Get OpenAI-compatible client for model operations
#     openai_client = project.get_openai_client()
    
#     print(f"OpenAI-compatible client created from project: {openai_client}")
# ```

# ## 4. **Installation Requirements**

# ```bash
# # For AIProjectClient (Foundry SDK 2.x - Stable)
# pip install "azure-ai-projects>=2.3.0" "openai>=3.0.0"

# # For FoundryChatClient (Agent Framework)
# pip install agent-framework-foundry

# # For authentication
# pip install azure-identity
# ```

# ## 5. **Environment Variables Setup**

# ```bash
# # Required environment variables
# export FOUNDRY_PROJECT_ENDPOINT="https://<your-foundry-account>.services.ai.azure.com/api/projects/<your-project>"
# export FOUNDRY_MODEL="gpt-4o-mini"  # or your deployed model name
# export AZURE_AI_PROJECT_ENDPOINT="https://<resource-name>.services.ai.azure.com/api/projects/<project-name>"
# ```

# ## Key Differences:

# | Client | Use Case | When to Use |
# |--------|----------|------------|
# | **AIProjectClient** | Foundry-native operations (agents, toolboxes, skills, connections) | Setup, configuration, project management |
# | **FoundryChatClient** | Direct inference with Agent Framework | Your app owns agent definition & conversation loop |
# | **OpenAI-compatible client** | OpenAI-style API calls (completions, files, fine-tuning) | Model operations, evaluations, file uploads |

# **Python version requirement**: Python 3.10 or later

# These clients provide authentication via `DefaultAzureCredential` which works with Azure CLI login, managed identities, and service principals.

# Completed: success