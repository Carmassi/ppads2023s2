from dotenv import load_dotenv, find_dotenv
import os
import pymongo
from datetime import datetime

load_dotenv(find_dotenv())

password = os.environ.get("MONGO_PWD")
connection_string = f"mongodb+srv://Carmassi:{password}@cluster0.qp9dsx1.mongodb.net/"
client = pymongo.MongoClient(connection_string)


db = client["brasileirao"]

times_collection = db["times"]
resultados_collection = db["resultados"]
jogos_collection = db["jogos"]


times_participantes = [
    "Flamengo",
    "Palmeiras",
    "Atlético Mineiro",
    "São Paulo",
    "Santos",
]

for time in times_participantes:
    times_collection.insert_one({"nome": time})

resultados_passados = [
    {
        "time_casa": "Flamengo",
        "time_visitante": "Palmeiras",
        "placar_casa": 2,
        "placar_visitante": 1,
        "data": datetime(2023, 9, 20),
    },
    {
        "time_casa": "Atlético Mineiro",
        "time_visitante": "São Paulo",
        "placar_casa": 3,
        "placar_visitante": 0,
        "data": datetime(2023, 9, 21),
    },
]

for resultado in resultados_passados:
    resultados_collection.insert_one(resultado)

proximos_jogos = [
    {
        "time_casa": "Santos",
        "time_visitante": "Flamengo",
        "data": datetime(2023, 9, 25),
    },
    {
        "time_casa": "Palmeiras",
        "time_visitante": "Santos",
        "data": datetime(2023, 9, 28),
    },
    {
        "time_casa": "Palmeiras",
        "time_visitante": "Atlético Mineiro",
        "data": datetime(2023, 9, 26),
    },
]


for jogo in proximos_jogos:
    jogos_collection.insert_one(jogo)


print("Times participantes:")
for time in times_collection.find():
    print(time["nome"])

print("\nResultados passados:")
for resultado in resultados_collection.find():
    print(
        f"{resultado['time_casa']} {resultado['placar_casa']} x {resultado['placar_visitante']} {resultado['time_visitante']} - {resultado['data']}"
    )

print("\nPróximos jogos:")
for jogo in jogos_collection.find():
    print(f"{jogo['time_casa']} x {jogo['time_visitante']} - {jogo['data']}")

client.close()
