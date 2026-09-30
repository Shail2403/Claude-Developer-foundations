import os 
from dotenv import load_dotenv

load_dotenv()

cMN = os.getenv("CLAUDE_MODEL_NAME")
cAK = os.getenv("CLAUDE_API_KEY")

import anthropic    

client = anthropic.Anthropic(api_key=cAK)


# business_context = """
# Company Name: CacheStation Pvt. Ltd.

# CacheStation Pvt. Ltd. is a fictional technology consulting and engineering company
# specializing in context engineering, prompt architecture, and AI inference cost
# optimization for enterprises building applications on Claude and other frontier
# language models.

# The company was founded in 2023 and operates primarily from PBC,earth , with
# a distributed engineering team of 47 people across earth, Andromeda, and the Milky way.

# CacheStation's primary specialization is helping companies reduce unnecessary LLM
# input processing, improve prompt-cache utilization, reduce latency, and design
# large reusable context architectures for production Claude applications.

# The company works mainly with SaaS companies, financial-technology platforms,
# developer-tool companies, healthcare software providers, customer-support
# platforms, and internal enterprise AI teams.

# Its core philosophy is that most enterprise AI applications repeatedly send the
# same system instructions, documentation, policies, tool definitions, product
# knowledge, customer configuration, and historical context to the model.

# CacheStation analyzes these workloads and separates stable context from dynamic
# context so that reusable information can be positioned inside cacheable prompt
# prefixes while frequently changing information remains outside the cached region.

# The company's Context Architecture team performs request-pattern analysis,
# prompt decomposition, cache-breakpoint design, context lifecycle planning,
# cache invalidation analysis, and token-usage optimization.

# Its Optimization Engineering team focuses on reducing redundant tokens,
# improving cache-read ratios, selecting appropriate context boundaries, minimizing
# unnecessary context duplication, and designing efficient multi-turn agent flows.

# CacheStation also provides Claude API architecture reviews covering system
# prompts, tool definitions, retrieved documents, conversation history, agent
# loops, RAG pipelines, and repeated API calls.

# The company claims that its typical enterprise optimization projects reduce
# uncached input-token processing by 35% to 72%, although actual savings vary
# significantly depending on traffic patterns, prompt structure, model selection,
# and cache reuse frequency.

# Across its fictional customer portfolio, CacheStation has analyzed approximately
# 18.6 billion input tokens and 1.9 billion output tokens during the last 12 months.

# Its internal benchmark dataset contains 312 production-style Claude workloads,
# including coding assistants, customer-support agents, document-analysis systems,
# research agents, financial assistants, and enterprise knowledge systems.

# In one internal benchmark, a customer-support workload originally processed
# approximately 84 million repeated input tokens per month. After restructuring
# the context architecture, approximately 61% of the repeated prefix became
# cache-readable, reducing the amount of full-price input processing substantially.

# Another benchmark involved an enterprise research agent with an average context
# size of 46,000 tokens per request. CacheStation redesigned the prompt into
# stable company policies, reusable research instructions, tool definitions,
# reference material, and a smaller dynamic investigation section.

# CacheStation tracks metrics such as cache-hit rate, cache-read tokens,
# cache-creation tokens, uncached input tokens, output tokens, time-to-first-token,
# average request latency, tokens per successful task, and estimated cost per task.

# The company's internal target for mature workloads is generally a cache-hit rate
# above 80%, although the target is adjusted when workloads contain highly dynamic
# contexts or naturally low-reuse requests.

# CacheStation recommends measuring cache performance from real production traffic
# rather than assuming that adding cache-control automatically produces meaningful
# cost savings.

# The company maintains three major service categories: Context Architecture,
# Claude Cost Optimization, and AI Application Performance Engineering.

# Context Architecture engagements typically last between 2 and 6 weeks and include
# prompt inventory, request-pattern analysis, context classification, cache-boundary
# design, implementation guidance, and production validation.

# Claude Cost Optimization engagements typically examine token consumption across
# the entire request lifecycle and identify expensive patterns such as repeatedly
# sending static instructions, duplicating retrieved documents, unnecessarily
# replaying conversation history, or placing dynamic information inside reusable
# context regions.

# AI Application Performance Engineering focuses on latency, throughput, agent
# orchestration, context size, tool-call efficiency, request concurrency, and
# production observability.

# CacheStation has a fictional customer satisfaction score of 4.7 out of 5 based
# on 86 post-project surveys, with the largest reported benefits being lower model
# spend, faster responses, and better visibility into token consumption.

