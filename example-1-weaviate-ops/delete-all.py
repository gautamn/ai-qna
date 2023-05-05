import weaviate

client = weaviate.Client(
    url = "https://gautamn-sandbox-c347iuuy.weaviate.network/",  # Replace with your endpoint
    additional_headers = {
        "X-OpenAI-Api-Key": "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"  # Replace with your inference API key
    }
)

#client = weaviate.Client(
#        url = "http://localhost:8080/",  # Replace with your endpoint
#)

#client.schema.delete_class("Article") # deletes the class "Article" along with all data points of class "Article"
# OR
client.schema.delete_all() # deletes all classes along with the whole data
