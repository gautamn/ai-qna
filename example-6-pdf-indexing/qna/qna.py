from langchain.vectorstores.weaviate import Weaviate
from langchain.llms import OpenAI
from langchain.chains import ChatVectorDBChain
import weaviate
from dotenv import load_dotenv
import os
import openai
import textwrap

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
weaviate_url = os.getenv('WEAVIATE_URL')

client = weaviate.Client(
      url = weaviate_url,  # Replace with your endpoint
      additional_headers = {
        "X-OpenAI-Api-Key": openai.api_key  # Replace with your inference API key
      }
)

result = client.query.get("Document", "source").with_bm25(
    query="some paper about housing prices"
).with_additional("score").do()
print(result)

results = client.query.get("Document", "abstract").with_where({
    "path": "source",
    "operator": "Equal",
    "valueText": "paper02.pdf"
}).do()
print(results)


prompt = """
Please summarize the following academic abstract in a one-liner for a layperson:

{abstract}
"""

results = (
   client.query.get("Document", "source").with_generate(single_prompt=prompt).do()
)
print(results)


#docs = results["data"]["Get"]["Document"]


#for doc in docs:
#    source = doc["source"]
#    abstract = doc["_additional"]["generate"]["singleResult"]
#    wrapped_abstract = textwrap.fill(abstract, width=80)
#    print(f"Source: {source}\nSummary:\n{wrapped_abstract}\n")



