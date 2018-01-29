# -*- coding: utf-8 -*-

import discord
import random
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('----')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('----')

@client.event
async def on_message(message):
    
    if message.content.startswith('!help'):
        if client.user != message.author:
            res = "e.g. if you send \'!1d100\', this bot return the result."
            await client.send_message(message.channel, res)

    elif message.content.startswith('!'):
        if client.user != message.author:
            m = message.content.lstrip('!')
            dice = m.split('d')
            stop = int(dice[0]) * int(dice[1])
            res = random.randrange(1, stop)
            await client.send_message(message.channel, res)

client.run("token")
