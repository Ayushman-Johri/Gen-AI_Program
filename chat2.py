from openai import OpenAI
import os
from openaikey import open_ai_key
os.environ['OPEN_AI_KEY']=open_ai_key
OpenAI_key = os.environ.get("OPEN_AI_KEY")

llm = OpenAI(api_key=OpenAI_key)

response = llm.responses.create(
    model="gpt-4.1",
    input="Square root of 49?"
)

print(response.output_text)