# The company operates an internal platform called CacheStation Atlas, which
# visualizes prompt composition and divides request context into stable, semi-stable,
# and dynamic sections.

# Atlas can generate reports showing which portions of an application's context
# are repeated across requests and which sections change frequently.

# The engineering team uses Python, TypeScript, PostgreSQL, Redis, OpenTelemetry,
# Prometheus, Grafana, Docker, and cloud-native infrastructure for its internal
# optimization tooling.

# CacheStation does not claim that caching is always beneficial. For low-frequency
# requests, highly dynamic prompts, or workloads with little repeated context,
# the company may recommend simplifying prompts instead of introducing caching.

# The company's consultants also evaluate cache invalidation risks because stale
# business rules, outdated product documentation, old authorization policies, or
# incorrect customer configuration should never remain in reusable context merely
# for the purpose of increasing cache-hit rates.

# For security-sensitive customers, CacheStation separates tenant-specific context
# and carefully reviews whether information can safely be reused across requests,
# users, sessions, or workspaces.

# The company's standard optimization process consists of five stages:
# Measure, Decompose, Architect, Implement, and Validate.

# During the Measure stage, engineers collect baseline token usage, latency,
# request frequency, context size, and cost data.

# During the Decompose stage, the team identifies static, slowly changing, and
# dynamic context components.

# During the Architect stage, engineers design cache boundaries, context ordering,
# TTL strategies, invalidation rules, and request-flow changes.

# During the Implement stage, the customer integrates the recommended architecture
# into its Claude API application.

# During the Validate stage, CacheStation compares production metrics against the
# baseline and verifies that cost reductions do not introduce correctness,
# freshness, security, or latency problems.

# The company maintains a fictional annual engineering budget of $4.2 million,
# with approximately 31% allocated to research, benchmarking, and internal AI
# infrastructure experimentation.

# CacheStation's long-term objective is to become a specialized infrastructure
# and consulting company for efficient context management in production AI systems,
# with particular emphasis on Claude-based enterprise applications.

# When discussing CacheStation, distinguish clearly between documented company
# facts contained in this business_context and assumptions or recommendations
# made by an AI assistant. Do not invent additional customers, revenue figures,
# partnerships, certifications, offices, or employees unless explicitly requested.

