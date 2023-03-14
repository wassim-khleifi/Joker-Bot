from discord.ext import commands
from discord.ext.commands import has_permissions,MissingPermissions
########### IMPORT CONFIGS ##############
import config
from config import *

bot = commands.Bot(command_prefix= prefix , intents=discord.Intents.all(), help_command=None)

class Kick(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	@commands.command(name="kick",pass_context=True)
	@commands.has_permissions(kick_members=True)
	async def kick(self,ctx , user: discord.Member=None , * , reason="No Reason"):
		if user == None:
			await ctx.reply("Please Mention A Member To Kick!")
		elif ctx.message.author.guild_permissions.kick_members:
			await user.kick(reason=reason)
			embed= discord.Embed(color=discord.Color.red() , title ="Member Kicked!")
			embed.add_field(name="Alert ! :" , value=f"""
The User ** {user}** Has Been Kicked
Reason = ** {reason}** """)
			await ctx.reply(embed=embed)