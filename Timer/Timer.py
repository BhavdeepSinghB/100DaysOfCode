#Author: Bhavdeep Singh
#Project: Timer.py - simple command line timer
#Build Log Attached as txt

import time
import sys



if len(sys.argv) == 1:
    print "Use: Timer.py <hh:mm:ss>"
    sys.exit()

target = sys.argv[1].split(":")
targetHr = int(target[0])
targetMin = int(target[1])
targetSec = int(target[2])

incrementTime = time.localtime() 
incrementHr = incrementTime.tm_hour
incrementMin = incrementTime.tm_min
incrementSec = incrementTime.tm_sec

print("{}:{}:{}".format(incrementHr,incrementMin, incrementSec))

finalMin = incrementMin + targetMin
finalSec = incrementSec + targetSec
finalHr = incrementHr + targetHr

if(finalSec >= 60):
    finalSec -= 60
    finalMin += 1
if(finalMin >= 60):
    finalMin = 0
    finalHr += 1
if(finalHr < incrementHr):
    finalHr += 24

print "{}:{}:{}".format(finalHr, finalMin, finalSec)

while(incrementMin != finalMin) or (incrementSec != finalSec) or (incrementHr != finalHr):

    incrementSec += 1
    if incrementSec == 60:
        incrementMin += 1
        incrementSec = 0
    if incrementMin == 60:
        incrementHr += 1
        incrementMin = 0
    
    if finalMin - incrementMin < 0:
        if finalSec - incrementSec < 0:
            print "%02d:%02d:%02d" % (finalHr - incrementHr, (60 + finalMin) - incrementMin, (60 + finalSec) - incrementSec)
        else:
            print "%02d:%02d:%02d" % (finalHr - incrementHr, (60 + finalMin) - incrementMin, finalSec - incrementSec)
    else:
        if finalSec - incrementSec < 0: 
            print "%02d:%02d:%02d" % (finalHr - incrementHr, (finalMin-incrementMin) - 1, (60 + finalSec) - incrementSec)
        else:
            print "%02d:%02d:%02d" % (finalHr - incrementHr, finalMin-incrementMin, finalSec - incrementSec)
    
    sys.stdout.write("\033[F")
    time.sleep(1)
    
    
    
print "{}:{}:{}".format(incrementHr,incrementMin, incrementSec)

