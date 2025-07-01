from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda, RunnableSequence
from langchain_openai import ChatOpenAI
 
from openaikey import open_ai_key
 
 
# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4.1",api_key=open_ai_key)
# Define prompt templates
prompt_template = ChatPromptTemplate.from_messages(
     [
        ("system", "You love facts and you tell facts about {animal}"),
        ("human", "Tell me {count} facts."),
    ])
# Create individual runnables (steps in the chain)
format_prompt = RunnableLambda(lambda x: prompt_template.format_prompt(**x))
invoke_model = RunnableLambda(lambda x: model.invoke(x.to_messages()))
parse_output = RunnableLambda(lambda x: x.content)
# Create the RunnableSequence (equivalent to the LCEL chain)
#LangChain Expression Language
chain = RunnableSequence(first=format_prompt, middle=[invoke_model], last=parse_output)
print(chain)
# Run the chain
response = chain.invoke({"animal": "cat", "count": 2})
# Output
print(response)