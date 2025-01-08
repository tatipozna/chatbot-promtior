from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import WebBaseLoader
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
import os
import fitz
from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles

os.environ["OPENAI_API_KEY"] = "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"

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

def load_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text("text") 
    return text

pdf_text = load_pdf("pdf/promtior.pdf")

loader = WebBaseLoader(["https://promtior.ai/"])
docs = loader.load()

combined_texts = [pdf_text] + [doc.page_content for doc in docs]

embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_texts(combined_texts, embeddings)

llm = ChatOpenAI(model_name="gpt-4")

retriever = vectorstore.as_retriever()
answer_bot = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

@app.get("/")
def get_index():
    return FileResponse("index.html")

@app.get("/chat")
def chat(query: str):
    response = answer_bot.run(query)

    if not response or response.strip() == "The information provided doesn't include":
        response = "No se encontró información relevante."

    return JSONResponse(content={"respuesta": response})
