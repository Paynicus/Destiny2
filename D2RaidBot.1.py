import discord

from discord.ext.commands import Bot
from discord.ext import commands

prefix = "!"

client = commands.Bot(command_prefix=prefix)

@client.event
async def on_ready():
    print("D2 Raidbot online")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))

@client.command(pass_context=True)
async def texttest(cxt):
    await client.say("Test satisfactory.")

Raid1 = []
Raid2 = []

@client.command(pass_context=True)
async def commands(cxt):
    await client.say('!raidcheck')
    await client.say('!signupthursday <PlayerNameHere>')
    await client.say('!signupsunday <PlayerNameHere>')
    await client.say('!wipethursday')
    await client.say('!wipesunday')

@client.command(pass_context=True)
async def raidcheck(cxt):
    if len(Raid1) > 0:
        await client.say('Currently on the Thursday raid are as follows:')
        await client.say(Raid1)
    else:
        await client.say('NO ONE IS SIGNED UP FER THE THURSDAY RAID! OH NOES!')
    if len(Raid2) > 0:
        await client.say('Currently on the Sunday raid are as follows:')
        await client.say(Raid2)
    else:
        await client.say('Seriously? No one signed up the Sunday raid?!')

@client.command(pass_context=True)
async def signupthursday(cxt, args):
    await client.say('Adding ' + args + ' to the Thursday raid list')
    Raid1.append(args)
    await client.say(Raid1)
    return Raid1

@client.command(pass_context=True)
async def signupsunday(cxt, args):
    await client.say('Adding ' + args + ' to the Sunday raid list')
    Raid2.append(args)
    await client.say(Raid2)
    return Raid2

@client.command(pass_context=True)
async def wipethursday(cxt):
    await client.say('Thursday raid list be getting wiped... Back to front...')
    del Raid1[:]
    await client.say('Wipe complete. With Charmin Ultra...')
    return Raid1

@client.command(pass_context=True)
async def wipesunday(cxt):
    await client.say('Sunday raid list... Is gone-arrhea now. Good Job!')
    del Raid2[:]
    await client.say('Wipe complete. With 1 Ply... You know that hurt!')
    return Raid2

@client.command(pass_context=True)
async def supertopsecretcommand(cxt):
    await client.say('Paynicus is pretty much shit.')
    await client.say('Warning! D2 Raidbot malfunction!')
    await client.say('Commencing recovery and recalibration... Please wait...')
    await client.say('3')
    await client.say('2')
    await client.say('1')
    await client.say('Process Complete. Re-assessing request from memory...')
    await client.say('Paynicus is pretty THE much shit.')

client.run("MzcwMjk0MTMwNzU0MTkxMzYx.DMpaSA.xiBTC7A7G8QDn3yO_99zvybdsUY")
