print(
	"""
	moo 1.0.0
	Copyright (c) 2021 c:/#4617
	Licensed under the GNU AGPL 3.0
	"""
)
#imports
import discord
import time
import random
from discord.ext import commands

#bunch of things to include to make the code run
client = commands.Bot(command_prefix = ["c;"])

#message to send when running
@client.event
async def on_ready():
	print("Connected to Discord at " + time.ctime())
	perms = discord.Permissions(3072)
	print("Invite link: {}".format(discord.utils.oauth_url(client.user.id, perms)))
	#activity
	await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="grass grow"))
	print('')
	print(':::')
	print('')

#bunch of variables
ping_responses = [
	'stop',
	'stap',
	'really?',
	'can you not?',
	'bruh wth',
	'i will kick you'
	]
cow = [
	'cow',
	'moo',
	'milk',
	'black',
	'white',
	'dairy',
	'cream',
	'butter',
	'🐄',
	'🐮'
	]

#a function to listen to sent messages
@client.listen('on_message')
async def idk(message):
	#ignores the msg if its sent by a bot, so that there isnt an infinite loop of messages
	if message.author == client.user:
		return

	msg = message.content.lower()

	if client.user.mentioned_in(message):
		time.sleep(1.5)
		await message.channel.send(random.choice(ping_responses))
	
	if any(word in message.content for word in cow):
		await message.channel.send('moo')

#replace TOKEN with your token
client.run('TOKEN')
