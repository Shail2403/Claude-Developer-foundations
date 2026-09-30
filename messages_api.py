import os 
from dotenv import load_dotenv

load_dotenv()

cMN = os.getenv("CLAUDE_MODEL_NAME")
cAK = os.getenv("CLAUDE_API_KEY")

import anthropic    

client = anthropic.Anthropic(api_key=cAK)

#USING CLAUDE MESSAGE APIS
# message = client.messages.create(
#     model=cMN,
#     system="You are Peter Parker, a superhero and Protector of New York City.",
#     messages=[
#         {
#             "role":"user",
#             "content":"What MJ doing today? tell in summarized max 180 around words"
#         }
#     ],
#     max_tokens=70
# )

# for block in message.content:
#     if block.type == "text":
#         print(block.text)


#STREAM MESSAGES
# with client.messages.stream(
#     model=cMN,
#     system="You are Peter Parker, a superhero and Protector of New York City.",
#     messages=[
#         {
#             "role":"user",
#             "content":"What MJ doing today? tell in summarized max 180 around words",
#         }
#     ],
#     max_tokens=130
# ) as stream:
#     for text in stream.text_stream:
#         print(text,end="",flush=True) #flush write data immediately to display from buffer or ram


#PASS ASSISTANT RESPONSE TO NEXT PROMPT
# with client.messages.stream(
#     model=cMN,
#     system="You are legendary Vibe code Debug Engineer.",
#     messages=[
#         {
#             "role":"user",
#             "content":"Hi I'm junior developer.I'm doing vibe coding in company development. You have to teach me how to debug big vibe coded codebases!"
#         },
#         {
#             "role": "assistant",
#             "content": "Hey dev, don't worry. Debugging a large vibe-coded codebase is less about reading every line and more about systematically narrowing down where the problem is."
#         },
#         {
#             "role": "user",
#             "content": "Okay, but when I get a bug in a large codebase, I don't know where to start. What should I do first?"
#         },
#         {
#             "role":"assistant",
#             "content": """
#             # Great question! Here's the systematic approach I recommend:
#                 ## 1. **Reproduce the Bug First**
#                 - Get consistent steps to trigger it
#                 - Note the exact error message, stack trace, or unexpected behavior
#                 - Know: does it happen always? Sometimes? Under specific conditions?

#                 ## 2. **Read the Error Message Carefully**
#                 - Stack traces are your best friend
#                 - Look at the **top of the stack** - that's usually closest to the actual problem
#                 - Check file names and line numbers

#                 ## 3. **Narrow Down the Scope**
#                 Don't try to understand the whole codebase! Instead:
#                 - **Isolate the feature**: Which module/feature is broken?
#                 - **Trace the data flow**: Follow how data moves through that feature
#                 - **Find the boundary**: Where does it break? Input? Processing? Output?

#                 ## 4. **Use Strategic Debugging Techniques**#
#                 """
#         },
#         {
#             "role":"user",
#             "content":"continue it from where left above..."
#         }
#     ],
#     max_tokens=180
# ) as stream:
#     for text in stream.text_stream:
#         print(text,end="",flush=True)


#PASS IMAGES IN API CALLS 
# image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSv9YeK7lInSELAjaDNdtIDWnRfYBT9UWPELrA2d2mVDQ&s=10"

# with client.messages.stream(
#     model=cMN,
#     system="You are Deep Humour Memer and also 10 year experienced AI Developer.",
#     messages=[
#         {
#             "role":"user",
#             "content":[
#                 {
#                     "type":"image",
#                     "source":{
#                         "type":"url",
#                         "url":image_url
#                     }
#                 },
#                 {
#                     "type":"text",
#                     "text":"Tell me more about story behind this image in short"
#                 }
#             ]
#         }
#     ],
#     max_tokens=220
# ) as stream:
#     for text in stream.text_stream:
#         print(text,end="",flush=True)


#PASS ENCODED IMAGES 
# import base64
# import httpx
# image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSv9YeK7lInSELAjaDNdtIDWnRfYBT9UWPELrA2d2mVDQ&s=10"
# image_media_type="image/jpeg"
# image_data=base64.standard_b64encode(httpx.get(image_url).content).decode("utf-8")

# with client.messages.stream(
#     model=cMN,
#     system="You are Deep Humour Memer and also 10 year experienced AI Developer.",
#     messages=[
#         {
#             "role":"user",
#             "content":[
#                 {
#                     "type":"image",
#                     "source":{
#                         "type":"base64",
#                         "media_type":image_media_type,
#                         "data":image_data
#                     }
#                 },
#                 {
#                     "type":"text",
#                     "text":"Tell me more about story behind this image in short"
#                 }
#             ]
#         }
#     ],
#     max_tokens=220
# ) as stream:
#     for text in stream.text_stream:
#         print(text,end="",flush=True)