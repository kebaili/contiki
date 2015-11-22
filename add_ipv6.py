#!/usr/bin/python
import json
f = open('ipv6bis.txt','r')
data=json.load(f)
print data["node"]["node-type"]
print data["node"]["time"]
print data["rsc"]["temperature"]["value"]
print data["rsc"]["leds"]
new_data={}
new_data["ipv6"] = "aaaa::c30c:0:0:2"
new_data["node-type"] = data["node"]["node-type"]
new_data["time"] = data["node"]["time"]
new_data["temperature"] = data["rsc"]["temperature"]["value"]
new_data["leds"] = data["rsc"]["leds"]
print json.dumps(new_data, indent=4)
f.close()
