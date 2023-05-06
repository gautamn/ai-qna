from langchain.vectorstores.weaviate import Weaviate
from langchain.llms import OpenAI
from langchain.chains import ChatVectorDBChain
import weaviate
from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
weaviate_url = os.getenv('WEAVIATE_URL')

client = weaviate.Client(
      url = weaviate_url,  # Replace with your endpoint
      additional_headers = {
        "X-OpenAI-Api-Key": openai.api_key  # Replace with your inference API key
      }
)

vectorstore = Weaviate(client, "PDFDocument", "content")
MyOpenAI = OpenAI(temperature=0.2, openai_api_key=openai.api_key)
qa = ChatVectorDBChain.from_llm(MyOpenAI, vectorstore)
chat_history = []
print("Welcome to the Weaviate ChatVectorDBChain Demo!")
print("Please enter a question or dialogue to get started!")

while True:
    query = input("")
    result = qa({"question": query, "chat_history": chat_history})
    print(result["answer"])
    chat_history = [(query, result["answer"])]