import os
import re
x=os.popen("nmap -sP 192.168.43.1/24").read()
ip=re.findall(r'[0-9]+(?:\.[0-9]+){3}',x)
mac=[]
for value in ip:
	cmd="sudo arping -I wlan0 -c 1 "+value
	y=os.popen(cmd).read()
	mac.append(re.findall(r'(?:[0-9a-fA-F]:?){12}',y))
print "IP\t\t","Mac"
for i in range(0,len(ip)):
	print ip[i],mac[i]
