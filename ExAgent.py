from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain_experimental.tools.python.tool import PythonREPLTool
from langchain_openai import OpenAI
#pip install langchain_experimental 
from openaikey import open_ai_key
 
 
llm = OpenAI(api_key=open_ai_key)
#  Define tools the agent can use The Python REPL tool (Read-Eval-Print Loop)
tools = [
    Tool(
        name="Calculator",
        func=PythonREPLTool().run,
        description="Useful for when you need to do math calculations"
    )]
#  Create the Agent
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False)
#  Ask a question that requires calculation
result = agent.run("What is 15% of 240?")
print("Answer:", result)
