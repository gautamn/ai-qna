import openai
from openai.embeddings_utils import get_embedding
import weaviate

openai.api_key = "sk-fY1nlGsAe34cCVpsMaT3sNBlbkFJGwhn9xGM3r9zcok9Uewn"

client = weaviate.Client(
    url = "https://gautamn-sandbox-347iuucy.weaviate.network/",  # Replace with your endpoint
    additional_headers = {
        "X-OpenAI-Api-Key": "sk-GsAe34cCVpsMaT3BlbkFJGwhn9xsNfY1nlGM3r9zcok9Uewn"  # Replace with your inference API key
    }
)

def query(input_text, k):
    input_embedding = get_embedding(input_text, engine="text-embedding-ada-002")
    vec = {"vector": input_embedding}
    result = client \
        .query.get("HistoryText", ["content", "_additional {certainty}"]) \
        .with_near_vector(vec) \
        .with_limit(k) \
        .do()

    output = []
    closest_paragraphs = result.get('data').get('Get').get('HistoryText')
    for p in closest_paragraphs:
        output.append(p.get('content'))

    return output
    

if __name__ == "__main__":
 
    input_text = "world war"
    k_vectors = 3

    result = query(input_text, k_vectors)
    for text in result:
        print(text)
