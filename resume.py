from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI  # or any other LLM
from openaikey import open_ai_key
# Load the resume PDF
loader = PyPDFLoader("resume.pdf")
docs = loader.load()

# Split text (optional but useful for large resumes)
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
splits = splitter.split_documents(docs)

# Define the prompt for extracting information
prompt = PromptTemplate.from_template("""
You are a resume parser. Extract the following details from the given text:
- Full Name
- Email
- Phone Number
- Skills
- Work Experience
- Education

Resume Text:
{text}

Return the result in JSON format.
""")

# Load the LLM
llm = ChatOpenAI(api_key=open_ai_key, model="gpt-4", temperature=0)

# Chain the steps together
chain = prompt | llm | StrOutputParser()

# Run on each split (or just the first one if resume is short)
response = chain.invoke({"text": splits[0].page_content})

print(response)
