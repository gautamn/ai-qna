from dotenv import load_dotenv
import streamlit as st
import weaviate
from langchain.vectorstores.weaviate import Weaviate
import os
import openai
from langchain.llms import OpenAI
from langchain.chains import ChatVectorDBChain


def main():
    load_dotenv()
    openai.api_key = os.getenv('OPENAI_API_KEY')
    weaviate_url = os.getenv('WEAVIATE_URL')
    st.set_page_config(page_title="Ask your PDF")
    st.header("Ask your PDF 💬")

    client = weaviate.Client(
      url = weaviate_url,  # Replace with your endpoint
      additional_headers = {
        "X-OpenAI-Api-Key": openai.api_key  # Replace with your inference API key
      }
    )

    vectorstore = Weaviate(client, "PDFDocument", "content")
    MyOpenAI = OpenAI(temperature=0.2, openai_api_key=openai.api_key)
    qa = ChatVectorDBChain.from_llm(MyOpenAI, vectorstore)
    chat_history = []
    
    # show user input
    user_question = st.text_input("Ask a question about your PDF:")
    if user_question:
        result = qa({"question": user_question, "chat_history": chat_history})
        print(result["answer"])
        chat_history = [(user_question, result["answer"])]
        
        st.write(result["answer"])
    

if __name__ == '__main__':
    main()
