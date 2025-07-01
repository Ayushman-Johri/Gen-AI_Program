from langchain_openai import ChatOpenAI
from openaikey import open_ai_key


llm = ChatOpenAI(model="gpt-4.1",api_key=open_ai_key)
question=input("My Question?")
result = llm.invoke(question)


print(result.content)
