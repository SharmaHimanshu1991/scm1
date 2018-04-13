#!/usr/bin/python2


import time
import commands
import re

print commands.getoutput(" arp -a | cut -f2 -d'(' | cut -f1 -d')' " )

time.sleep(2)

execfile('start.py')






