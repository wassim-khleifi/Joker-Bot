import discord
from discord.ext import commands
import datetime
import time
import typing
########### IMPORT CONFIGS ##############
import config
from config import *
class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="ping")
    async def ping(self, ctx):
    	embed = discord.Embed(title="***__Bot Ping__***" , description=f"**Pong! 🏓 ** `{round(self.bot.latency * 1000)}` **ms**" , color=THEME_COLOUR)
    	await ctx.reply(embed=embed)