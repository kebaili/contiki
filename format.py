#!/usr/bin/python

import json
import urllib2

f = open('ipv6.txt','r')
content = f.readlines()
x=len(content)
i=0
while i<x:
	y=content[i].strip()
	print "http://["+y+"]"
	z = "http://["+y+"]"
	donnee = urllib2.urlopen(z)
	m = donnee.read()
	m1 = str(m)
	data=json.loads(m1)
	print data
	new_data={}
	new_data["ipv6"] = y
	new_data["node-type"] = data["node"]["node-type"]
	new_data["time"] = data["node"]["time"]
	new_data["temperature"] = data["rsc"]["temperature"]["value"]
	new_data["leds"] = data["rsc"]["leds"]
	print json.dumps(new_data, indent=4)
	i+=1
f.close()
