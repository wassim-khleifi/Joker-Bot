import discord
from discord.ext import commands
########### IMPORT CONFIGS ##############
import config
from config import *

bot = commands.Bot(command_prefix= prefix, intents=discord.Intents.all(), help_command=None)
class Ban(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	@commands.command(name="ban",pass_context=True)
	@commands.has_permissions(ban_members=True)
	async def ban(self,ctx , user: discord.Member=None , * , reason="No Reason"):
		if user == None:
			await ctx.reply("Please Mention A Member To Ban!")
		elif ctx.message.author.guild_permissions.ban_members:
			await user.kick(reason=reason)
			embed= discord.Embed(color=discord.Color.red() , title ="Member Kicked!")
			embed.add_field(name="Alert ! :" , value=f"""
The User ** {user}** Has Been Banned
Reason = ** {reason}** """)
			await ctx.reply(embed=embed)
