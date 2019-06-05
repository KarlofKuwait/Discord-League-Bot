"""
Name: Password Manager
Made By: Mads Hermansen
Github: https://github.com/KarlofKuwait
Date: 05/06/2019
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
role_error = "Examples of usable roles are \n- all \n- top \n- jng \n- mid \n- adc \n- sup"
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

def findchamp(id):
    if id == 266:
        return "Aatrox"
    if id == 412:
        return "Thresh"
    if id == 23:
        return "Tryndamere"
    if id == 79:
        return "Gragas"
    if id == 69:
        return "Cassiopeia"
    if id == 136:
        return "Aurelion Sol"
    if id == 13:
        return "Ryze"
    if id == 78:
        return "Poppy"
    if id == 14:
        return "Sion"
    if id == 1:
        return "Annie"
    if id == 202:
        return "Jhin"
    if id == 43:
        return "Karma"
    if id == 111:
        return "Nautilus"
    if id == 240:
        return "Kled"
    if id == 99:
        return "Lux"
    if id == 103:
        return "Ahri"
    if id == 2:
        return "Olaf"
    if id == 112:
        return "Viktor"
    if id == 34:
        return "Anivia"
    if id == 27:
        return "Singed"
    if id == 86:
        return "Garen"
    if id == 127:
        return "Lissandra"
    if id == 57:
        return "Maokai"
    if id == 25:
        return "Morgana"
    if id == 28:
        return "Evelynn"
    if id == 105:
        return "Fizz"
    if id == 74:
        return "Heimerdinger"
    if id == 238:
        return "Zed"
    if id == 68:
        return "Rumble"
    if id == 82:
        return "Mordekaiser"
    if id == 37:
        return "Sona"
    if id == 96:
        return "Kog'Maw"
    if id == 55:
        return "Katarina"
    if id == 117:
        return "Lulu"
    if id == 22:
        return "Ashe"
    if id == 30:
        return "Karthus"
    if id == 12:
        return "Alistar"
    if id == 122:
        return "Darius"
    if id == 67:
        return "Vayne"
    if id == 110:
        return "Varus"
    if id == 77:
        return "Udyr"
    if id == 89:
        return "Leona"
    if id == 126:
        return "Jayce"
    if id == 134:
        return "Syndra"
    if id == 80:
        return "Pantheon"
    if id == 92:
        return "Riven"
    if id == 121:
        return "Kha'Zix"
    if id == 42:
        return "Corki"
    if id == 268:
        return "Azir"
    if id == 51:
        return "Caitlyn"
    if id == 76:
        return "Nidalee"
    if id == 85:
        return "Kennen"
    if id == 3:
        return "Galio"
    if id == 45:
        return "Veigar"
    if id == 432:
        return "Bard"
    if id == 150:
        return "Gnar"
    if id == 90:
        return "Malzahar"
    if id == 104:
        return "Graves"
    if id == 254:
        return "Vi"
    if id == 10:
        return "Kayle"
    if id == 39:
        return "Irelia"
    if id == 64:
        return "Lee Sin"
    if id == 420:
        return "Illaoi"
    if id == 60:
        return "Elise"
    if id == 106:
        return "Volibear"
    if id == 20:
        return "Nunu"
    if id == 4:
        return "Twisted Fate"
    if id == 24:
        return "Jax"
    if id == 102:
        return "Shyvana"
    if id == 429:
        return "Kalista"
    if id == 36:
        return "Dr. Mundo"
    if id == 427:
        return "Ivern"
    if id == 131:
        return "Diana"
    if id == 223:
        return "Tahm Kench"
    if id == 63:
        return "Brand"
    if id == 113:
        return "Sejuani"
    if id == 8:
        return "Vladimir"
    if id == 154:
        return "Zac"
    if id == 421:
        return "Rek'Sai"
    if id == 133:
        return "Quinn"
    if id == 84:
        return "Akali"
    if id == 163:
        return "Taliyah"
    if id == 18:
        return "Tristana"
    if id == 120:
        return "Hecarim"
    if id == 15:
        return "Sivir"
    if id == 236:
        return "Lucian"
    if id == 107:
        return "Rengar"
    if id == 19:
        return "Warwick"
    if id == 72:
        return "Skarner"
    if id == 54:
        return "Malphite"
    if id == 157:
        return "Yasuo"
    if id == 101:
        return "Xerath"
    if id == 17:
        return "Teemo"
    if id == 75:
        return "Nasus"
    if id == 58:
        return "Renekton"
    if id == 119:
        return "Draven"
    if id == 35:
        return "Shaco"
    if id == 50:
        return "Swain"
    if id == 91:
        return "Talon"
    if id == 40:
        return "Janna"
    if id == 115:
        return "Ziggs"
    if id == 245:
        return "Ekko"
    if id == 61:
        return "Orianna"
    if id == 114:
        return "Fiora"
    if id == 9:
        return "Fiddlesticks"
    if id == 31:
        return "Cho'Gath"
    if id == 33:
        return "Rammus"
    if id == 7:
        return "LeBlanc"
    if id == 16:
        return "Soraka"
    if id == 26:
        return "Zilean"
    if id == 56:
        return "Nocturne"
    if id == 222:
        return "Jinx"
    if id == 83:
        return "Yorick"
    if id == 6:
        return "Urgot"
    if id == 203:
        return "Kindred"
    if id == 21:
        return "Miss Fortune"
    if id == 62:
        return "Wukong"
    if id == 53:
        return "Blitzcrank"
    if id == 98:
        return "Shen"
    if id == 201:
        return "Braum"
    if id == 5:
        return "Xin Zhao"
    if id == 29:
        return "Twitch"
    if id == 11:
        return "Master Yi"
    if id == 44:
        return "Taric"
    if id == 32:
        return "Amumu"
    if id == 41:
        return "Gangplank"
    if id == 48:
        return "Trundle"
    if id == 38:
        return "Kassadin"
    if id == 161:
        return "Vel'Koz"
    if id == 143:
        return "Zyra"
    if id == 267:
        return "Nami"
    if id == 59:
        return "Jarvan IV"
    if id == 81:
        return "Ezreal"
    if id == 518:
        return "Neeko"
    if id == 350:
        return "Yuumi"
    if id == 517:
        return "Sylas"
    if id == 555:
        return "Pyke"
    if id == 145:
        return "Kai'sa"
    if id == 142:
        return "Zoe"
    if id == 516:
        return "Ornn"
    if id == 141:
        return "Kayn"
    if id == 497:
        return "Rakan"
    if id == 498:
        return "Xayah"
    if id == 164:
        return "Camille"
    if id == 427:
        return "Ivern"
    if id == 240:
        return "Kled"
    if id == 136:
        return "Aurelion Sol"
    if id == 202:
        return "Jhin"
    if id == 420:
        return "Illoai"

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
    if message.content.startswith("uwu") or message.content.startswith("rawr") or message.content.startswith("owo"):
        await channel.send("""​x3 nuzzles! pounces on you uwu you so warm (Ooo)
