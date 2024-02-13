
#Import Libraries Here
import time
import sys

timeToSleep = 1

print("\n\nWelcome to InforTech Center V1.0\n")
time.sleep(timeToSleep)

#Code to have the ellipsi add a dot every .5 seconds
x = 0
ellipsis = 0

while x != 20:
    x += 1
    message = ("Infotech Center System Booting"+"."* ellipsis)
    ellipsis = ellipsis + 1
    sys.stdout.write("\r"+ message) # \r prints a carriage return first
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\n\nOperating system Booted Up - Retina Scanned - Access Granted!")