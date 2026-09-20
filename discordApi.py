import discord
import diceRoller
import pandas as pd
import os 
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')
DM_ACTION = os.getenv('DM')

intent = discord.Intents.default()
intent.message_content = True
client = discord.Client(intents=intent)
guild = discord.Guild

@client.event
async def on_message(message):
    message_content =  message.content.lower()
    message_author = message.author
    if message_content.startswith('!dice')  == True:
        await message.channel.send(diceRoller.StringAnalizer(message_content,message_author))
    elif message_content.startswith('!attack')  == True:
        if str(message_author) == DM_ACTION:
            await message.channel.send(diceRoller.Attacking())
    elif message_content.startswith('!mattack')  == True:
        if str(message_author) == DM_ACTION:
            await message.channel.send(diceRoller.AttackingM())
    elif message_content.startswith('!photo')  == True:
        # estructura !photo nombre_archivo extension(png, jpg, webp) 
        if str(message_author) == DM_ACTION:
            returnData = diceRoller.PhotoSending(message_content)
            await message.channel.send(file=returnData[0], embed=returnData[1])
    elif message_content.startswith('!advantage') or message_content.startswith('!disadvantage') == True:
         await message.channel.send(diceRoller.AdvantageDisadvantageCalc(message_content,message_author))
    elif message_content.startswith('!me') or message_content.startswith('!health') == True:
         await message.channel.send(diceRoller.ViewHealth(message_content,message_author))
    elif message_content.startswith('!add') or message_content.startswith('!minus') or  message_content.startswith('!reset') == True:
        if str(message_author) == DM_ACTION and message_content.startswith('!reset'):
             await message.channel.send(diceRoller.HealthModifier(message_content,message_author))
        await message.channel.send(diceRoller.HealthModifier(message_content,message_author))


if __name__ == "__main__":
    client.run(API_TOKEN)
