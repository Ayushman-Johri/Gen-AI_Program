from langchain_core.runnables import RunnableLambda
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
 
from openaikey import open_ai_key
 
 
# 1. Define your custom Python logic using RunnableLambda
question = RunnableLambda(lambda x: {"text": int(x["text"])+2})

# 2. Define an LLM and a prompt
llm = OpenAI(api_key=open_ai_key)
prompt = PromptTemplate.from_template("square root of {text}")

# 3. Create a chain using LCEL (using the pipe `|` syntax)
# try without question
chain = question | prompt | llm

# 4. Run the chain
output = chain.invoke({"text": "47"})
print(output)