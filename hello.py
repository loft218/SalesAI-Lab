from langchain.llms import OpenAI

# 初始化，加载env变量
import init

llm = OpenAI(temperature=0.9)

text = "hello?"
print(llm(text))
