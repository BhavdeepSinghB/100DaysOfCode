import asyncio
import discord
import time
import collections
from threading import Timer
import requests
import json
import string
import signal

TOKEN = ''
fileName = "invitesaver.bin"
inviteCode = ""
client = discord.Client()
trainQueue = collections.deque([])


def addToQueue(author):
    if author not in trainQueue:
        trainQueue.append(author)
        return True
    return False

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

def noResponse(signum, frame):
    trainStuff.claimed = False
    if(len(trainQueue) != 0):
        trainQueue.popleft()
    on_message.count = 0

@client.event
async def on_message(message):
    person = message.author
    if person == client.user:
        return
    #await channel.send("hello")
    if message.content.lower().startswith('!train add'):

        if addToQueue(person) == True:
            await message.channel.send("{0.name} added to the train".format(person))
        else:
            await message.channel.send("{0.name} is already on the train".format(person))

    await trainStuff()
    #await reminders()
    if(message.content.lower().startswith('!claim')):
        print(trainStuff.claimed)
        signal.alarm(0)
        if(trainStuff.claimed == False):
            await message.author.send("Too late, please add yourself to the train again")
            trainStuff.claimed = True
        elif(message.author == popped and trainStuff.claimed is True):
            inviteCode = readFromFile()
            await message.author.send("{} is your invite code, please generate an invite and use !invite + your code to keep the train moving".format(inviteCode))
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
on_message.count = 0

@client.event
async def trainStuff():    
    if(len(trainQueue) != 0):
        global popped
        popped = trainQueue[0]
        global claimed
        if on_message.count == 0:
           await popped.send("Your invite code is ready, please type !claim to claim it. You have 10 minutes")
           signal.signal(signal.SIGALRM, noResponse)
           signal.alarm(5)
           on_message.count += 1
    else:
        popped = None

@client.event
async def reminders():
    await client.wait_until_ready()
    #i = 0
    print("I am here")
    while(not client.is_closed):
        channel = client.get_channel(id=560227488786284554)
        await channel.send("Hello")
        await asyncio.sleep(5)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.loop.create_task(reminders())
client.run(TOKEN)
