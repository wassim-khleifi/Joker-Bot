import discord
from discord.ext import commands
########### IMPORT CONFIGS ##############
import config
from config import *

bot = commands.Bot(command_prefix= prefix, intents=discord.Intents.all(), help_command=None)
THEME_COLOUR = discord.Colour.blurple()
EVENTS_COLOR = discord.Colour.blurple()
INFO_COLOR = discord.Colour.blurple()
MOD_COLOR = discord.Colour.blurple()
ERROR_COLOUR = discord.Colour.red()

@bot.command()
@commands.has_permissions(kick_members=True)
async def ban(ctx , user: discord.Member , * , reason="No Reason"):
	await user.ban(reason=reason)
	embed= discord.Embed(color=discord.Color.red() , title ="Member Banned!")
	embed.add_field(name="Alert ! :" , value=f"""
The User ** {user}** Has Been Banned
Reason = ** {reason}** """)
	await ctx.reply(embed=embed)
