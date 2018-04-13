#!/usr/bin/python2


import time
import commands
import re

# first check your own ip

print commands.getoutput(" tcpdump -D | grep -vE 'usb|nf|any' | cut -d. -f2 " )

# command to get ip

nic = raw_input ( " type nic from above list : "  )
output =  commands.getoutput(' ifconfig ' +nic )

#print ( type( output))
#print (output)

# spliting the string in list and obtaing ip
print output.split()[5]

print ("program is going to restart")
time.sleep(2)

execfile('start.py')

'''
print( re.search('\d.\d.\d.\d', output))
print((re.split(r'\s',output)))
lis = output.split()
for i in lis :
	match = re.match('(\d.\d.\d.\d)', i)
print match
'''





