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
    await ctx.send(f'Pong ! {round(client.latency * 100)}')
    
@client.command()
async def embed(ctx):
    embed = discord.Embed(title = "Embed", description = "This Message was sent using embed", color = 0x0062ff)
    embed.add_field(name = "This is field 1", value = "This is field description", inline=False)
    embed.add_field(name = "This is field 2", value = "This is field description", inline=False)
    embed.set_footer(text = "#Code Part-1 :)")
    await ctx.send(embed = embed)
    


client.run('YOUR_TOKEN_HERE')
