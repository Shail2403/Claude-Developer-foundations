import os
from dotenv import load_dotenv
load_dotenv()

oAK = os.getenv("OPENAI_API_KEY")
cMN = os.getenv("CLAUDE_MODEL_NAME")
cAK = os.getenv("CLAUDE_API_KEY")

QDRANT_URL = "http://localhost:6333"
COLLECTION_NAME = "NTrips"

import anthropic
anthropic_client=anthropic.Anthropic(api_key=cAK)

from openai import OpenAI
openai_client=OpenAI(api_key=oAK)



#CREATE VECTOR EMBEDDING GENERATOR FUCNTION
def generate_vector_embeddings(user_query):
    response=openai_client.embeddings.create(
        model="text-embedding-3-small",
        input=user_query
    )
    return response.data[0].embedding

#CREATE CONTEXT RETRIEVAL FUNCTION
from qdrant_client import QdrantClient
from qdrant_client.models import Distance,VectorParams,PointStruct

def context_retrieval(user_query):

    #Generate Vector Embeddings for User Query
    user_embeddings=generate_vector_embeddings(user_query)

    #Initialize Qdrant Client
    qdrant_client=QdrantClient(url=QDRANT_URL)

    #Throwing a request to QDrantDB to retrieve top matched content 
    search_result=qdrant_client.query_points(
        collection_name="NTrips",
        query=user_embeddings,
        with_vectors=True,
        with_payload=True,
        limit=2
    ).points

    #Retrieving the top text content that cna be used to answer query
    supporting_text_content = search_result[0].payload.get("content")

    return supporting_text_content


#Summarize with Claude Messages API
#user_query="""Where is Polo Forest mentioned by Nirav? and what is price?  """
user_query="""Who is operating Tour?"""
context=context_retrieval(user_query)

with anthropic_client.messages.stream(
    model=cMN,
    system="You are a helpful RAG Assistant Chatbot.",
    messages=[
        {
            "role":"user",
            "content":f"""answer the user query using provided supporting knowledge \n
                                        user_query: {user_query} \n
                                        supporting_text: {context}""",
        }
    ],
    max_tokens=1000
) as stream:
    for text in stream.text_stream:
        print(text,end="",flush=True)