import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

model = init_chat_model(
    os.getenv("OPENAI_CHAT_MODEL"),
    temperature = 0
)

response = model.invoke("Give me a cute, lighthearted one-liner to flirt with a friend.")

print(response.content)