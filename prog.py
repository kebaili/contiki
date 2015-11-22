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
	data = urllib2.urlopen(z)
	print data.read()
	i+=1
f.close()
