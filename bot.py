import discord
from keep_alive import keep_alive
from discord.ext import commands
import random
import asyncio
import aiohttp
import requests
import reddit


client = commands.Bot(command_prefix = 'idk ')




client.remove_command('help')

class MyHelpCommand(commands.MinimalHelpCommand):
    def get_command_signature(self, command):
        return '{0.clean_prefix}{1.qualified_name} {1.signature}'.format(self, command)

class MyCog(commands.Cog):
    def __init__(self, bot):
        self._original_help_command = bot.help_command
        bot.help_command = MyHelpCommand()
        bot.help_command.cog = self

    def cog_unload(self):
        self.bot.help_command = self._original_help_command



@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game('idk help'))
  print("bot is ready")

  

@client.command()
async def hello(ctx):
  await ctx.send('Hi !!')

@client.command()
async def hi(ctx):
  await ctx.send('Hi !!')

@client.command()
async def Hi(ctx):
  await ctx.send('Hi !!')

@client.command()
async def Hello(ctx):
  await ctx.send('Hi !')

@client.command()
async def what(ctx):
  await ctx.send('Nothing')

@client.command()
async def What(ctx):
  await ctx.send('Nothing....')


@client.command()
async def yo(ctx):
  await ctx.send('Yo !')

@client.command()
async def Yo(ctx):
  await ctx.send('Yo !')

@client.command()
async def wbu(ctx):
  await ctx.send('I am Fine hbu ?')

@client.command()
async def Fine(ctx):
  await ctx.send('Nice !')

@client.command()
async def fine(ctx):
  await ctx.send('Nice !')



@client.command()
async def minecraft(ctx):
  await ctx.send("Let's Play Minecraft ⛏️!")

@client.command()
async def roblox(ctx):
  await ctx.send("Let's Play Roblox :spy: !")

@client.command()
async def gta5(ctx):
  await ctx.send("Let's Play GTA 5 :gun: !")

@client.command()
async def granny(ctx):
  await ctx.send("Let's Play Granny :bat: !")

@client.command()
async def SARANSH(ctx):
  await ctx.send("He Sucks !")

@client.command()
async def Ranger(ctx):
  await ctx.send("He Sucks !")

@client.command()
async def NABH(ctx):
  await ctx.send("He Sucks !")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')

@client.command()
async def run(ctx):
  await ctx.send(f':man_running: I am Running.......')

@client.command()
async def dance(ctx):
  await ctx.send(':dancer: I am Dancing.......')


@client.command()
async def kill(ctx, member: discord.Member):  # This command will be named kill and will take two arguments: ctx (which is always needed) and the user that was mentioned
    kill_messages = [
        f'{ctx.message.author.mention} killed {member.mention} with a frying pan',
        f'{ctx.message.author.mention} killed {member.mention} with super punch on his face',
        f'{ctx.message.author.mention} killed {member.mention} with a nuclear missile',
        f'{member.mention} died from CORONA VIRUS ',
        f'{member.mention} accidently put an axe on his feet and he died',
        f'{member.mention} died from laughing :laughing:',
    ]  # This is where you will have your kill messages. Make sure to add the mentioning of the author (ctx.message.author.mention) and the member mentioning (member.mention) to it
    await ctx.send(random.choice(kill_messages))


@client.command()
async def slap(ctx, member: discord.Member):  # This command will be named kill and will take two arguments: ctx (which is always needed) and the user that was mentioned
    slap_messages = [
        f'{ctx.message.author.mention} slapped {member.mention} 1 times. He slapped {ctx.message.author.mention} in return',
        f'{ctx.message.author.mention} slapped {member.mention} 100 times. He will take revenge...',
        f'{ctx.message.author.mention} slapped {member.mention} 1000 times. He luckily Survived.....',
        f'{ctx.message.author.mention} slapped {member.mention} ♾️ times. He luckily Survived in ventilator.....',

    ]  # This is where you will have your kill messages. Make sure to add the mentioning of the author (ctx.message.author.mention) and the member mentioning (member.mention) to it
    await ctx.send(random.choice(slap_messages))

@commands.has_permissions(kick_members=True)
@client.command()
async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
        await user.kick(reason=reason)
        kick = discord.Embed(title=f"Kicked {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        await ctx.message.delete()
        await ctx.channel.send(embed=kick)
        await user.send(embed=kick)

@client.command()
async def help(ctx):
  embed = discord.Embed(title = "Help - KILLER MEMER", description = "**Tip : There is a Secret command find it out ! **")
  embed.add_field(name='ㅤ', value='**[Commands](https://www.google.com/)**')
  await ctx.send(embed=embed)

@client.command()
async def vaccinateot(ctx, member: discord.Member):
  await ctx.send(f'{ctx.message.author.mention} vaccinated {member.mention} He/She is now safe')

@client.command()
async def vaccinate(ctx):
  await ctx.send(f'Vaccinated {ctx.message.author.mention}. You are now safe.')

@client.command()
async def sub(ctx):
  await ctx.send(f"{ctx.message.author.mention}, Sub To The Bot Develpoer's Channel : https://bit.ly/3tE6WER ")

@client.command()
async def inviteme(ctx):
  await ctx.send('Here is the Link To Invite Me :smiley:  : https://bit.ly/3o3fHXH ')

@client.command(aliases = ["pfp", "pfp_pic"])
async def profile_pic(ctx, member: discord.User):
    if member == None:
        member == ctx.author

    embed = discord.Embed(title = f"Profile Picture of {member.display_name}", color = member.color)
    embed.set_image(url = member.avatar_url)
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Asked by {ctx.author.display_name}#{ctx.author.discriminator}")
    await ctx.send(embed=embed)

@client.command(aliases=['make_role'])
@commands.has_permissions(manage_roles=True) # Check if the user executing the command can manage roles
async def create_role(ctx, *, name):
	guild = ctx.guild
	await guild.create_role(name=name)
	await ctx.send(f'Role `{name}` has been created')


@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(ctx):
    possible_responses = [
        'Hell no',
        'Prolly not',
        'Idk bro',
        'Prolly',
        'Hell yeah my dude',
    ]
    await ctx.send(random.choice(possible_responses) + ", " + ctx.message.author.mention)

@client.command()
async def square(ctx, number):
    squared_value = int(number) * int(number)
    await ctx.send(str(number) + " squared is " + str(squared_value))


@client.command()
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + " Server Information",
        description='ㅤ',
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)


@client.command(pass_context=True)
async def meme(ctx):
    embed = discord.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)
      
player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@client.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")

@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the .tictactoe command.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.") 




keep_alive()
client.run('YOUR_TOKEN_HERE')
