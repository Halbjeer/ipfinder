#!/usr/bin/python3

import socket
import time
import random

# Halbjeer thekurd 

print ("-------------- Coded BY Halbjeer TheKurd--------------\n\n")
a = input("ta dvet ip xo bzani (y/n) ")
if a == "y":
    ping = input ("Enter Website : ")
    print ('wait 5 second :)')
    x = random.randrange(5,10)
    time.sleep(x)
    print ("IP : " + socket.gethostbyname(ping))
if a == "n":
    print ("supas bote :) ")
