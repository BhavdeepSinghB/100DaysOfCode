import asyncio
import discord
import time
import collections
from threading import Timer


TOKEN = 'NTU3MzMzMTMyODY1Njk5ODQz.D3GxZg.EFfkSxAU3IHWmERPTzhbnX85CDQ'
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

@client.event
async def on_message(message):
    person = message.author
    if person == client.user:
        return

    if message.content.lower().startswith('!train add'):

        if addToQueue(person) == True:
            await message.channel.send("{0.name} added to the train".format(person))
        else:
            await message.channel.send("{0.name} is already on the train".format(person))

    await trainStuff()
    if(message.content.lower().startswith('!claim')):
        if(message.author == popped):
            inviteCode = readFromFile()
            await message.author.send("{} is your invite code, please generate an invite and use !invite + your code to keep the train moving".format(inviteCode))
        else:
            await message.author.send("Wait your turn")

    if(message.content.lower().startswith('!invite')):
        if(message.author == popped):
            newinv = message.content
            newinv = newinv.replace("!invite ", "")
            inviteCode = newinv
            writeToFile(newinv)
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
            if on_message.count == 0:
                await popped.send("Your invite code is ready, please type !claim to claim it. You have 10 minutes")
                on_message.count += 1
            
                


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
client.run(TOKEN)