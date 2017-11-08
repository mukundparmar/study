#!/usr/bin/python
#defined function to find which operating system has installed in current machine
import platform
import subprocess

#def os_name(self):
#	os = platfrom.system()
#	if (os == "Windows"):
##		ping = "ping -n {} {}"
#		print 'OS is windows'
#	elif (os == "Linux"):
#		ping = "ping -c {} {}"
#		print 'OS is Linux'
#	else:
#		ping = "ping -c {} {}"
#		print "os is other than windows and linux"
#	self.command = ping
#	return
for ping in range(1,254):
	address = "10.11.0."+ str(ping)
	res = subprocess.call(['ping', '-c', '1', address])
	if res == 0:
		print "ping to" + address + "OK"
	elif res == 2:
		print "no respose from", address
	else:
		print "ping to" + address + "failed!"
