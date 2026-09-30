import os 
from dotenv import load_dotenv

load_dotenv()

cMN = os.getenv("CLAUDE_MODEL_NAME")
cAK = os.getenv("CLAUDE_API_KEY")


#INSTANTIATE THE CHATANTHROPIC CLASS
from langchain_anthropic import ChatAnthropic

model = ChatAnthropic(
    model_name = cMN,
    api_key = cAK
)


#DEFINE WORKFLOW STATE
from typing import TypedDict

class VacationState(TypedDict):

    query: str

    location: str

    destination: str

    weather: str

    cuisine: str

    itinerary: str


#CREATE LOCATION PICKER AI AGENT
def location_picker(state):

    print("\n===================================")
    print("Executing Location Picker Agent")
    print("===================================\n")

    response = model.invoke(f"""
        You are a travel consultant.

        Based on the user's request, identify the most appropriate vacation region.

        User Request:

        {state["query"]}

        Return only the recommended location.
        """)

    print("Location Picker Agent Output:{}".format(response.content))
    print("===================================\n")

    return {
        "location": response.content
    }


#CREATE DESTINATION RECOMMENDER AGENT
def destination_agent(state):

    print("\n===================================")
    print("Executing Destination Agent")
    print("===================================\n")

    response = model.invoke(f"""
                                You are a travel expert.

                                Recommend the best tourist destinations in:

                                {state["location"]}
                            """)

    print("Destination Agent Output:{}".format(response.content))
    print("===================================\n")

    return {
        "destination": response.content
    }


#CREATE WEATHER AGENT
def weather_agent(state):

    print("\n===================================")
    print("Executing Weather Agent")
    print("===================================\n")

    response = model.invoke(f"""
                                You are a weather expert.

                                Describe the typical weather for:

                                {state["location"]}

                                Include the best season to visit.
                            """)

    print("Weather Agent Output:{}".format(response.content))
    print("===================================\n")

    return {
        "weather": response.content
    }


#CREATE CUISINE AGENT
def cuisine_agent(state):

    print("\n===================================")
    print("Executing Cusisine Agent")
    print("===================================\n")

    response = model.invoke(f"""
                            You are a culinary expert.

                            Recommend local cuisine for:

                            {state["location"]}
                            """)

    print("Cuisine Agent Output:{}".format(response.content))
    print("===================================\n")

    return {
        "cuisine": response.content
    }


#CREATE ITINERARY PLANNER
def itinerary_agent(state):

    print("\n===================================")
    print("Executing Itinerary Planner Agent")
    print("===================================\n")

    prompt = f"""
                Create a detailed 5-day vacation itinerary.

                Location

                {state["location"]}

                Destinations

                {state["destination"]}

                Weather

                {state["weather"]}

                Cuisine

                {state["cuisine"]}
                """

    response = model.invoke(prompt)

    print("Itinerary Planner Agent Output:{}".format(response.content))
    print("===================================\n")

    return {
        "itinerary": response.content
    }


#BUILD CUSTOM WORKFLOW
from langgraph.graph import StateGraph, START, END

builder = StateGraph(VacationState)

builder.add_node("location", location_picker)

builder.add_node("destination", destination_agent)

builder.add_node("weather", weather_agent)

builder.add_node("cuisine", cuisine_agent)

builder.add_node("itinerary", itinerary_agent)

builder.add_edge(START, "location")

# Fan-out
builder.add_edge("location", "destination")
builder.add_edge("location", "weather")
builder.add_edge("location", "cuisine")

# Fan-in
builder.add_edge("destination", "itinerary")
builder.add_edge("weather", "itinerary")
builder.add_edge("cuisine", "itinerary")

builder.add_edge("itinerary", END)

graph = builder.compile()


#GENERATE MERMAID DIAGRAM
png = graph.get_graph().draw_mermaid_png()

with open("vacation_workflow.png", "wb") as f:
    f.write(png)


#EXECUTE WORKFLOW
response = graph.invoke(
    {
        "query":
            """
            Help me plan a vacation to Gujarat.

            I enjoy historical places,adventurous 
            prefer warm weather,
            and love trying local food.
            """
    }
)

print(response["itinerary"])