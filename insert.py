#!/usr/bin/python

from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client.contikidb
collection = db.test
collection.insert({"node-type": "Zolertia Z1", "leds": 0, "time": 3489, "temperature": 1.5, "ipv6": "aaaa::c30c:0:0:2"})
