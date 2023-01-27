import discord
from discord.ext import commands
########### IMPORT CONFIGS ##############
import config
from config import *
bot = commands.Bot(command_prefix= prefix, intents=discord.Intents.all(), help_command=None)

THEME_COLOUR = discord.Colour.random()
EVENTS_COLOR = discord.Colour.random()
INFO_COLOR = discord.Colour.blurple()
MOD_COLOR = discord.Colour.blurple()
ERROR_COLOUR = discord.Colour.red()
@bot.command(description="Shows the heartbeats of the bot")
async def ping(ctx):
   pingEm = discord.Embed(title=f"Ping Pong", description=f"Bot latency :  `{round(bot.latency * 1000)}ms` ", color=THEME_COLOUR)
   await ctx.reply(embed=pingEm)