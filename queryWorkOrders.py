
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma

import openai

persist_directory="chromaPersistanceForWorkOrders"

embedding = OpenAIEmbeddings(openai_api_key="")

vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)

question = "what is the status for work order 00052"

docs = vectordb.similarity_search(query=question, k=8)

data = ''

for doc in docs:
    data += doc.page_content + '\n'

prompt = "answer the question '" + question + "'\nwith the following data:\n\n" + data

print(prompt)

openai.api_key = "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"

response = openai.Completion.create(
    engine='text-davinci-003',
    prompt=prompt
)

print(response.choices[0].text)