Couldn't help but notice your bulge from across the floor
Nuzzles yo' necky wecky-tilde murr-tilde hehe
Unzips yo baggy ass pants, oof baby you so musky
Take me home, pet me, ’n' make me yours and don't forget to stuff me!
See me wag my widdle baby tail all for your buldgy-wuldgy!
Kissies 'n' lickies yo neck
I hope daddy likies
Nuzzles 'n' wuzzles yo chest (yuh)
I be (yeah) gettin' thirsty
""")
    if message.content.startswith("nani"):
        await channel.send("​https://www.youtube.com/watch?v=dNQs_Bef_V8")
    if message.content.startswith("oof"):
        await channel.send("*Roblox death sound*")
    if message.content.startswith("i'm top status"):
        await channel.send("Well im dave")
    if message.content.startswith("hi") or message.content.startswith("hey"):
        await channel.send("whats up")
    if message.content.startswith("whats up") or message.content.startswith("Whats up"):
        await channel.send("the sky")

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
!champ roles
!champ add (champion)
!champ remove (champion)
!champ list
!champ me

Uses:
champ - randomizes a champion from a role
add - adds a champion to your list of champions
remove - removes a champion from your list of champions
list - lists all the champions in the your list
role - lists all the roles
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
        filename = ("Userdata/" + str(author) + ".txt")
        if len(usermessage) == 2:
            if usermessage[1] == "me":
                champcheckandfile(filename)
                prevdata = [x.strip() for x in open(filename).readlines()]
                await channel.send(random.choice(prevdata))
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
                    await channel.send("Sorry, " + usermessage[2] + " was already in your champ list")
                    return
                typeuserlist = open(filename, "w")
                await channel.send(usermessage[2] + " has successfully added to your list, Try !Champ list to see all your champs")
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
                await channel.send(
                    usermessage[2] + " has successfully been removed from your list, Try !Champ list to see all your champs")
            if usermessage[1] == "list":
                champcheckandfile(filename)
                prevdata = [x.strip() for x in open(filename).readlines()]
                info_bot_message = str(author) + "'s list \n"
                for i in prevdata:
                    info_bot_message += i + "\n"
                await channel.send(info_bot_message)

    # Respond to !Info need Riot API
    if message.content.startswith("!info") or message.content.startswith("!Info"):
        summonerlength = len(usermessage)
        if summonerlength == 1:
            await channel.send("""Syntax:
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
                    champs.append(findchamp(Champid))
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
                info_bot_message = usermessage[1] + "\n"
                for x in summonerrank:
                    if x.get("queueType") == "RANKED_SOLO_5x5":
                        info_bot_message += "Ranked Solo: \n" + x.get("tier") + " " + x.get(
                            "rank") + "\n" + str(x.get("leaguePoints")) + " LP"
                for x in summonerrank:
                    if x.get("queueType") == "RANKED_FLEX_SR":
                        info_bot_message += "\n\nRanked Flex: \n" + x.get("tier") + " " + x.get(
                            "rank") + "\n" + str(x.get("leaguePoints")) + " LP"
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
