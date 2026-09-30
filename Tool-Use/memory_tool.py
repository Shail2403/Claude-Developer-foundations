import os
from dotenv import load_dotenv
load_dotenv()

cMN = os.getenv("CLAUDE_MODEL_NAME")
cAK = os.getenv("CLAUDE_API_KEY")

import anthropic
client = anthropic.Anthropic(api_key=cAK)

from anthropic.tools import BetaLocalFilesystemMemoryTool
memory = BetaLocalFilesystemMemoryTool(
    base_path="./memory"
)

#LOAD THE FIRST CONVERSATION
runner=client.beta.messages.tool_runner(
    model=cMN,
    max_tokens=1100,
    tools=[memory],
    messages=[
        {
            "role":"user",
            # "content":"""
            #             Remember the following information.
            #             My name is Jarvish . I am 21 years old and a Claude Developer.
                        
            #             My company is CarbonOps.
            #             Our new AI Product is AGai - an AI Powered ESG Audit and Reporting Tool for BRSR, GRI, ESRS, SDGs etc.

            #             Whenever you write LinkedIn posts,
            #             use a professional and educational tone.

            #             My preferred audience is sustainability consultants.
            #             """
            "content":"I loves to watch Galaxy."
        }
    ]
)

response = runner.until_done()

print("==>",response,"<==")

for block in response.content:
    if block.type=="text":
        print(block.text)










#==> ParsedBetaMessage[TypeVar](id='msg_011CfLShyKJ3wg4uD45zWrhq', container=None, content=[ParsedBetaTextBlock[TypeVar](citations=None, text="Great! I have information about you in my memory. Here's something about you:\n\n**Jarvish** is a 21-year-old Claude Developer at CarbonOps. You work on **AGai**, an AI-powered ESG (Environmental, Social, and Governance) audit and reporting tool that supports multiple sustainability frameworks including BRSR, GRI, ESRS, and the Sustainable Development Goals (SDGs). \n\nYou create professional and educational content aimed at sustainability consultants, typically shared on platforms like LinkedIn. Your work focuses on helping organizations measure and report their environmental and social impact more effectively through AI-powered tools.\n\nIs there anything specific about your work or background you'd like to discuss or update?", type='text', parsed_output=None)], context_management=None, diagnostics=None, model='claude-haiku-4-5-20251001', role='assistant', stop_details=None, stop_reason='end_turn', stop_sequence=None, type='message', usage=BetaUsage(cache_creation=BetaCacheCreation(ephemeral_1h_input_tokens=0, ephemeral_5m_input_tokens=0), cache_creation_input_tokens=0, cache_read_input_tokens=0, fallback_credit=None, inference_geo='not_available', input_tokens=2002, iterations=None, output_tokens=158, output_tokens_details=None, server_tool_use=None, service_tier='standard', speed=None), input_transformations=None) <==