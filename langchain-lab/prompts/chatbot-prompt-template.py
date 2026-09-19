from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate(
    [
        ("system", "You are a helpful DSA AI bot. Your name is {name}"),
        ("human", "Explain {topic}")
    ]
)

prompt = template.invoke(
    {
        "name": "ray",
        "topic": "array"
    }
)

print(prompt)