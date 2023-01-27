###############################
import discord
from discord.ext import commands,tasks
import os , random
from dotenv import load_dotenv
import youtube_dl
import datetime
import asyncio
########### IMPORT CONFIGS ##############
import config
from config import *

###############################
bot = commands.Bot(command_prefix= prefix, intents=discord.Intents.all())
###############################
THEME_COLOUR = discord.Colour.random()
EVENTS_COLOR = discord.Colour.random()
INFO_COLOR = discord.Colour.blurple()
MOD_COLOR = discord.Colour.blurple()
ERROR_COLOUR = discord.Colour.red()

@bot.command(help = "Shows the Guild the bot is in")
async def serverlst(ctx):
	print("soon")