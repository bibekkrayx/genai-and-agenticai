import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()
print(os.getenv("HUGGINGFACEHUB_API_TOKEN"))

model = init_chat_model(
    "microsoft/Phi-3-mini-4k-instruct",
    model_provider="huggingface",
    temperature=0.7,
    max_tokens=1024,
    api_key=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)


response = model.invoke("Why do parrots talk?")

print(f"Hugging face response: {response.content}")