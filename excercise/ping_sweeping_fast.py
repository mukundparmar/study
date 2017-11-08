#!/usr/bin/python
#subprocess module is for to spawning process, and ipaddres module used for manupulating ipaddresses.
import subprocess
import ipaddress

p = {} # ip --> process
for n in range(1,254): #start ping prcess
	ip = "10.11.0.%d",%n
	p[ip] Popen(['ping', ])
