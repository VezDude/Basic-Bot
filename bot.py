#Tutorial Bot by Code Part-1
#updated bot source code

import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def hi(ctx):
    await ctx.send(f'Hi {ctx.author.mention}')
    
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong ! {round(client.latency * 1000)}')

client.run('YOUR_TOKEN_HERE')
