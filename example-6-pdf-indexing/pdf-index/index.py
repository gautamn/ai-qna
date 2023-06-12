from dotenv import load_dotenv
from pathlib import Path
import weaviate
import os
from unstructured.partition.pdf import partition_pdf
import openai
import textwrap
from AbstractExtractor import AbstractExtractor


def main():
    load_dotenv()
    openai.api_key = os.getenv('OPENAI_API_KEY')
    weaviate_url = os.getenv('WEAVIATE_URL')
    client = weaviate.Client(
      url = weaviate_url,  # Replace with your endpoint
      additional_headers = {
        "X-OpenAI-Api-Key": openai.api_key  # Replace with your inference API key
      }
    )
    data_folder = "../data/nfts/"
    data_objects = []

    for path in Path(data_folder).iterdir():
        if path.suffix != ".pdf":
            continue
        print(f"Processing {path.name}...")
        elements = partition_pdf(filename=path)
        #for elem in elements[:10]:
        #    print(elem)
        # titles = [elem for elem in elements if elem.category == "Title"]
        #for title in titles:
        #    print("title=="+title.text)
        
        narrative_texts = [elem for elem in elements if elem.category == "NarrativeText"]

        for index, elem in enumerate(narrative_texts[:5]):
            print(f"Narrative text == {index + 1}:")
            print("\n".join(textwrap.wrap(elem.text, width=100)))
            print("\n" + "-" * 100 + "\n")
            
        #abstract_extractor = AbstractExtractor()
        #abstract_extractor.consume_elements(elements)
        #data_object = {"source": path.name, "abstract": abstract_extractor.abstract()}
        #data_objects.append(data_object)

        #with client.batch as batch:
        #   for data_object in data_objects:
        #       batch.add_data_object(data_object, "Document")

    #client.data_object.get(class_name="Document")['totalResults']           

if __name__ == '__main__':
    main()