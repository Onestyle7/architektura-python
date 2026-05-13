from pymongo import MongoClient
import requests

client = MongoClient("mongodb://localhost:27017")
db = client.lab4
networks = db["networks"]

networks.drop()

response = requests.get("https://api.geckoterminal.com/api/v2/networks")
data = response.json()["data"]

networks.insert_many(data)

pipeline = [
     {"$group": {"_id": "$type", "count": {"$sum": 1}}},
     {"$sort": {"count": -1}}
]

for doc in networks.aggregate(pipeline):
    print(doc)