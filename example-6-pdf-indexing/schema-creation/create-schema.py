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
    "class": "Document",
    "vectorizer": "text2vec-openai",
    "properties": [
        {
            "name": "source",
            "dataType": ["text"],
        },
        {
            "name": "abstract",
            "dataType": ["text"],
            "moduleConfig": {
                "text2vec-openai": {"skip": False, "vectorizePropertyName": False}
            },
        },
    ],
    "moduleConfig": {
        "generative-openai": {},
        "text2vec-openai": {"model": "ada", "modelVersion": "002", "type": "text"},
    },
}

client.schema.create_class(schema)