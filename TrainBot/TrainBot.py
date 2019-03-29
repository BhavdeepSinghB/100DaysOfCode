import asyncio
import discord
import time
import collections
from threading import Timer
import requests
import json
import string
import signal

TOKEN = 'NTU3MzMzMTMyODY1Njk5ODQz.D3rKBg.RT3L-BcSox26gxmBkXrs6D4EZxc'
fileName = "invitesaver.bin"
inviteCode = ""
client = discord.Client()
trainQueue = collections.deque([])

def addToQueue(author):
    if author not in trainQueue:
        trainQueue.append(author)
        return True
    return False

def removeFromQueue(author):
    if author not in trainQueue:
        return False
    trainQueue.remove(author)
    return True

def findPosition(author):
    if author not in trainQueue:
        return -1
    return trainQueue.index(author)

def writeToFile(arg):
    fh = open(fileName, "w")
    fh.write("{}".format(arg))
    fh.close()

def readFromFile():
    fh = open(fileName, "r")
    code = fh.readline()
    fh.close()
    return code

def isValidInvite(text):
    inviteCode = readFromFile()
    if text == inviteCode:
        return False
    if not (all(c in string.hexdigits for c in text) and len(text) == 32):
        return False
    response = requests.get("https://api.morningstreams.com/api/invites/" + text)
    if response.text == "null":
        return False
    json = response.json()
    if json.get("isUsed"):
        return False
    else:
        return True

def isUsedInvite(text):
    response = requests.get("https://api.morningstreams.com/api/invites/" + text)
    if response.text == "null":
        return True
    json = response.json()
    if json.get("isUsed"):
        return True
    else:
        return False

def noResponse(signum, frame):
    trainStuff.claimed = False
    if(len(trainQueue) != 0):
        trainQueue.popleft()
    on_message.count = 0

def noInv(signum, frame):
    on_message.invite = False
    on_message.count = 0

async def checkBan():
    invite = readFromFile()
    if isUsedInvite(invite):
        await popped.send("Unfortunately you claimed the invite and didn't return it, and hung the train, you have been banned from morningstreams")
        banUser()
    else:
        await popped.send("Your invite was not used and will be given to the next person")
        trainQueue.popleft()
        on_message.count = 0
        trainStuff.claimed = False
        popped = None
        trainStuff()

@client.event
async def on_message(message):
    person = message.author
    if(message.author == client.user):
        on_message.count += 1
    if message.content.lower().startswith('!train add'):

        if addToQueue(person) == True:
            await message.channel.send("{0.name} added to the train".format(person))
        else:
            await message.channel.send("{0.name} is already on the train".format(person))
        on_message.count = 0
    await trainStuff()

    if(message.content.lower().startswith('!claim')):
        if(trainStuff.claimed == False):
            await message.author.send("Too late, please add yourself to the train again")
            trainStuff.claimed = True
        elif(message.author == popped and trainStuff.claimed is True):
            inviteCode = readFromFile()
            await message.author.send("{} is your invite code, please generate an invite and use !invite + your code to keep the train moving".format(inviteCode))
            await message.author.send("You have 10 minutes")
            signal.signal(signal.SIGALRM, noInv)
            signal.alarm(600)
            trainStuff.claimed = True
        else:
            await message.author.send("Wait your turn")
            trainStuff.claimed == True

    if(message.content.lower().startswith('!invite ')):
        if(message.author == popped):
            newinv = message.content
            newinv = newinv.replace("!invite ", "")
            if not isValidInvite(str(newinv)):
                await message.author.send("{} is not a valid invite, please try again".format(newinv))
            else:
                await message.author.send("Thank you for riding the train")
                inviteCode = newinv
                writeToFile(newinv)
                if len(trainQueue) != 0:
                    trainQueue.popleft()
                on_message.count = 0
                await trainStuff()

        else:
            await message.author.send('Wait your turn')

    if(message.content.lower().startswith('!train remove')):
        if findPosition(person) == 0:
            removeFromQueue(person)
            await message.channel.send("{0.name} removed from the train".format(message.author))
            on_message.count = 0
            await trainStuff()
        elif removeFromQueue(person) == True:
            await message.channel.send("{0.name} removed from the train".fromat(message.author))
        else:
            await message.channel.send("{0.name} was not found in the train".format(message.author))

    if(message.content.lower().startswith('!train help')):
        await message.channel.send("!train add       -      Hop on the train")
        await message.channel.send("!train remove    -      Hop off the train\n")
        await message.channel.send("If you are already on the train \n!train check   -     Check your position")

    if(message.content.lower().startswith('!train check')):
        position = findPosition(person)
        if position == 0:
            await message.channel.send("{} at position {} in the train. Check your Private Messages there's a 10 minute limit".format(str(person)[:-5], int(position) + 1))
        elif position == -1:
            await message.channel.send("{0.name} not found on the train, please type !train add to add yourself".format(person))
        else:
            await message.channel.send("{} at position {} in the train".format(str(person)[:-5], int(position) + 1))

    if(on_message.invite == False):
        await checkBan()
on_message.count = 0
on_message.invite = True
@client.event
async def trainStuff():    
    if(len(trainQueue) != 0):
        global popped
        popped = trainQueue[0]
        global claimed
        if on_message.count == 0:
           await popped.send("Your invite code is ready, please type !claim to claim it. You have 10 minutes")
           signal.signal(signal.SIGALRM, noResponse)
           signal.alarm(600)
           on_message.count += 1
    else:
        popped = None
trainStuff.claimed = True

@client.event
async def reminders():
    await client.wait_until_ready()
    print("I am here")
    channel = client.get_channel(560227488786284554)
    while not client.is_closed():
        await channel.send("The train is taking in new passangers all the time! Type \"!train add\" to hop on and grab an invite")
        await channel.send("Type \"!train remove\" to hop off the train in case you got your invite or \"!train help\" for other commands")
        await asyncio.sleep(600)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.loop.create_task(reminders())
client.run(TOKEN)
