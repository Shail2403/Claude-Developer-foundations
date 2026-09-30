import os 
from dotenv import load_dotenv

load_dotenv()

cMN = os.getenv("CLAUDE_MODEL_NAME")
cAK = os.getenv("CLAUDE_API_KEY")

import anthropic    

client = anthropic.Anthropic(api_key=cAK)


user_prompt = """
                Extract the following customer inquiry into structured JSON.

                Customer Name: Sarah Johnson
                Email: sarah.johnson@contoso.com

                Company: Contoso Electronics

                The customer is interested in our Premium Digital Marketing Package.

                She would like to schedule a consultation next Wednesday and has requested additional pricing information.
            """

#GENERATE STRUCTURED OUTPUT USING RAW JSON SCHEMA CONFIGURATION
message = client.messages.create(
    model=cMN,
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": user_prompt
        }
    ],
    output_config={
        "format": {
            "type": "json_schema",
            "schema": {
                "type": "object",
                "properties": {
                    "customer_name": {
                        "type": "string"
                    },
                    "email": {
                        "type": "string"
                    },
                    "company": {
                        "type": "string"
                    },
                    "service_requested": {
                        "type": "string"
                    },
                    "consultation_requested": {
                        "type": "boolean"
                    },
                    "pricing_information_requested": {
                        "type": "boolean"
                    }
                },
                "required": [
                    "customer_name",
                    "email",
                    "company",
                    "service_requested",
                    "consultation_requested",
                    "pricing_information_requested"
                ],
                "additionalProperties": False
            }
        }
    }
)

for block in message.content:
    if block.type == "text":
        print(block.text)



#USE PYDANTIC MODELS TO GENERATE STRUCTURED OUTPUT
from pydantic import BaseModel 

class CustomerLead(BaseModel):
    customer_name: str
    email: str
    company: str
    service_requested: str
    consultation_requested: bool
    pricing_information_requested: bool

response = client.messages.parse(
    model=cMN,
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": user_prompt
        }
    ],
    output_format = CustomerLead
)

contact = response.parsed_output
print("customer name: ", contact.customer_name)
print("email: ", contact.email)
print("company: ", contact.company)
print("service requested: ", contact.service_requested)
print("consultation requested: ", contact.consultation_requested)
print("pricing information requested: ", contact.pricing_information_requested)