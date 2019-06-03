import discord
import random, time
import requests, json

# Bot Info
bot_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
messages = ["Hello", "Oh hey there ;)", "Whats up", "Yo", "Waddup"]
champs = [x.strip() for x in open("Champlist.txt").readlines()]
# End

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
    # Respond to hehe
    if message.content.startswith("hehe") or message.content.startswith("Hehe"):
        await channel.send("oh you are an amazing person " + str(author))
    # Respond to !Help
    if message.content.startswith("!help") or message.content.startswith("!Help"):
        if len(usermessage) > 2:
            await channel.send("Please specify a working command")
        else:
            await channel.send("""Commands \n- Help \n- Champ \n- Info""")
    # Respond to !Champ
    if message.content.startswith("!champ") or message.content.startswith("!Champ"):
        if len(usermessage) > 2:
            await channel.send(
                "Please specify the role, examples are \n- all \n- top \n- jng \n- mid \n- adc \n- sup")
        try:
            if usermessage[1] == "all" or usermessage[1] == "All":
                await channel.send(random.choice(champs))
            else:
                await channel.send(
                    "Please specify the role, examples are \n- all \n- top \n- jng \n- mid \n- adc \n- sup")
        except IndexError:
            await channel.send(
                "Please specify the role, examples are \n- all \n- top \n- jng \n- mid \n- adc \n- sup")
    # Respond to !Info need Riot API
    if message.content.startswith("!info") or message.content.startswith("!Info"):
        await channel.send("Currently this command doesnt work, instead try !Champ")
    # Review the sent message (Will create log?)
    now = datetime.now()
    dt_string = now.strftime("[%d/%m/%Y:%H/%M/%S]")
    log = ("\n" + dt_string + str(author) + " sent \"" + str(message.content) + "\"")
    if createlog == True:
        # Create log
        pass
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
