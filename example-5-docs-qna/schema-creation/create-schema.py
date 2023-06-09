import weaviate
import time
from dotenv import load_dotenv
import os

load_dotenv()
openai_key = os.getenv('OPENAI_API_KEY')
weaviate_url = os.getenv('WEAVIATE_URL')

client = weaviate.Client(
    url = weaviate_url,  # Replace with your endpoint
    additional_headers = {
        "X-OpenAI-Api-Key": openai_key  # Replace with your inference API key
    }
)

schema = {
   "classes": [
       {
           "class": "PDFDocument",
           "description": "pdf documents for creating knowledge base",
           "moduleConfig": {
               "text2vec-openai": {
                    "skip": False,
                    "vectorizeClassName": True,
                    "vectorizePropertyName": False
                },
                 "generative-openai": {
                    "model": "gpt-3.5-turbo",
                    "temperatureProperty": 0.2
                }
           },
           "vectorIndexType": "hnsw",
           "vectorizer": "text2vec-openai",
           "properties": [
               {
                   "name": "content",
                   "dataType": ["text"],
                   "description": "The text content in the pdf file"
               },
               {
                   "name": "organizationId",
                   "dataType": ["text"],
                   "description": "The organization id to which the pdf file belongs to"
               }
           ]
       }
   ]
}

client.schema.create(schema)