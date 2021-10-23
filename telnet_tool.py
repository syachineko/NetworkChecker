#!/usr/bin/python3

import subprocess
import sys

# Variables
OKLists = []
NGLists = []

# input data
# <IP>::<Port>

importFile = open(sys.argv[1], "r")
importFileList = importFile.readlines()
items = []
for i in importFileList:
    items.append(i.replace("\n",""))

for item in items:
    
    ip,ports=item.split("::")

    for port in ports.split(","):

        print(ip,port)
        ans = "try <telnet " + ip + " " + port + "> -->"

        # try command
        try:
            res = subprocess.run(["telnet",ip,port], stdout=subprocess.PIPE, timeout=1)
            ans += "OK"
            OKLists.append(ans)
            
        except:
            ans += "NG"
            NGLists.append(ans)

print("Result-------------------------------")
print("Summary Total:"+str(len(OKLists)+len(NGLists))+"  OK:"+str(len(OKLists))+ "  NG:"+str(len(NGLists)))
print("")
print("NG Lists-----------------------------")
for result in NGLists:
    print(result)
print("")
print("-------------------------------------")


