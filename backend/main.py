import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Any

from utils import load_docs, split_docs, connect_lancedb, get_answer

# Load environment variables from .env file (if any)
load_dotenv()

class Response(BaseModel):
    result: str | None

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000"
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_key = os.getenv("OPENAI_API_KEY")
directory = os.getenv("PATH_TO_KNOWLEDGE_BASE")

@app.post("/predict", response_model = Response)
def predict() -> Any:
  
  #implement this code block
  
  return {"result": "hello world!"}


def test_func(query):
    documents = load_docs(directory)
    print("Number of documents available in the knowledge base: ", len(documents))
    docs = split_docs(documents)
    print("Number of docs after Recursive Splitting: ", len(docs))
    docsearch = connect_lancedb(docs, api_key)
    answer = get_answer(query, docsearch, api_key)
    print('answer: ', answer)
    return answer

if __name__ == '__main__':
    inp_query = input(str("Enter your query: "))
    print("input query: ", inp_query)
    answer = test_func(inp_query)