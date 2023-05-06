from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI


def readPdfFile():
    pdfFileObj = open('../docs/nfts.pdf', 'rb')
    pdf_reader = PdfReader(pdfFileObj)
    text = ""
    for page in pdf_reader.pages:
      text += page.extract_text()

    # closing the pdf file object
    pdfFileObj.close()
    return text

def indexPdf(text):
  # split into chunks
    text_splitter = CharacterTextSplitter(
      separator="\n",
      chunk_size=1000,
      chunk_overlap=200,
      length_function=len
    )
    chunks = text_splitter.split_text(text)
    
    # create embeddings
    embeddings = OpenAIEmbeddings()
    

    retunr embeddings
    

#insert the documents in weaviate
def addDataInWeaviate(df):
    client.batch.configure(batch_size=10)
    with client.batch as batch:
        for index, row in df.iterrows():
            text = row['content']
            ebd = row['embedding']
            batch_data = {
                "content": text
            }
            batch.add_data_object(data_object=batch_data, class_name="NFTs", vector=ebd)

    print("Data Added!")


def main():
    load_dotenv()
    text = readPdfFile()
    print(text)
    
 
if __name__ == '__main__':
    main()
