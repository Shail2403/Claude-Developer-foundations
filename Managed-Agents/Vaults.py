import os 
from dotenv import load_dotenv

load_dotenv()

cMN = os.getenv("CLAUDE_MODEL_NAME")
cAK = os.getenv("CLAUDE_API_KEY")
github_pat = os.getenv("GITHUB_PAT")

import anthropic 

client = anthropic.Anthropic(api_key=cAK)


#CREATE VAULT
vault = client.beta.vaults.create(
    display_name="GitBot PAT Vault",
    metadata={
        "github_username":"Shail2403"
    }
)

print(vault.id)


#REGISTER GITHUB PAT SECRET IN THAT VAULT
credential = client.beta.vaults.credentials.create(

    vault_id=vault.id,

    display_name="GitBot PAT Vault",

    auth={
        "type": "static_bearer",

        "mcp_server_url": "https://api.githubcopilot.com/mcp/",

        "token": github_pat
    }
)


#CREATE AGENT
agent = client.beta.agents.create(

    name="GitBot patternGPT Assistant",

    model=cMN,

    system= """
                You are an expert GitHub assistant.
            """,

    mcp_servers=[
        {
            "type": "url",
            "name": "GitHub",
            "url": "https://api.githubcopilot.com/mcp/"
        }
    ],

    tools=[
        {
            "type": "agent_toolset_20260401"
        },
        {
            "type": "mcp_toolset",
            "mcp_server_name": "GitHub",
            "default_config": {
                "permission_policy": {
                    "type": "always_allow"
                }
            }
        }
    ]
)

print(f"Agent ID: {agent.id}, version: {agent.version}")


#ENVIRONMENT
environment = client.beta.environments.create(
    name="gitBot-env",
    config={
        "type": "cloud",
        "networking": {"type": "unrestricted"},
    },
)

print(f"Environment ID: {environment.id}")


#SESSION
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    vault_ids=[vault.id]
)


#EXECUTE AGENT 
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
                                "text": """ Read the repo [Shail2403/patternGPT] completely (READ ONLY). Inspect README, requirements.txt, backend/, chroma/, chroma_db/, and .github/workflows/.
                                            Explain concisely:
                                            1. Problem
                                            2. Full request→response flow
                                            3. Key files/functions
                                            4. FastAPI role
                                            5. ChromaDB + embeddings + similarity search
                                            6. Mistral/LLM role
                                            7. Where retrieved context enters the LLM prompt
                                            8. GitHub Actions
                                            9. Key architecture decisions/tradeoffs
                                            Cite exact file/function/class names. Distinguish facts from inference. Focus on important technical details; skip trivial code. Don't modify or suggest changes.
                                        """,
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






# I'll read this repository comprehensively. Let me start by fetching the repository structure and key files.Now let me read the README, requirements.txt, and explore all directories:Now let me read the backend app files and workflow files:Now let me read all the detailed source files:Now let me read the GitHub Actions workflow:Perfect! Now I have all the information. Let me create a comprehensive analysis document.
# [Using tool: write]
# Perfect! I've completed a comprehensive read-only analysis of the patternGPT repository. Here's a **concise summary**:

# ## **PatternGPT: Technical Overview**

# ### **1. Problem**
# AI-powered system to retrieve and explain Python coding patterns. Users query with natural language → system finds semantically similar patterns → generates explanations with executable code using an LLM.

# ### **2. Full Request→Response Flow**
# ```
# Query String → Query Embedding (ONNX MiniLM) → ChromaDB Vector Search → 
# Retrieve Top-K Pattern(s) → Build Prompt (context injection) → 
# Mistral LLM via OpenRouter → Parse Explanation + Code → Return JSON
# ```

# ### **3. Key Files/Functions**
# - **`backend/app/main.py`**: FastAPI server, route `/answer`, `call_mistral_model()`
# - **`backend/pattern_retriever.py`**: `OnnxEmbedder` class, `query_patterns()` semantic search
# - **`backend/pattern_answerer.py`**: High-level `answer_query()` orchestrator
# - **`backend/ingest_patterns.py`**: `ONNXMiniLMEmbedder`, `quick_regex_parse()`, `ingest()` pipeline
# - **`backend/pattern_codeDB.py`**: 38 curated Python patterns (printing, ASCII art)

# ### **4. FastAPI Role**
# HTTP REST server. Routes: `/health`, `/`, `/answer` (main endpoint with query param). Pydantic models enforce schema (`AnswerResponse`). Uses OpenAI SDK configured with OpenRouter base URL.

# ### **5. ChromaDB + Embeddings + Similarity Search**
# - **Embedding**: Text → ONNX MiniLM-L6-v2 (384-dim vectors, mean pooled + L2 normalized)
# - **Storage**: Persistent SQLite-based ChromaDB collection "patterns" (docs + embeddings + metadata)
# - **Retrieval**: Cosine similarity search returns top-k matching patterns with distances
# - **Ingestion**: Regex parse `pattern_codeDB.py` → extract descriptions + code → embed → store

# ### **6. Mistral/LLM Role**
# Model: `mistralai/mistral-small-3.2-24b-instruct:free` via OpenRouter. Receives prompt with injected retrieved pattern → generates explanation + Python code. Output parsed to extract code blocks (between ``` markers).

# ### **7. Where Retrieved Context Enters LLM Prompt**
# **`backend/app/main.py`, route `answer_query()` (line ~55-60)**:
# ```python
# best_doc = hits["documents"][0][0]  # Retrieved pattern
# prompt = f"""...\nReturned pattern: {best_doc}\n..."""  # ← Injected here
# explanation = call_mistral_model(prompt)
# ```
# Classic RAG pattern: retrieve relevant doc → inject into prompt template.

# ### **8. GitHub Actions CI/CD** 
# **`.github/workflows/ci.yml`**: Triggered on push to main + manual dispatch. Sets up Python 3.12, installs deps, runs `pattern_answerer.py` with configurable query (default: "triangle star pattern"). Uses `OPENROUTER_API_KEY` from secrets.

# ### **9. Key Architecture Decisions & Trade-offs**

# | Decision | Why | Trade-off |
# |----------|-----|-----------|
# | **ONNX MiniLM** (not cloud embeddings) | Offline, fast CPU, minimal deps | Lower quality than large models |
# | **Local ChromaDB** (not Pinecone) | Simple, portable, no DB server | Single-machine, no scaling |
# | **OpenRouter Mistral** (not self-hosted) | Free tier, no GPU needed | External API, latency risk, API key exposure |
# | **Top-K=1 default** | Fewer LLM calls, speed | May miss better matches nearby |
# | **Regex parsing** (not AST/agent) | Simple, deterministic | Brittle, no semantic understanding |
# | **Mean pooling + L2 norm** | Standard for embeddings | May dilute token importance vs. CLS-only |
# | **Separate ingestion pipeline** | Pre-compute once, fast queries | Re-ingest needed if patterns change |
# | **Markdown code extraction** (```) | Standard format, LLM-native | Fragile parsing, assumes specific format |

# ---

# **Critical Security Issue:** API key hardcoded in `backend/app/main.py` and `backend/pattern_answerer.py`.

# **Full detailed analysis saved to:** `/mnt/session/outputs/patternGPT_analysis.md`

# Agent finished.