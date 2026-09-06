import os

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embeddings = OpenAIEmbeddings(
    model=os.getenv("OPENAI_EMBEDDING_MODEL"),
    dimensions=3
)

text = "ray"

vector = embeddings.embed_query(text)

print(vector)
print("vector len: ", len(vector))
print("-"*20)

text2 = ["hi my name is bibek"]
text3 = "hi my name is bibek and i am software, ai and devOps engineer"

vector2 = embeddings.embed_documents(text2)
vector3 = embeddings.embed_documents(text3)

print(vector2)
print("vector len: ", len(vector2))
print("-"*20)
print(vector3)
print("vector len: ", len(vector3))
print("-"*20)
