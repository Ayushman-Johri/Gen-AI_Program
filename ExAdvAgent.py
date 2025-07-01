from langchain_experimental.tools.python.tool import PythonREPLTool
from langchain.agents import Tool, AgentExecutor, create_react_agent
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
 
from openaikey import open_ai_key
 
 
# 2. Define an LLM and a prompt
llm = OpenAI(api_key=open_ai_key)
template = """Answer the following questions as best you can. 
You have access to the following tools:
{tools}
Use the following format:
Question: the input question you must answer
Thought: what you should do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question
Begin!
Question: {input}
{agent_scratchpad}"""
prompt = PromptTemplate(
    input_variables=["input", "tools", "tool_names", "agent_scratchpad"],
    template=template,
)
# Step 3: Define the tool
python_tool = PythonREPLTool()
tools = [
    Tool(
        name="Sandeep's Calculator",
        func=python_tool.run,
        description="Useful for doing math or running Python code"
    )]
# Step 4: Create the agent using the prompt
agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)
# Step 5: Create the executor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
# Step 6: Use the agent
'''
response = agent_executor.invoke({"input": "What is 25 multiplied by 4 plus the square root of 81?"})
print(response["output"])
'''
response = agent_executor.invoke({"input": "Show the sum of array [55,66,77,88,99]"})
print(response["output"])
