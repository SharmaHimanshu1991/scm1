#!/usr/bin/python2

from  time  import  sleep
print  "########################################################"
print  "########################################################"
print  "                                                        "
print  "Starting my Network scanning TooL :@@@@ "
sleep(2)

options='''
Press 1  to  Check your own IP :  
Press 2  to  Check all connected IP from your Machine :    
Press 3  to  all the IP address in your current network : 
Press q  to  close the programe :
'''

print  options
#  below function used for taking input from user 
choice=raw_input()

if  choice  ==  '1' :

	execfile('scanning.py')
	#  this function for calling  another file

elif  choice == '2' :
	execfile('connected.py')

elif  choice ==  'q' :
	exit()

else :
	print  "Plz make your choice correct " 
	sleep(1.78)
	print   "Due to invalid option we are terminating the programe"
	sleep(1.78)
	print   "You can start it again "
	sleep(1.78)
	exit()

