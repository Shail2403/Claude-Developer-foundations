import os
from dotenv import load_dotenv
load_dotenv()

oAK = os.getenv("OPENAI_API_KEY")


from openai import OpenAI

client = OpenAI(
    api_key=oAK
)

#PREPARE THE DATASET
from pathlib import Path
from pypdf import PdfReader
import json

# pre_vector_data = []

# data_dir = Path(__file__).parent / "data"

# for file in data_dir.glob("*.pdf"):
#     reader=PdfReader(file)
#     content=""
#     for page in reader.pages:
#         content+=(page.extract_text() or "") + "\n"
#     pre_vector_data.append(
#         {
#             "title":file.stem,
#             "content":content.strip()
#         }
#     )

#WRITE TO JSON
#with open("data.json","w",encoding="utf-8") as f:
#     json.dump(pre_vector_data,f,indent=4,ensure_ascii=False)

# print(f"Saved {len(pre_vector_data)} documents to data.json")


#VECTORISE THE DATA
# with open("data.json","r",encoding="utf-8") as f:
#     documents=json.load(f)

# for document in documents:

#     response = client.embeddings.create(
#         model="text-embedding-3-small",
#         input=document["content"]
#     )
#     document["vector"]=response.data[0].embedding

# with open("data.json","w",encoding="utf-8") as f:
#     json.dump(documents,f,indent=4,ensure_ascii=False)

# print(f"Generated embeddings for {len(documents)} documents.")


#UPDLOAD VECTORS TO QDRANT DB 
from qdrant_client import QdrantClient
from qdrant_client.models import Distance,VectorParams,PointStruct

QDRANT_URL = "http://localhost:6333"
COLLECTION_NAME = "NTrips"

qdrant_client=QdrantClient(url=QDRANT_URL)

if not qdrant_client.collection_exists(COLLECTION_NAME):
        qdrant_client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=1536,distance=Distance.DOT)
        )
        print(f"Collection '{COLLECTION_NAME}' created.")

        # Load vectors from file 
        with open("data.json","r") as f:
                data=json.load(f)

        points=[
                PointStruct(
                        id=i+1,
                        vector=entry["vector"],
                        payload={"content":entry["content"]}
                ) for i,entry in enumerate(data)
        ]

        qdrant_client.upsert(
                collection_name=COLLECTION_NAME,
                wait=True,
                points=points
        )
        print(f"Upserted {len(points)} vectors.")

else:
        print(f"Collection {COLLECTION_NAME} already exists.")


