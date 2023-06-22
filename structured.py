
from string import Template
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma

persist_directory="chromaPersistanceForWorkOrders"

embedding = OpenAIEmbeddings(openai_api_key="")

filePath = 'ActiveWorkOrders.csv'

file = open(filePath, 'r')

lines = file.readlines()

template = Template(("The work order '$workOrderNumber'"
                     " for service account '$serviceAccount'"
                     " was created on '$createdOn'"
                     " the current status is '$systemStatus',"
                     " the work order type is '$workOrderType'"
                     " and the primary incident type is '$primaryIncidentType'"))

texts = []

for line in lines:
    fields = line.strip().split(',')

    text = template.substitute(
        modified = fields[2],
        workOrderNumber = fields[3],
        serviceAccount = fields[4],
        systemStatus = fields[7],
        createdOn = fields[8],
        workOrderType = fields[9],
        primaryIncidentType = fields[10],
        primaryIncidentDescription = fields[11])

    texts.append(text)

vectordb = Chroma.from_texts(texts=texts, embedding=embedding, persist_directory=persist_directory)

vectordb.persist()


 




