from langchain.vectorstores import Chroma
from langchain.document_loaders import DirectoryLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter

# 初始化，加载env变量
import init

# 加载文件夹中的所有txt类型的文件
loader = DirectoryLoader("./sample_data/", glob="**/*.txt")
# 将数据转成 document 对象，每个文件会作为一个 document
documents = loader.load()

# 初始化加载器
text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
# 切割加载的 document
split_docs = text_splitter.split_documents(documents)

# 初始化 openai 的 embeddings 对象
embeddings = OpenAIEmbeddings()

# 将 document 通过 openai 的 embeddings 对象计算 embedding 向量信息并临时存入 Chroma 向量数据库，用于后续匹配查询
docsearch = Chroma.from_documents(
    split_docs, embeddings, persist_directory="./chroma_db"
)
docsearch.persist()

print("数据已存入本地Chroma")
