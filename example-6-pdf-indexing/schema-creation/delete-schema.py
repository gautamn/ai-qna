import weaviate
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

#client.schema.delete_class("PDFDocument") # deletes the class "PDFDocument" along with all data points of class "PDFDocument"
# OR
client.schema.delete_all() # deletes all classes along with the whole data
