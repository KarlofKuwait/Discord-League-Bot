"""
Name: Discord Bot - Riot API return values
Made By: Mads Hermansen
Github: https://github.com/KarlofKuwait
Date: 05/06/2019
"""

from datetime import datetime
import random
import time
import os
import errno
import requests
import discord
import DiscordBotRedundantFunctions as dbrf

# Settings
bot_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
riot_api_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
createlog = False
logfilename = "Chatlog.txt"

# Champion settings
allchamps = [x.strip() for x in open("Champlist.txt").readlines()]
topchamps = dbrf.topchamps
jngchamps = dbrf.jngchamps
midchamps = dbrf.midchamps
adcchamps = dbrf.adcchamps
supchamps = dbrf.supchamps
# End Settings

# Messages
role_error = "Examples of usable roles are \n- all \n- top \n- jng \n- mid \n- adc \n- sup"
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

def requestSummonerMastery(summonerName, riot_api_key):
    URL = "https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + summonerName + "?api_key=" + riot_api_key
    response = requests.get(URL)
    return response.json()

def champcheckandfile(filename):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
    try:
        [x.strip() for x in open(filename).readlines()]
    except:
        with open(filename, "w") as f:
            f.write("")

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
    if message.content.startswith("nani"):
        await channel.send("Dave is sad :(")
    # Respond to !Help
    if message.content.startswith("!help") or message.content.startswith("!Help"):
        if len(usermessage) > 2:
            await channel.send("Please specify a working command")
        try:
            if usermessage[1] == "help" or usermessage[1] == "Help":
                await channel.send("""Help is used to find information about commands
                
**Syntax:**
!help
!help (command name)

**Uses:**
help - lists all available commands
(command name) - lists information about the command""")
            elif usermessage[1] == "champ" or usermessage[1] == "Champ":
                await channel.send("""Use Champ to randomize a champ or add champs
to your list to randomize

**Syntax:**
!champ
!champ (role)
!champ roles
!champ add (champion)
!champ remove (champion)
!champ list
!champ me

**Uses:**
champ - randomizes a champion from a role
add - adds a champion to your list of champions
remove - removes a champion from your list of champions
list - lists all the champions in the your list
role - lists all the roles
me - randomizes a champion from your list of champions""")
            elif usermessage[1] == "info" or usermessage[1] == "Info":
                    await channel.send("""Use Champ to randomize a champ or add champs
to your list to randomize

**Syntax:**
!info
!info (summonername)
!info mastery (summonername)

**Uses:**
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
        filename = ("Userdata/" + str(author) + ".txt")
        if len(usermessage) == 2:
            if usermessage[1] == "me":
                champcheckandfile(filename)
                prevdata = [x.strip() for x in open(filename).readlines()]
                await channel.send(random.choice(prevdata))
            elif usermessage[1] == "list":
                champcheckandfile(filename)
                prevdata = [x.strip() for x in open(filename).readlines()]
                info_bot_message = "**" + str(author) + "**'s list \n"
                for i in prevdata:
                    info_bot_message += "- " + i + "\n"
                await channel.send(info_bot_message)
            elif usermessage[1] == "roles":
                await channel.send(role_error)
            # Add remove and create list of different users profile lists
            elif usermessage[1] == "all" or usermessage[1] == "All":
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
        if len(usermessage) == 3:
            if usermessage[1] == "add":
                # Check if it is a real champion
                if not (usermessage[2] in allchamps):
                    await channel.send("""Sorry that is not a Champion try again, check your spelling 
https://pastebin.com/SfjEx9Dv""")
                    return
                # Create file and write
                champcheckandfile(filename)
                prevdata = [x.strip() for x in open(filename).readlines()]
                if usermessage[2] in prevdata:
                    await channel.send("Sorry, **" + usermessage[2] + "** was already in your champ list")
                    return
                typeuserlist = open(filename, "w")
                await channel.send("**" + usermessage[2] + "** has successfully added to your list, Try !Champ list to see all your champs")
                for Info in prevdata:
                    typeuserlist.write(str(Info) + "\n")
                typeuserlist.write(usermessage[2] + "\n")
                typeuserlist.close()
            if usermessage[1] == "remove":
                # Check if it is a real champion
                if not (usermessage[2] in allchamps):
                    await channel.send("""Sorry that is not a Champion try again, check your spelling 
https://pastebin.com/SfjEx9Dv""")
                    return
                # Remove Champion
                champcheckandfile(filename)
                prevdata = [x.strip() for x in open(filename).readlines()]
                prevdata.remove(usermessage[2])
                typeuserlist = open(filename, "w")
                for Info in prevdata:
                    typeuserlist.write(str(Info) + "\n")
                typeuserlist.close()
                await channel.send("**" + usermessage[2] + "** has successfully been removed from your list, Try !Champ list to see all your champs")

    # Respond to !Info need Riot API
    if message.content.startswith("!info") or message.content.startswith("!Info"):
        summonerlength = len(usermessage)
        if summonerlength == 1:
            await channel.send("""**Syntax:**
!info
!info (summonername)
!info mastery (summonername)""")
        info_bot_message = ""
        if usermessage[1] == "mastery":
            # Make sure the link works
            username = str(usermessage[2])
            for i in usermessage[3:]:
                username += "%20" + str(i)
            # Retrieve mastery
            try:
                summonerdata = requestSummonerData(username, riot_api_key)
                summonerid = (summonerdata.get("id"))
                summonermastery = requestSummonerMastery(summonerid, riot_api_key)
                champs = []
                for i in range(3):
                    Champid = summonermastery[i].get("championId")
                    Champlevel = summonermastery[i].get("championLevel")
                    Champpoints = summonermastery[i].get("championPoints")
                    champs.append(dbrf.findchamp(Champid))
                    champs.append(Champlevel)
                    champs.append(Champpoints)
                for i in range(0, 7, 3):
                    info_bot_message += "\nChampion: " + str(champs[i]) + "\nMastery Level: " + str(champs[i+1]) + "\nMastery Points: "+ str(champs[i+2]) + "\n"
            except IndexError:
                info_bot_message = "No entry found, Maybe it was spelt wrong? or not at least 3 played champions"
        else:
            try:
                username = str(usermessage[1])
                for i in usermessage[2:]:
                    username += "%20" + str(i)
                summonerdata = requestSummonerData(username, riot_api_key)
                summonerid = (summonerdata.get("id"))
                summonerrank = requestSummonerRank(summonerid, riot_api_key)
                # Create Message
                info_bot_message = ""
                for x in summonerrank:
                    if x.get("queueType") == "RANKED_SOLO_5x5":
                        wins = x.get("wins")
                        losses = x.get("losses")
                        info_bot_message += "**Ranked Solo:** \n" + x.get("tier") + " " + x.get(
                            "rank") + "\n" + str(x.get("leaguePoints")) + " LP" + "\nWinrate: " + \
                             str(round(wins/(wins+losses)*100, 1)) + "%\n" + "Wins: " + str(wins) + "\nLosses: " + \
                             str(losses) + "\n"
                for x in summonerrank:
                    if x.get("queueType") == "RANKED_FLEX_SR":
                        wins = x.get("wins")
                        losses = x.get("losses")
                        info_bot_message += "\n**Ranked Flex: **\n" + x.get("tier") + " " + x.get(
                            "rank") + "\n" + str(x.get("leaguePoints")) + " LP" + "\nWinrate: " + \
                             str(round(wins/(wins+losses)*100, 1)) + "%\n" + "Wins: " + str(wins) + "\nLosses: " + str(losses)
                if info_bot_message == "":
                    info_bot_message = "Account not found, \nplease try again"
            except TypeError:
                info_bot_message = "Account not found, \nplease try again"
        await channel.send(info_bot_message)
        # Retrieve data about account

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
