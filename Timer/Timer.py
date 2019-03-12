#Author: Bhavdeep Singh
#Project: Timer.py - simple command line timer
#Build Log Attached as txt

import time
import sys


if len(sys.argv) == 1:
    print "Use: Timer.py <target time>"
    sys.exit()

target = sys.argv[1].split(":")
targetMin = int(target[0])
targetSec = int(target[1])

incrementTime = time.localtime()
incrementMin = incrementTime.tm_min
incrementSec = incrementTime.tm_sec

print("9:{}:{}".format(incrementMin, incrementSec))

finalMin = incrementMin + targetMin
finalSec = incrementSec + targetSec

if(finalSec >= 60):
    finalSec -= 60
    finalMin += 1
    

while(incrementMin != finalMin) or (incrementSec != finalSec):
    if finalSec - incrementSec < 0:
        print "{}:{}".format(finalMin-incrementMin - 1, 60 + (targetSec - incrementSec))
    else:
        print "{}:{}".format(finalMin-incrementMin, finalSec - incrementSec)
   
    sys.stdout.write("\033[F")
    time.sleep(1)
    
    incrementSec += 1
    if incrementSec == 60:
        incrementMin += 1
        incrementSec = 0
    
print "{}:{}".format(incrementMin, incrementSec)

