#Tutorial Bot by Code Part-1

import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def hi(ctx):
    await ctx.send(f'Hi {ctx.author.mention}')

client.run('YOUR_TOKEN_HERE')