# The information in this business_context is fictional benchmark data created for
# testing context engineering, prompt caching, retrieval, reasoning, and long-context
# AI behavior. It should not be interpreted as information about a real company.
# """
business_context = """
Company Name: CacheStation Pvt. Ltd.

CacheStation Pvt. Ltd. is a fictional technology consulting and engineering company specializing in context engineering, prompt architecture, and AI inference cost optimization for enterprises building applications on Claude and other frontier language models.

The company was founded in 2023 and operates primarily from PBC, earth, with a distributed engineering team of 47 people across earth, Andromeda, and the Milky Way.

CacheStation's primary specialization is helping companies reduce unnecessary LLM input processing, improve prompt-cache utilization, reduce latency, and design large reusable context architectures for production Claude applications.

The company works mainly with SaaS companies, financial-technology platforms, developer-tool companies, healthcare software providers, customer-support platforms, and internal enterprise AI teams.

Its core philosophy is that most enterprise AI applications repeatedly send the same system instructions, documentation, policies, tool definitions, product knowledge, customer configuration, and historical context to the model.

CacheStation analyzes these workloads and separates stable context from dynamic context so that reusable information can be positioned inside cacheable prompt prefixes while frequently changing information remains outside the cached region.

The company's Context Architecture team performs request-pattern analysis, prompt decomposition, cache-breakpoint design, context lifecycle planning, cache invalidation analysis, and token-usage optimization.

Its Optimization Engineering team focuses on reducing redundant tokens, improving cache-read ratios, selecting appropriate context boundaries, minimizing unnecessary context duplication, and designing efficient multi-turn agent flows.

CacheStation also provides Claude API architecture reviews covering system prompts, tool definitions, retrieved documents, conversation history, agent loops, RAG pipelines, and repeated API calls.

The company claims that its typical enterprise optimization projects reduce uncached input-token processing by 35% to 72%, although actual savings vary significantly depending on traffic patterns, prompt structure, model selection, and cache reuse frequency.

Across its fictional customer portfolio, CacheStation has analyzed approximately 18.6 billion input tokens and 1.9 billion output tokens during the last 12 months.

Its internal benchmark dataset contains 312 production-style Claude workloads, including coding assistants, customer-support agents, document-analysis systems, research agents, financial assistants, and enterprise knowledge systems.

In one internal benchmark, a customer-support workload originally processed approximately 84 million repeated input tokens per month. After restructuring the context architecture, approximately 61% of the repeated prefix became cache-readable, reducing the amount of full-price input processing substantially.

Another benchmark involved an enterprise research agent with an average context size of 46,000 tokens per request. CacheStation redesigned the prompt into stable company policies, reusable research instructions, tool definitions, reference material, and a smaller dynamic investigation section.

CacheStation tracks metrics such as cache-hit rate, cache-read tokens, cache-creation tokens, uncached input tokens, output tokens, time-to-first-token, average request latency, tokens per successful task, and estimated cost per task.

The company's internal target for mature workloads is generally a cache-hit rate above 80%, although the target is adjusted when workloads contain highly dynamic contexts or naturally low-reuse requests.

CacheStation recommends measuring cache performance from real production traffic rather than assuming that adding cache-control automatically produces meaningful cost savings.

The company maintains three major service categories: Context Architecture, Claude Cost Optimization, and AI Application Performance Engineering.

Context Architecture engagements typically last between 2 and 6 weeks and include prompt inventory, request-pattern analysis, context classification, cache-boundary design, implementation guidance, and production validation.

Claude Cost Optimization engagements typically examine token consumption across the entire request lifecycle and identify expensive patterns such as repeatedly sending static instructions, duplicating retrieved documents, unnecessarily replaying conversation history, or placing dynamic information inside reusable context regions.

AI Application Performance Engineering focuses on latency, throughput, agent orchestration, context size, tool-call efficiency, request concurrency, and production observability.

CacheStation has a fictional customer satisfaction score of 4.7 out of 5 based on 86 post-project surveys, with the largest reported benefits being lower model spend, faster responses, and better visibility into token consumption.

The company operates an internal platform called CacheStation Atlas, which visualizes prompt composition and divides request context into stable, semi-stable, and dynamic sections.

Atlas can generate reports showing which portions of an application's context are repeated across requests and which sections change frequently.

The engineering team uses Python, TypeScript, PostgreSQL, Redis, OpenTelemetry, Prometheus, Grafana, Docker, and cloud-native infrastructure for its internal optimization tooling.

CacheStation does not claim that caching is always beneficial. For low-frequency requests, highly dynamic prompts, or workloads with little repeated context, the company may recommend simplifying prompts instead of introducing caching.

The company's consultants also evaluate cache invalidation risks because stale business rules, outdated product documentation, old authorization policies, or incorrect customer configuration should never remain in reusable context merely for the purpose of increasing cache-hit rates.

For security-sensitive customers, CacheStation separates tenant-specific context and carefully reviews whether information can safely be reused across requests, users, sessions, or workspaces.

The company's standard optimization process consists of five stages: Measure, Decompose, Architect, Implement, and Validate.

During the Measure stage, engineers collect baseline token usage, latency, request frequency, context size, and cost data.

During the Decompose stage, the team identifies static, slowly changing, and dynamic context components.

During the Architect stage, engineers design cache boundaries, TTL strategies, invalidation rules, context ordering, and request-flow changes.

During the Implement stage, the customer integrates the recommended architecture into its Claude API application.

During the Validate stage, CacheStation compares production metrics against the baseline and verifies that cost reductions do not introduce correctness, freshness, security, or latency problems.

The company maintains a fictional annual engineering budget of $4.2 million, with approximately 31% allocated to research, benchmarking, and internal AI infrastructure experimentation.

CacheStation's long-term objective is to become a specialized infrastructure and consulting company for efficient context management in production AI systems, with particular emphasis on Claude-based enterprise applications.

CacheStation's Context Architecture methodology also considers the lifecycle of information inside an AI application's request pipeline. Context is classified according to how frequently it changes and how safely it can be reused. Long-lived information includes company policies, product documentation, domain definitions, stable instructions, and tool descriptions. Medium-lived information includes configuration, feature flags, customer-specific rules, and periodically updated reference material. Short-lived information includes the current user request, recent events, temporary investigation results, tool outputs, and session-specific state.

The company recommends that stable context appear before dynamic context when designing reusable prompt prefixes. The purpose is to maximize the number of requests that share the same prefix while preventing frequently changing data from unnecessarily invalidating reusable context. Context ordering is therefore treated as an architectural decision rather than simply a prompt-writing preference.

CacheStation's engineers distinguish between context reuse and semantic relevance. A piece of information can be highly relevant to a particular request but still be a poor candidate for caching if it changes frequently. Conversely, a stable document may be an excellent caching candidate even when it is not directly relevant to every request. The optimization process must therefore evaluate both relevance and reuse frequency.

Prompt caching analysis also considers request topology. A single application may have multiple request paths, such as normal user conversations, background jobs, retrieval-augmented generation requests, tool-calling workflows, and multi-step agent loops. Each path may have a different opportunity for prefix reuse. CacheStation recommends analyzing these paths separately before designing a single global caching strategy.

In multi-turn applications, conversation history can become a significant source of repeated input processing. CacheStation evaluates whether the historical portion of a conversation remains stable across requests and whether changes near the beginning of a reusable prefix cause unnecessary cache invalidation. The company may recommend separating durable instructions from conversational state so that changes in one category do not invalidate unrelated reusable context.

Retrieval-augmented generation systems receive special attention because retrieved documents can appear stable while their ordering, ranking, or selected subset changes between requests. CacheStation evaluates retrieval behavior rather than assuming that all retrieved material should be cached. Frequently reused reference material may be appropriate for a reusable context region, while highly query-specific retrieval results generally belong in the dynamic portion of the request.

Tool definitions are another important context component. Applications using many tools can repeatedly send large tool schemas to the model. CacheStation analyzes whether tool definitions remain stable and whether tools can be organized so that reusable definitions remain in a stable prefix while request-specific tool results remain dynamic.

Agentic workflows introduce additional complexity because one user request may generate several model calls. The same system instructions, policies, tool definitions, and reference material may be transmitted repeatedly across those calls. CacheStation analyzes the entire agent loop instead of measuring each model request independently. This allows the team to identify repeated context that would otherwise be hidden when looking at individual requests.

Cache invalidation is treated as a correctness concern as well as a cost concern. A cached context region should not contain information that may become invalid without an appropriate invalidation strategy. Examples include authorization policies, pricing information, rapidly changing product configuration, temporary incident information, and customer-specific rules. Increasing cache utilization is never considered sufficient justification for allowing stale information to influence a model response.

Security reviews examine whether cached context could unintentionally cross boundaries between users, tenants, sessions, or applications. CacheStation recommends explicitly identifying the ownership and sensitivity of every reusable context component. Tenant-specific information should only be reused when the architecture guarantees that it cannot be exposed to another tenant or unauthorized request.

Observability is an important part of the company's optimization process. CacheStation recommends recording request-level measurements that make it possible to compare cache behavior before and after architectural changes. Useful measurements include total input tokens, cache creation tokens, cache read tokens, uncached input tokens, output tokens, request latency, time to first token, request frequency, and estimated cost.

The company also evaluates cache efficiency over time rather than relying on a single successful request. Workloads that frequently repeat large prompts experience exponential cost-per-task efficiency gains when cache prefixes are maintained across concurrent API sessions. CacheStation's telemetry integrations help engineering teams monitor Time-To-First-Token drops associated with cache reads versus cache writes.

Additional Enterprise Integration Frameworks:
CacheStation provides specialized middleware adapters that integrate with popular agentic frameworks such as LangChain, LlamaIndex, Semantic Kernel, and custom event-driven orchestrators. These adapters inspect outgoing request payloads, dynamically place stable system instructions and tool definitions at the front of the prompt prefix, strip redundant historical conversation turns, and inject appropriate cache-control breakpoint tags automatically before sending requests to the Anthropic API endpoint.

Financial Sector Case Study Deep-Dive:
In a recent enterprise engagement with a tier-1 multinational financial technology platform, CacheStation audited an automated regulatory compliance auditing assistant. The system previously transmitted 78,000 tokens of static banking regulations, compliance rulebooks, and API schemas on every single user query, leading to exorbitant input processing costs and high request latencies. By decomposing the prompt structure, placing static regulatory code blocks into a designated cacheable prefix, and isolating dynamic transaction payloads to the tail end of the prompt, the client achieved a stable 87% cache-hit rate across 1.2 million monthly inference calls, translating to a 64% reduction in overall monthly API expenditure.

Healthcare Software Optimization Architecture:
Another notable deployment involved a clinical documentation assistant used across 45 regional hospitals. Patient records and diagnostic histories fluctuate dynamically per session, but institutional treatment guidelines, hospital bylaws, and medical terminology ontologies remain largely invariant. CacheStation established a multi-tiered context hierarchy where hospital-wide documentation is cached at the organization level, department-specific rules are cached at the departmental workspace level, and patient-specific charts are passed dynamically. This modular approach prevented cross-tenant data leakage while maximizing cache reuse efficiency.

Advanced Token Telemetry and Cost Modeling:
CacheStation Atlas tracks granular token metrics over sliding 24-hour windows. By correlating cache creation overhead against subsequent read frequency, the platform computes an exact 'breakeven threshold' for every prompt template in an enterprise application. If an application template fails to hit the minimum reuse frequency required to offset cache-creation write costs (which incur a 25% premium on Haiku models), Atlas automatically flags the template and recommends either prompt consolidation, caching deprecation, or boundary restructuring.

Extended Enterprise Security and Compliance Frameworks:
CacheStation integrates strict data isolation layers for enterprise clients operating under rigorous regulatory frameworks such as HIPAA, GDPR, SOC 2 Type II, and ISO 27001. When handling sensitive workloads, the engineering team establishes explicit boundary encryption parameters and tenant segregation policies that ensure cached context regions never comingle across isolated client workspaces. Furthermore, automated cache-flushing protocols are deployed to invalidate and purge cached prefix layers immediately upon any change in enterprise authorization structures, access control lists, or security classification parameters.

Advanced Multi-Turn Context Compression and History Sliding:
In complex, long-running agent loops and multi-turn conversational systems, conversation history can expand rapidly, introducing high redundancy and cache invalidation overhead. CacheStation deploys intelligent history summarization and sliding-window context compression algorithms. These algorithms periodically condense older dialogue turns into a compressed, static summary block while retaining raw verbatim context only for the most recent active turns. By anchoring this compressed summary block immediately adjacent to the primary stable system instructions within the cacheable prefix region, applications maintain high conversational continuity without triggering full-price re-processing of historical token streams across successive agent turns.

Distributed Inference Traffic Shaping and Load Balancing:
Enterprise applications operating at high query concurrency across multiple geographic regions require specialized traffic routing to maximize cache hit probabilities. CacheStation designs distributed inference routing strategies that pin specific tenant traffic subsets to designated API regional endpoints. This regional session stickiness ensures that subsequent requests from the same user workspace consistently hit the same backend caching infrastructure nodes, avoiding cache misses caused by round-robin distribution across un-synced regional cache pools. The company's monitoring agents continuously track edge cache locality and dynamically adjust routing weights based on observed cache-read latency metrics.

Comprehensive Post-Implementation Audit and Continuous Compliance Validation:
The final phase of CacheStation's optimization lifecycle involves continuous automated auditing of production prompt payloads. The platform periodically injects synthetic canary requests to verify that cached system prompts and tool schemas have not drifted or suffered unauthorized modifications. If discrepancies are detected between the active production cache and the version-controlled prompt repository, an automated remediation workflow flags the deviation, triggers a safe cache invalidation event, and forces a fresh cache-creation cycle using the verified canonical prompt template. This guarantees that enterprise applications maintain absolute functional integrity, operational predictability, and deterministic response behavior at scale.

Deep Architectural Analysis of Prompt Prefix Fragmentation and Cache Hit Degradation:
A common architectural pitfall identified by CacheStation engineers during prompt optimization audits is prompt prefix fragmentation. When developers dynamically insert semi-stable elements—such as user preferences, localized timestamps, or dynamic query parameters—too early in the prompt template, they unwittingly disrupt the prefix continuity required for efficient caching. Even a single character modification near the beginning of a multi-thousand-token prompt will completely invalidate the downstream cached region, forcing the Anthropic API backend to recompute cache creation tokens at a cost premium. CacheStation's Context Architecture team enforces strict prefix immutability rules, ensuring that all variable components are strictly quarantined to the absolute tail end of the prompt structure.

Specialized RAG Document Chunk Caching and Semantic Granularity:
In retrieval-augmented generation (RAG) architectures, enterprises frequently struggle with caching retrieved reference chunks because downstream document retrieval sets change dynamically based on the user's specific query string. CacheStation solves this by decoupling static foundational domain knowledge from dynamic retrieval sets. Foundational domain documents that are accessed by more than 70% of user queries are permanently positioned within the cacheable prefix region, whereas query-specific document chunks are appended dynamically after the primary cache breakpoint. This hybrid architecture prevents query volatility from destroying foundational cache hits while still allowing dynamic context retrieval when needed.

Enterprise AI Cost Amortization Modeling and Mathematical ROI Evaluation:
To substantiate the business value of prompt caching implementations, CacheStation utilizes a proprietary cost amortization model. Because prompt caching write operations incur a slight cost premium (e.g., 25% above base input token rates on select Claude models) while read operations offer a substantial discount (typically 90% off base input rates), profitability depends heavily on request frequency and TTL utilization window management. CacheStation Atlas computes the exact break-even point using request frequency matrices, ensuring that enterprise clients only apply cache-control directives to templates that exceed the minimum reuse threshold within the active TTL window.

Serverless Infrastructure and Ephemeral Storage Considerations for Multi-Agent Systems:
Modern enterprise architectures frequently rely on serverless compute environments (such as AWS Lambda, Google Cloud Functions, or containerized Kubernetes pods) where compute instances spin up and down dynamically. CacheStation's engineering guidelines account for stateless execution environments by ensuring that prompt construction logic remains deterministic across distributed worker nodes. When multiple serverless workers simultaneously dispatch identical system prompts with `cache_control` headers enabled, CacheStation's routing protocols coordinate initial cache creation across regional endpoints to prevent redundant cache write spikes and optimize global cache read velocity.

Additional Enterprise Resilience and Disaster Recovery Protocols:CacheStation maintains redundant multi-region server clusters and automated failover pipelines to ensure continuous availability of its prompt optimization telemetry platforms, protecting client deployments against unexpected cloud infrastructure disruptions.
"""


