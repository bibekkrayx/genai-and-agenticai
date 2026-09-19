from dotenv import load_dotenv

load_dotenv()
from langchain_core.messages import HumanMessage

from langchain_openai import ChatOpenAI
from langchain.messages import SystemMessage, AIMessage

model = ChatOpenAI()

chat_history = [SystemMessage("Your are principle SDE and system design tutor")]

while True:
    user_input = input("USER: ")
    chat_history.append(HumanMessage(user_input))
    if user_input == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(result.content))
    print(f"AI: {result.content}")
