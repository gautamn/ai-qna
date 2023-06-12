from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from openai.embeddings_utils import get_embedding
import weaviate
import os
import openai




def readPdfFile():
    pdfFileObj = open('../docs/nfts.pdf', 'rb')
    pdf_reader = PdfReader(pdfFileObj)
    text = ""
    for page in pdf_reader.pages:
      text += page.extract_text()

    # closing the pdf file object
    pdfFileObj.close()
    return text

def createCorpusOfChunks(text):
  corpus = []
  # split into chunks
  text_splitter = CharacterTextSplitter(
      separator="\n",
      chunk_size=1000,
      chunk_overlap=200,
      length_function=len
    )
  chunks = text_splitter.split_text(text)
  for i in chunks:
    newObj = {'content' : i}
    corpus.append(newObj)
  return corpus

#insert the documents in weaviate
def addDataInWeaviate(corpus, openai_key, weaviate_url):
    
    client = weaviate.Client(
      url = weaviate_url,  # Replace with your endpoint
      additional_headers = {
        "X-OpenAI-Api-Key": openai_key  # Replace with your inference API key
      }
    )
    client.batch.configure(batch_size=10)
    with client.batch as batch:
        for item in corpus:
            text = item
            #print(text)
            print(text['content'])
            str = text['content'].replace("\n", " ")
            print("**********************************************************************************************************")
            ebd = generate_data_embeddings(str)
            batch_data = {
                "content": str,
                "organizationId" : "andor"
            }
            batch.add_data_object(data_object=batch_data, class_name="PDFDocument", vector=ebd)

    print("Data Added!")

def generate_data_embeddings(item):
  embedding = openai.Embedding.create(
  input=item, model="text-embedding-ada-002")["data"][0]["embedding"]
  len(embedding)
  return embedding

def main():
    load_dotenv()
    openai.api_key = os.getenv('OPENAI_API_KEY')
    weaviate_url = os.getenv('WEAVIATE_URL')
    text = readPdfFile()
    #print(text)
    corpus = createCorpusOfChunks(text)
    print(len(corpus))
    addDataInWeaviate(corpus, openai.api_key, weaviate_url)
    
 
if __name__ == '__main__':
    main()
