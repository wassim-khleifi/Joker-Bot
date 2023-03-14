import discord
from discord.ext import commands
from discord import File , ButtonStyle,SelectOption
from discord.ui import Button , View , Select
########### IMPORT CONFIGS ##############
import config
from config import *

bot = commands.Bot(command_prefix= prefix, intents=discord.Intents.all(), help_command=None)
class Vote(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	@commands.command(name="vote",pass_context=True)
	async def vote(self,ctx):
		vote_em = discord.Embed(title="**Voting**", description="""
***__Why Voting?__***
>>> ```yaml
Voting Us Will Grow Our Community And Members, That Will Ecourage Us To Make New Updates
```
			""", colour=THEME_COLOUR)
		topgg = Button(label="Topgg" , url="https://top.gg/bot/1022850160201584681" , emoji="🔗")
		botlist = Button(label="Botlist" , url="https://github.com/clown83848474" , emoji="🔗")
		myview = View(timeout=180)
		myview.add_item(topgg)
		myview.add_item(botlist)
		await ctx.reply(embed=vote_em,view=myview)
