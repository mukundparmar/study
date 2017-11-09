#!/usr/bin/python
import subprocess
import os
with open(os.devnull, "wb") as limbo:
        for n in xrange(1, 255):
                ip="10.11.1.{0}".format(n)
                result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
                        stdout=limbo, stderr=limbo).wait()
                if result:
                        print ip, "inactive"
                else:
                        print ip, "active"
