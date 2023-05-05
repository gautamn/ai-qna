import weaviate
import json

client = weaviate.Client(
        url = "http://localhost:8080/",  # Replace with your endpoint
)

# we will create the class "Question"
class_obj = {
    "class": "Question",
    "description": "Information from a Jeopardy! question",  # description of the class
    "properties": [
        {
            "dataType": ["text"],
            "description": "The question",
            "name": "question",
        },
        {
            "dataType": ["text"],
            "description": "The answer",
            "name": "answer",
        },
        {
            "dataType": ["text"],
            "description": "The category",
            "name": "category",
        },
    ],
    "vectorizer": "text2vec-contextionary"  #text2vec-contextionary or ext2vec-openai  Or "text2vec-cohere" or "text2vec-huggingface"
}

# add the schema
client.schema.create_class(class_obj)

# get the schema
schema = client.schema.get()

# print the schema
print(json.dumps(schema, indent=4))

