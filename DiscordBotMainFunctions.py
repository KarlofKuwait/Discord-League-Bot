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
riot_api_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
createlog = False
logfilename = "Chatlog.txt"

# Champion settings
allchamps = [x.strip() for x in open("Champlist.txt").readlines()]
topchamps = ["Aatrox", "Akali", "Camille", "Cho'Gath", "Darius",
             "Dr. Mundo", "Fiora", "Gangplank", "Garen", "Gnar",
             "Illoai", "Irelia", "Jax", "Jayce", "Kayle",
             "Kennen", "Kled", "Malphite", "Maokai", "Mordekaiser",
             "Nasus", "Neeko", "Olaf", "Ornn", "Pantheon",
             "Poppy", "Pyke", "Quinn", "Renekton", "Rengar",
             "Riven", "Rumble", "Ryze", "Shen", "Singed",
             "Sion", "Sylas", "Tahm Kench", "Teemo", "Tryndamere",
             "Urgot", "Vayne", "Vladimir", "Volibear", "Wukong",
             "Yasuo", "Yorick"]
jngchamps = ["Aatrox", "Ammumu", "Elise", "Evelynn", "Fiddlesticks",
             "Gragas", "Graves", "Hecarim", "Ivern", "Jarvan IV",
             "Jax", "Karthus", "Kayn", "Kha'Zix", "Kindred",
             "Lee Sin", "Master Yi", "Nidalee", "Nocturne", "Nunu & Willump"
             "Pantheon", "Rammus", "Rek'Sai", "Rengar", "Sejuani",
             "Shaco", "Shyvana", "Skarner", "Trundle", "Twitch",
             "Udyr", "Vi", "Volibear", "Warwick", "Wukong",
             "Xin Zhao", "Zac"]
midchamps = ["Aatrox", "Ahri", "Akali", "Anivia", "Annie",
             "Azir", "Cassiopeia", "Corki", "Diana", "Ekko",
             "Fizz", "Irelia", "Kassadin", "Katerina", "Leblanc",
             "Lissandra", "Lux", "Malzahar", "Morgana", "Neeko",
             "Orianna", "Pyke", "Ryze", "Swain", "Sylas",
             "Syndra", "Taliyah", "Talon", "Twisted Fate", "Veigar",
             "Vel'Koz", "Viktor", "Vladimir", "Xerath", "Yasuo",
             "Zed", "Ziggs", "Zilean", "Zoe"]
adcchamps = ["Ashe", "Caitlyn", "Draven", "Ezreal", "Jhin",
             "Jinx", "Kai'Sa", "Kalista", "Kog'Maw", "Lucian",
             "Miss Fortune", "Sivir", "Tristana", "Twitch", "Varus",
             "Vayne", "Xayah"]
supchamps = ["Alistar", "Bard", "Blitzcrank", "Brand", "Bruam",
             "Fiddlesticks", "Galio", "Janna", "Karma", "Leona",
             "Lulu", "Lux", "Morgana", "Nami", "Nautilus",
             "Pyke", "Rakan", "Sona", "Soraka", "Taric",
             "Thresh", "Vel'koz", "Xerath", "Yummi", "Zilean",
             "Zyra"
             ]
# End Settings

# Messages
role_error = "Please specify the role, examples are \n- all \n- top \n- jng \n- mid \n- adc \n- sup"
custom_message = "whats ligma"
custom_message_response = "ligma balls "
# End Messages

client = discord.Client()

def requestSummonerData(summonerName, riot_api_key):
    URL = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + riot_api_key
    response = requests.get(URL)
    return response.json()

def requestSummonerRank(summonerName, riot_api_key):
    URL = "https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + summonerName + "?api_key=" + riot_api_key
    response = requests.get(URL)
    return response.json()

