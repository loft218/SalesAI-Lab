from langchain import OpenAI
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.embeddings import SentenceTransformerEmbeddings


# 初始化，加载env变量
import init


def main():
    llm = OpenAI(temperature=0.5)
    # embeddings = OpenAIEmbeddings()
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    # 从数据库读取documents
    doc_search = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)

    # 创建问答对象
    retriever = doc_search.as_retriever()
    retrievalQA = RetrievalQA.from_chain_type(
        llm=llm, chain_type="stuff", retriever=retriever
    )

    while True:
        question = input("\n我: ")
        result = retrievalQA({"query": question})
        print("🤖:" + result["result"] + "\n")


if __name__ == "__main__":
    main()
