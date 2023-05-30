# AI 销售

这是一个试验程序

## TODO

- [ ] 返回结构化格式，支持图文
- [ ] 对话支持前置上下文
- [ ] 增量更新数据库

## 配置说明

修改文件 `.env.local` 为 `.env`，并配置你的 **你的 OPENAI_API_KEY**

## 依赖

windows 需要 c++编译工具

> Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/

### 安装依赖

```
pip install -r requirements.txt
```

### 依赖包有

- chromadb
- tiktoken
- unstructured
- tabulate
- pdf2image

## 运行说明

### 第 1 步：加载文本数据到 chroma

```
python directory_loader.py
```

### 第 2 步：执行主程序

```
python main.py
```