@client.event
async def on_message(message):
    # If bot sees a message from itself it does not respond
    author = message.author
    channel = message.channel
    usermessage = message.content.split(" ")
    if author == client.user:
        return
    # Respond to message with message
    # Respond to custom messages
    if message.content.startswith(custom_message):
        await channel.send(custom_message_response + str(author))
    if message.content.startswith("no u"):
        await channel.send("Uno reverse card")

    # Respond to !Help
    if message.content.startswith("!help") or message.content.startswith("!Help"):
        if len(usermessage) > 2:
            await channel.send("Please specify a working command")
        try:
            if usermessage[1] == "help" or usermessage[1] == "Help":
                await channel.send("""Help is used to find information about commands
                
Syntax:
!help
!help (command name)

Uses:
help - lists all available commands
(command name) - lists information about the command""")
            elif usermessage[1] == "champ" or usermessage[1] == "Champ":
                await channel.send("""Use Champ to randomize a champ or add champs
to your list to randomize

Syntax:
!champ
!champ (role)
!champ add (champion)
!champ remove (champion)
!champ list
!champ me

Uses:
champ - randomizes a champion from a role
add - adds a champion to your list of champions
remove - removes a champion from your list of champions
list - lists all the champions in the your list
me - randomizes a champion from your list of champions""")
            elif usermessage[1] == "info" or usermessage[1] == "Info":
                    await channel.send("""Use Champ to randomize a champ or add champs
to your list to randomize

Syntax:
!info
!info (summonername)
!info mastery (summonername)

Uses:
info - gain information about riot servers
info (summonername) - gain information about a summoner
info mastery - gain information about someones mastery
""")
            else:
                await channel.send("""Commands \n- Help \n- Champ \n- Info""")
        except IndexError:
            await channel.send("""Commands \n- Help \n- Champ \n- Info""")

    # Respond to !Champ
    if message.content.startswith("!champ") or message.content.startswith("!Champ"):
        if len(usermessage) > 2:
            await channel.send(role_error)
        try:
            if usermessage[1] == "all" or usermessage[1] == "All":
                await channel.send(random.choice(allchamps))
            elif usermessage[1] == "top" or usermessage[1] == "Top":
                await channel.send(random.choice(topchamps))
            elif usermessage[1] == "jng" or usermessage[1] == "Jng":
                await channel.send(random.choice(jngchamps))
            elif usermessage[1] == "mid" or usermessage[1] == "Mid":
                await channel.send(random.choice(midchamps))
            elif usermessage[1] == "adc" or usermessage[1] == "Adc":
                await channel.send(random.choice(adcchamps))
            elif usermessage[1] == "sup" or usermessage[1] == "Sup":
                await channel.send(random.choice(supchamps))
            else:
                await channel.send(role_error)
        except IndexError:
            await channel.send(role_error)

    # Respond to !Info need Riot API
    if message.content.startswith("!info") or message.content.startswith("!Info"):
        if len(usermessage) > 2:
            await channel.send("Please only have the summonername")
        # Retrieve data about account
        try:
            summonerdata = requestSummonerData(usermessage[1], riot_api_key)
            summonerid = (summonerdata.get("id"))
            summonerrank = requestSummonerRank(summonerid, riot_api_key)
            # Create Message
            info_bot_message = usermessage[1] + "\n"
            for x in summonerrank:
                if x.get("queueType") == "RANKED_SOLO_5x5":
                    info_bot_message += "Ranked Solo: \n" + x.get("tier") + " " + x.get(
                        "rank") + "\n" + str(x.get("leaguePoints")) +" LP"
            for x in summonerrank:
                if x.get("queueType") == "RANKED_FLEX_SR":
                    info_bot_message += "\n\nRanked Flex: \n" + x.get("tier") + " " + x.get(
                        "rank") + "\n" + str(x.get("leaguePoints")) +" LP"

        except TypeError:
            info_bot_message = ("Account not found, \nplease try again")
        # Say message
        await channel.send(info_bot_message)


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
