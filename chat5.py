#from langchain_openai import OpenAI
from openai import OpenAI
import base64
import os
from openaikey import open_ai_key
os.environ['OPEN_AI_KEY']=open_ai_key
OpenAI_key = os.environ.get("OPEN_AI_KEY")
prompt="Create an AI character image of student with transparent background like pixabay"
client=OpenAI(api_key=OpenAI_key)

result = client.images.generate(
    model="gpt-image-1",
    prompt=prompt,
   
    quality='medium',
    n=1
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

# Save the image to a file
with open("std.png", "wb") as f:
    f.write(image_bytes)