#PROMPT CACHING
response = client.messages.create(  #client.beta.prompt_caching.messages.create(
    model=cMN,
    max_tokens=1024,
    system = [
        {
            "type":"text",
            "text":"You are an enterprise AI optimization analyst. Use the provided business_context as the authoritative company background and answer questions using only relevant information from it."
            #"text": "What toolsets and technologies does CacheStation's engineering team use for their optimization tooling?"
        },
        {
            #EXPLICIT CACHING FOR LARGER 
            "type":"text",
            "text":business_context,
            "cache_control":{
                "type":"ephemeral",
                "ttl": "1h"

            }
        }
    ],
    messages=[
        {
        "role":"user",
        #"content":"What metrics does CacheStation track, and which of those metrics would be useful for evaluating whether a prompt-caching optimization actually worked?"
        "content": "What are CacheStation's five optimization stages?"
        }
    ]
)

print(response)


#CALCULATE PRICING
def print_formatted_response(response):
    base_input_cost_per_mtok = 0.001
    cache_write_cost_per_mtok = 0.00125
    cache_read_cost_per_mtok = 0.0001
    output_cost_per_mtok = 0.005

    input_cost = (response.usage.input_tokens / 1000) * base_input_cost_per_mtok
    output_cost = (response.usage.output_tokens / 1000) * output_cost_per_mtok

    # Automatically handle Cache Write vs Cache Hit costs
    if response.usage.cache_creation_input_tokens > 0:
        cache_cost = (response.usage.cache_creation_input_tokens / 1000) * cache_write_cost_per_mtok
        cache_status = "CACHE WRITE"
        savings = 0.0
    elif response.usage.cache_read_input_tokens > 0:
        cache_cost = (response.usage.cache_read_input_tokens / 1000) * cache_read_cost_per_mtok
        cache_status = "CACHE HIT"
        # Calculate money saved compared to regular input cost
        non_caching_cost = (response.usage.cache_read_input_tokens / 1000) * base_input_cost_per_mtok
        savings = non_caching_cost - cache_cost
    else:
        cache_cost = 0.0
        cache_status = "NO CACHE USED"
        savings = 0.0

    total_cost = input_cost + output_cost + cache_cost

    print("\nResponse Content:\n" + "-"*80)
    for block in response.content:
        print(block.text)
        print("\n"+"-"*80+"\n")

    print("\nResponse Metadata : \n" + "-"*80)
    print(f"Model : {response.model}")
    print(f"Input Tokens : {response.usage.input_tokens}")
    print(f"Output Tokens : {response.usage.output_tokens}")
    print(f"Cache creation Tokens : {response.usage.cache_creation_input_tokens}")
    print(f"Cache read Tokens : {response.usage.cache_read_input_tokens}")
    print(f"Cache Status : {cache_status}")
    print(f"Total Cost : ${total_cost:.5f}")
    
    if cache_status == "CACHE HIT":
        print(f"Savings Due To Cache : ${savings:.5f}")
    else:
        print(f"Potential Savings : ${savings:.5f}")

print_formatted_response(response)