import os
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv
import discord


load_dotenv('TK.env')
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents().all()
get_prefix = "!"

bot = commands.Bot(command_prefix=get_prefix, intents=intents)


@bot.command()
async def Aliaz(ctx):
    aliaz = get(ctx.guild.members, name='Aliaz')
    await ctx.send(f'<@352037304816238592> is sucking your dick')


@bot.command()
async def Mati(ctx):
    mati = get(ctx.guild.members, name='Mati')
    await ctx.send(f'{mati.mention} simpi teraz że hej')


@bot.command()
async def Boss(ctx):
    boss = get(ctx.guild.members, name='Big Boss Man')
    await ctx.send(f'{boss.mention} SZYBKO BABA DZWONI')


@bot.command()
async def Moris(ctx):
    umr = get(ctx.guild.members, name='Moris')
    await ctx.send(f'{umr.mention} napierdala rankeda')


@bot.command()
async def Duck(ctx):
    await ctx.send(f'https://cdn.discordapp.com/attachments/981232034733228072/981514647779811359/duck.gif')


@bot.command()
async def Assemble(ctx):
    aliaz = get(ctx.guild.members, name='Aliaz')
    umr = get(ctx.guild.members, name='Moris')
    macin = get(ctx.guild.members, name='Big Boss Man')
    mati = get(ctx.guild.members, name='Mackobot')
    if(aliaz!=None and umr!=None and mati!=None and macin!=None):
        await ctx.send(f'https://tenor.com/view/captain-america-avengers-assemble-gif-22306281')
        await ctx.send(f'{aliaz.mention} '), await ctx.send(f'{umr.mention} '), await ctx.send(f'{macin.mention} '), \
        await ctx.send(f'{mati.mention} '), await ctx.send('ASSEMBLE!!!')
    else:
        await ctx.send(f'Nie ma wszystkich')


bot.run(TOKEN)
