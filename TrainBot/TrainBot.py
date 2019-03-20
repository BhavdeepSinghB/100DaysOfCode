import asyncio
import discord
import time
import collections
from threading import Timer

TOKEN = 'your token here'
inviteCode = 'your invite here'

client = discord.Client()


trainQueue = collections.deque([])


@client.event
async def trainStuff():
        if(len(trainQueue) != 0):
            global popped
            popped = trainQueue.popleft()
            await popped.send("Your invite code is ready, please type !claim to claim it. You have 10 minutes")

@client.event
async def on_message(message):
    #client.loop.create_task(trainStuff())
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
            print("here")
            await message.author.send("{} is your invite code, please generate an invite and use !invite + your code to keep the train moving".format(inviteCode))
        else:
            await message.author.send("Wait your turn")

def addToQueue(author):
    if author not in trainQueue:
        trainQueue.append(author)
        return True
    return False


    



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)