import os 
from dotenv import load_dotenv

load_dotenv()

cMN = os.getenv("CLAUDE_MODEL_NAME")
cAK = os.getenv("CLAUDE_API_KEY")

from langchain_anthropic import ChatAnthropic
model = ChatAnthropic(
    model_name = cMN,
    api_key = cAK
)


#INVOKE MODEL
messages = [
    (
        "system",
        "You are a helpful AI Assistant have only scientific knowledge.",
    ),
    (
        "human",
        "Tell me something about Aurora Borealis",
    ),
]

ai_msg = model.invoke(messages)
#print(ai_msg.text)

#STREAM MESSAGES
stream = model.stream_events(messages, version="v3")
for token in stream.text:
    print(token, end="", flush=True)






# # Aurora Borealis (Northern Lights)

# The Aurora Borealis is a natural light display in Earth's atmosphere, primarily visible at high northern latitudes. Here are the key scientific facts:

# ## How It Forms
# - **Solar wind interaction**: Charged particles from the Sun (mainly electrons and protons) travel toward Earth
# - **Magnetic field deflection**: Earth's magnetosphere channels these particles toward the polar regions
# - **Atmospheric collision**: Particles collide with oxygen and nitrogen molecules in the upper atmosphere (100-300 km altitude)
# - **Light emission**: These collisions excite the gas molecules, causing them to release energy as visible light

# ## Characteristic Colors
# - **Green** (most common): Oxygen at lower altitudes (~100 km)
# - **Red**: Oxygen at higher altitudes
# - **Blue/Purple**: Nitrogen
# - **Magenta/Pink**: Rare, usually at lower altitudes

# ## Geographic and Temporal Patterns
# - Best visible during **geomagnetic storms** (when solar activity increases)
# - Most frequent occurrence during the **equinoxes** (March and September)
# - Visible from high northern latitudes: Scandinavia, Alaska, Canada, northern Russia
# - A southern hemisphere equivalent (Aurora Australis) occurs over Antarctica and southern Australia

# ## Frequency
# Aurora activity follows **11-year solar cycles**, with more frequent displays during solar maximum periods.