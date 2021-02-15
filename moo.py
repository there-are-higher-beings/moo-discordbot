print(
	"""
	moo 1.0.0
	Copyright (c) Jonathan Ford
	Licensed under the GNU AGPL 3.0
	"""
)

import discord
import time
import random
from discord.ext import commands
from keep_alive import keep_alive

client = commands.Bot(command_prefix = ["c;"])

@client.event
async def on_ready():
	print("Connected to Discord at " + time.ctime())
	perms = discord.Permissions(3072)
	print("Invite link: {}".format(discord.utils.oauth_url(client.user.id, perms)))

	'''
	#Setting `Playing ` status
	(name="a game")
	# Setting `Streaming ` status
	(name="My Stream", url=my_twitch_url)
	# Setting `Listening ` status
	(type=discord.ActivityType.listening, name="a song")
	# Setting `Watching ` status
	(type=discord.ActivityType.watching, name="a movie")
	'''

	await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="grass grow"))
	print('')
	print(':::')
	print('')


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
	'white'
	]

moo = [
	'',
	'',
	'',
	'',
	'moo'
	]

@client.listen('on_message')
async def idk(message):
	if message.author == client.user:
		return

	msg = message.content.lower()

	if msg == 'boing':
		await message.channel.send('boing')
		await message.channel.send('boing')
		await message.channel.send('boing')
		await message.channel.send('boing')
		await message.channel.send('boing')

	if client.user.mentioned_in(message):
		time.sleep(1.5)
		await message.channel.send(random.choice(ping_responses))
	
	if any(word in message.content for word in message.content):
		await message.channel.send(random.choice(moo))

keep_alive()
client.run('my token')
