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

@bot.command(pass_context=True)
async def darkweb(ctx):
	user = random.choice(ctx.guild.members)
	dark = ["Drugs" , "nothing", "Red Room" , "Blood" , "Killer" , "Hacker" , "mysterybox"]
	choice = random.choice(dark)
	embed = discord.Embed(title="Dark Web § :" , description=f"""
**Dark Web Council** :
Member {user.mention} Have To Check A Dark Web Website To Buy {choice}
""" , colour= EVENTS_COLOR)
	embed.set_image(url="https://media.discordapp.net/attachments/1059151958570713098/1065309806879068342/standard_7.gif?width=738&height=415")
	await ctx.reply (embed=embed)
	
	if choice == "Hacker":
	    embed = discord.Embed(title="RIP" , description=f"""
**RIP** :
Member {user.mention} Has Been Hacked !
""" , colour= EVENTS_COLOR)
	    await ctx.reply(embed=embed)
	elif choice == "Killer":
		embed = discord.Embed(title="RIP" , description=f"""
**RIP** :
Member {user.mention} Has Been Killed !
""" , colour= EVENTS_COLOR)
		await ctx.reply(embed=embed)

	elif choice == "Blood":
		embed = discord.Embed(title="RIP" , description=f"""
**RIP** :
OH SHIT THE BLOOD IS CONTAMINATED
Member {user.mention} Has Been Killed !
""" , colour= EVENTS_COLOR)
		await ctx.reply(embed=embed)

	elif choice == "Drugs":
		embed = discord.Embed(title="ALERT ! :" , description=f"""
**NEWS OF THE WEEK :** :
OH SHIT THE BLOOD IS CONTAMINATED
Member {user.mention} Has Been Arrested !
""" , colour= EVENTS_COLOR)
		await ctx.reply(embed=embed)

	elif choice == "mysterybox":
		embed = discord.Embed(title="RIP" , description=f"""
**RIP** :
Member {user.mention} Found A Bomb In The Box !
Member {user.mention} Has Been Killed !
""" , colour= EVENTS_COLOR)
		await ctx.reply(embed=embed)

	elif choice == "mysterybox":
		embed = discord.Embed(title="RIP" , description=f"""
**RIP** :
Member {user.mention} Has A Weak Heart :C
Member {user.mention} Is Died!
""" , colour= EVENTS_COLOR)
		await ctx.reply(embed=embed)

