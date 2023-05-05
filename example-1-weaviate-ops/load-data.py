import weaviate
import requests
import json

#client = weaviate.Client(
#    url = "https://gautamn-sandbox-c347iuuy.weaviate.network/",  # Replace with your endpoint
#    additional_headers = {
#        "X-OpenAI-Api-Key": "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"  # Replace with your inference API key
#    }
#)

client = weaviate.Client(
        url = "http://localhost:8080/",  # Replace with your endpoint
)


url = 'https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny.json'
resp = requests.get(url)
data = json.loads(resp.text)

# Configure a batch process
with client.batch as batch:
    batch.batch_size=100
    for i, d in enumerate(data):
        properties = {
            "answer": d["Answer"],
            "question": d["Question"],
            "category": d["Category"],
        }

        client.batch.add_data_object(properties, "Question")
