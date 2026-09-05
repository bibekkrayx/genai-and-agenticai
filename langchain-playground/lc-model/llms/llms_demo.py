import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAI

load_dotenv()

model = OpenAI(model=os.getenv("OPENAI_CHAT_MODEL"))

response = model.invoke("what is the fastest animal")

print(response)