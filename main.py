import pymongo
from pymongo import MongoClient

client = MongoClient("localhost", 27017)           #padrão

#print(client.list_database_names())

#Criar uma base de dados
db = client.Conhecendo_MongoDB
serverStatusResult = db.command("serverStatus")      #verifica o status do servidor
print(serverStatusResult)

db.fruits.insert_many(
    [
        {'Banana': 'Yellow'},
        {'Orange': 'Orange'},
        {'Apple' : 'Red'},
        {'Lemon' : 'Green'}
    ]
)

print(db.fruits.find_one({'Banana' : 'Yellow'}))          #retorna o ID do objeto

