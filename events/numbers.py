import discord
from discord.ext import commands
import random
########### IMPORT CONFIGS ##############
import config
from config import *
bot = commands.Bot(command_prefix= prefix, intents=discord.Intents.all(), help_command=None)
THEME_COLOUR = discord.Colour.random()
EVENTS_COLOR = discord.Colour.random()
INFO_COLOR = discord.Colour.blurple()
MOD_COLOR = discord.Colour.blurple()
ERROR_COLOUR = discord.Colour.red()
@bot.command()
async def number(ctx):
	embed = discord.Embed(title="Number Random Generator :" , description=f"""
Number Has Been Generated !
Number Is : `{int(random.randint(0 , 10))}`  """ , colour= EVENTS_COLOR)
	await ctx.reply (embed=embed)