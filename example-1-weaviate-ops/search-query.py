import weaviate
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

nearText = {"concepts": ["biology"]}

result = (
    client.query
    .get("Question", ["question", "answer", "category"])
    .with_near_text(nearText)
    .with_limit(2)
    .do()
)

print(json.dumps(result, indent=4))
