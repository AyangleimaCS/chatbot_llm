import os

import lancedb
from langchain_community.vectorstores.lancedb import LanceDB
from langchain_openai import OpenAIEmbeddings

from langchain_community.document_loaders.directory import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_docs(directory):
    loader = DirectoryLoader(directory)
    print('loader: ', loader)
    docs = loader.load()
    return docs


def split_docs(documents, chunk_size=1000, chunk_overlap=20):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = text_splitter.split_documents(documents)
    return docs


# def sentence_transformer_embeddings():
#     embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
#     query_result = embeddings.embed_query("Hello World")
#     print('len query result: ', len(query_result))
#     return embeddings, query_result


def connect_lancedb(docs):
    embeddings = OpenAIEmbeddings(api_key="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")
    docsearch = LanceDB.from_documents(docs, embeddings)
    query = "Tell me about Taj Mahal"
    similar_docs = docsearch.similarity_search(query)
    print(similar_docs[0].page_content)
    print('lancedb docs:\n', len(similar_docs))

