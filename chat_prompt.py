from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_openai import ChatOpenAI

from openaikey import open_ai_key

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4.1",api_key=open_ai_key)
# Define prompt templates (no need for separate Runnable chains)
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a facts expert who knows facts about {animal}."),
        ("human", "Tell me {fact_count} facts."),
        ("system", "Tell me the country name where  this  {animal} found?"),
        ("human", "Tell me Asian Country?"),
    ]
)

# Create the combined chain using LangChain Expression Language (LCEL)
chain = prompt_template | model | StrOutputParser()
# chain = prompt_template | model
#print(chain)

# Run the chain
result = chain.invoke({"animal": "elephant", "fact_count": 2})

# Output
print(result)

# Run the chain
result = chain.invoke({"animal": "Tiger", "fact_count": 3})

# Output
print(result)