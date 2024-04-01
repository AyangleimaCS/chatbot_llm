from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Any

from utils import load_docs, split_docs, connect_lancedb

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


@app.post("/predict", response_model = Response)
def predict() -> Any:
  
  #implement this code block
  
  return {"result": "hello world!"}


def test_func():
    directory = "C:\git_repo\chatbot_git_repo\chatbot_llm\data"
    print('directory: ', directory)
    documents = load_docs(directory)
    print("len of documents: ", len(documents))
    docs = split_docs(documents)
    print("len of documents: ", len(docs))
    # embeddings, query_result = sentence_transformer_embeddings()
    # print('embeddings:\n', embeddings)
    # print('query_result len:', len(query_result))
    connect_lancedb(docs)
    # connect_pinecone(docs, embeddings, query_result)
    # embeddings = apply_embeddings()


if __name__ == '__main__':
    test_func()