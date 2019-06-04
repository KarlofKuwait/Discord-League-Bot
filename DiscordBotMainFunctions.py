"""
Name: Password Manager
Made By: Mads Hermansen
Github: https://github.com/KarlofKuwait
Date: 04/06/2019
"""

from datetime import datetime
import random
import time
import os
import errno
import json
import requests
import discord

# Settings
bot_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
riot_api_key = ""
champs = [x.strip() for x in open("Champlist.txt").readlines()]
createlog = False
logfilename = "Chatlog.txt"
# End Settings

# Messages
role_error = "Please specify the role, examples are \n- all \n- top \n- jng \n- mid \n- adc \n- sup"
custom_message = "hehe"
custom_message_response = "oh you are an amazing person "
# End Messages

client = discord.Client()

@client.event
async def on_message(message):
    # If bot sees a message from itself it does not respond
    author = message.author
    channel = message.channel
    usermessage = message.content.split(" ")
    if author == client.user:
        return
    # Respond to message with message
    # Respond to custom_message
    if message.content.startswith(custom_message):
        await channel.send(custom_message_response + str(author))

    # Respond to !Help
    if message.content.startswith("!help") or message.content.startswith("!Help"):
        if len(usermessage) > 2:
            await channel.send("Please specify a working command")
        else:
            await channel.send("""Commands \n- Help \n- Champ \n- Info""")

    # Respond to !Champ
    if message.content.startswith("!champ") or message.content.startswith("!Champ"):
        if len(usermessage) > 2:
            await channel.send(role_error)
        try:
            if usermessage[1] == "all" or usermessage[1] == "All":
                await channel.send(random.choice(champs))
            else:
                await channel.send(role_error)
        except IndexError:
            await channel.send(role_error)

    # Respond to !Info need Riot API
    if message.content.startswith("!info") or message.content.startswith("!Info"):
        await channel.send("Currently this command doesnt work, instead try !Champ")

    # Review the sent message (Optional log)
    now = datetime.now()
    dt_string = now.strftime("[%d/%m/%Y %H:%M:%S]")
    log = (str(channel) + dt_string + str(author) + " sent \"" + str(message.content) + "\"")
    # Create log
    if createlog:
        """
        I know discord automatically logs everything and it is saved
        onto their servers, it is optional if a custom log is created
        """
        try:
            prevlog = [x.strip() for x in open(logfilename).readlines()]

        except:
            prevlog = ""
        with open(logfilename, "w") as f:
            for info in prevlog:
                f.write(str(info) + "\n")
            f.write(log)
            f.close()
    print(log)


@client.event
async def on_ready():
    print("Bot Name: " + str(client.user.name))
    print("User Client ID " + str(client.user.id))
    print("Time taken: " + str(time.time() - start))
    print()

def start():
    global start
    print("Initializing bot...")
    start = time.time()
    client.run(bot_token)

start()
