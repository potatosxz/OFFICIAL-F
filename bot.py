import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='Fortnite'))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '$owner':
        await client.send_message(message.channel,'KUBUS#1749 dan NADYA KENTANG#5975')
    if message.content == '$botmaker':
        await client.send_message(message.channel,'@potatos.#0707')
    if message.content == '$invitelink':
        await client.send_message(message.channel,'https://discord.gg/Ay3nW7s')
    if message.content == '$vape':
        await client.send_message(message.channel,'ngevape kok onlen boedjank')
    if message.content.startswith('$gw ganteng?'):
        randomlist = ["iya","tidak",]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('$gw cantik?'):
        randomlist = ["iya","tidak",]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('Halo'):
        await client.send_message(message.channel,'Hai <@%S>'  %(message.author.id))
  
  
 
#YOU CAN USE os.environ TO HIDE YOUR BOT TOKEN: SAVE YOUR BOT TOKEN AS THE NAME YOU GAVE IN os.environ['name'] 
bot.run(os.environ['BOT_TOKEN'])
