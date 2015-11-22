#!/usr/bin/python

import json
import urllib2
import time
from pymongo import MongoClient

f = open('ipv6.txt','r')
content = f.readlines()
x=len(content)
client = MongoClient('mongodb://localhost:27017/')
db = client.contikidb
collection = db.test
j=0
while j<10:
	i=0
	while i<x:
		y=content[i].strip()
		print "http://["+y+"]"
		z = "http://["+y+"]"
		donnee = urllib2.urlopen(z)
		m = donnee.read()
		m1 = str(m)
		data=json.loads(m1)
		new_data={}
		new_data["ipv6"] = y
		new_data["node-type"] = data["node"]["node-type"]
		new_data["time"] = data["node"]["time"]
		new_data["temperature"] = data["rsc"]["temperature"]["value"]
		new_data["leds"] = data["rsc"]["leds"]
		print json.dumps(new_data)
		collection.insert(new_data)
		i+=1
	time.sleep( 5 )
	j+=1
f.close()
