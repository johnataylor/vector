
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader

persist_directory="chromaPersistance"

embedding = OpenAIEmbeddings(openai_api_key="")

from pypdf import PdfReader
pdfReader = PdfReader("HP-Laserjet-4-5-Service-Manual.pdf")

text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=10, chunk_overlap=0)

texts = []

for page in pdfReader.pages:
    text = page.extract_text()
    docs = text_splitter.split_text(text)
    for d in docs:
        texts.append(d)

vectordb = Chroma.from_texts(texts=texts, embedding=embedding, persist_directory=persist_directory)

vectordb.persist()

vectordb = None
