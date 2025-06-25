from langchain_community.llms.ollama import Ollama
from langchain_community.vectorstores import FAISS
from langchain_community.llms import ollama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate


from llm_memory import get_embedding_model
import os

# loading the embedding model
embedding_model = get_embedding_model()

# loading FAISS vector store
DB_FAISS_PATH = "vectorstore/db_faiss"
data = FAISS.load_local(DB_FAISS_PATH, embeddings=embedding_model,
                        allow_dangerous_deserialization=True)

#initialize ollama with llama3
llm = Ollama(model="llama3")

# custom prompt template
custom_prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
Use the pieces of information provided in the context to answer the user's question.
If you don't know the answer, just say that you don't. Don't try to make up an answer.
Do not provide anything outside the given context.

Context: {context}
Question: {question}

Start the answer directly. No small talk please.
    """
)

# create RetrievalQA with custom prompt
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=data.as_retriever(),
    chain_type_kwargs={"prompt": custom_prompt},
    return_source_documents=True
)

# function to ask user question
def ask_question(query):
    result = qa_chain({"query": query})
    print("\nAnswer: ")
    print(result['result'])

    print("\nSources: ")
    for doc in result['source_documents']:
        print(" -",doc.metadata.get("source","Unknown"))

if __name__ == "__main__":
    while True:
        query = input("\nAsk a question (or type 'exit'): ")
        if query.lower() in ["exit", "quit"]:
            break
        ask_question(query)