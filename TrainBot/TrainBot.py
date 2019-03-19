import asyncio
import discord
import time

TOKEN = 'NTU3MzMzMTMyODY1Njk5ODQz.D3GxZg.EFfkSxAU3IHWmERPTzhbnX85CDQ'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('!train add'):
        await message.channel.send("{0.name} added to the train".format(message.author))
        addToStack(message.author)

trainStack = []

def addToStack(author):
    trainStack.append(author)
    print (trainStack)



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)