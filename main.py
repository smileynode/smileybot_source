import discord
from discord.ext import commands
from webserver import keep_alive
import os

token = 'PUT_YOUR_DISCORD_BOT_TOKEN_HERE'
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
# Discord Presence Command
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name='Smiley Client'))

# Welcome Command
@client.event
async def on_member_join(member):
    guild = client.get_guild(PUT_YOUR_SERVER_ID_HERE)
    welcome_channel = guild.get_channel(PUT_YOUR_CHANNEL_ID_HERE)
    role = guild.get_role(PUT_YOUR_ROLE_ID_HERE)
    await member.add_roles(role)
    await welcome_channel.send(f'Welcome to the {guild.name} Discord, {member.mention}!')
    await member.send(f'We are glad to have you in the {guild.name} Discord Server, {member.name} !  :partying_face:')
 # Kick Command
@client.command()
async def kick(ctx, member : discord.Member, *, reason =None):
  await member.kick(reason=reason)
# Ban Command
@client.command()
async def ban(ctx, member : discord.Member, *, reason =None):
  await member.ban(reason=reason)
# Hello Command
@client.command()
async def on_message(message):
    if message.content == 'hi':
        await message.channel.send('Hello!')

keep_alive()
client.run(token)
