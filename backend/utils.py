
from langchain_community.vectorstores.lancedb import LanceDB
from langchain.embeddings.openai import OpenAIEmbeddings

from langchain_community.document_loaders.directory import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain_community.llms import OpenAI


def load_docs(directory):
    print("Loading documents...")
    loader = DirectoryLoader(directory)
    docs = loader.load()
    print("Loaded documents from directory")
    return docs


def split_docs(documents, chunk_size=1000, chunk_overlap=20):
    print("Splitting documents...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = text_splitter.split_documents(documents)
    print("Successfully completed documents split into chunks")
    return docs


def connect_lancedb(docs, api_key):
    print("Connecting to LanceDB...")
    embeddings = OpenAIEmbeddings(api_key=api_key)
    docsearch = LanceDB.from_documents(docs, embeddings)
    print("Connected to LanceDB")
    return docsearch


def get_answer(query, docsearch, api_key):
    print("Getting answer from our knowledge base by using the model gpt-3.5-turbo")
    similar_docs = docsearch.similarity_search(query)
    print('len similar_docs: ', len(similar_docs))
    model_name = "gpt-3.5-turbo"
    llm = OpenAI(api_key=api_key, model_name=model_name)
    chain = load_qa_chain(llm, chain_type="stuff")
    answer = chain.run(input_documents=similar_docs, question=query)
    return answer
