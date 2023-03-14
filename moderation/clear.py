import discord
from discord.ext import commands
import datetime
########### IMPORT CONFIGS ##############
import config
from config import *

bot = commands.Bot(command_prefix= prefix , intents=discord.Intents.all(), help_command=None)

THEME_COLOUR = discord.Colour.random()
EVENTS_COLOR = discord.Colour.blurple()
INFO_COLOR = discord.Colour.blurple()
MOD_COLOR = discord.Colour.blurple()
ERROR_COLOUR = discord.Colour.red()
class Clear(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	@commands.command(name="clear",pass_context=True)
	@commands.has_permissions(manage_messages=True)
	async def clear(self,ctx, n=0):
		if n <= 0:
			await ctx.send('Please Write The Numbers Of Messages You Want To Delete')
		else:
			await ctx.channel.purge(limit=int(n))
			x = discord.Embed(title='Alert ! :')
			x.add_field(name='Messages deleted:', value=f'{n}')
			x.set_author(name=ctx.author)
			x.timestamp = datetime.datetime.utcnow()
			await ctx.send(embed=x)