
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma

persist_directory="chromaPersistance"

embedding = OpenAIEmbeddings(openai_api_key="")

vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)

docs = vectordb.similarity_search("how can I install a new printer driver")

if len(docs) > 0:
    print(docs[0])

