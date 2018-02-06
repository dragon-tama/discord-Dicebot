# -*- coding: utf-8 -*-

import discord
import random
import re
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
            res = "e.g. if you send \'!1d100\'; \'!2D6+6\', this bot return the result."
            await client.send_message(message.channel, res)

    elif message.content.startswith('!'):
        if client.user != message.author:
            m = re.match(r"\!([0-9]{1,3})[Dd]([0-9]{1,3})", message.content)
            l = re.match(r"\!([0-9]{1,3})[Dd]([0-9]{1,3})\+([0-9]{1,3})", message.content)

            if l:
                count = int(l.group(1))
                dice = int(l.group(2))
                add = int(l.group(3))
                result = []
                addresult = 0

                for n in range(count):
                    i = random.randrange(1, dice)
                    result.append(i)
                    addresult += i

                addresult += add
                maped = map(str, result)
                each = ','.join(maped)
                res = str(addresult) + " (" + each + ")"
                await client.send_message(message.channel, res)



            elif m:
                count = int(m.group(1))
                dice = int(m.group(2))
                result = []
                addresult = 0

                for n in range(count):
                    i = random.randrange(1, dice)
                    result.append(i)
                    addresult += i

                maped = map(str, result)
                each = ','.join(maped)
                res = str(addresult) + " (" + each + ")"
                await client.send_message(message.channel, res)

client.run("token")
