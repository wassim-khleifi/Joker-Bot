import discord
from discord.ext import commands
import datetime
import random
import config
from config import *
import json
import economy
bot = commands.Bot(command_prefix= prefix, case_insensitive=True  , intents=discord.Intents.all(), help_command=None)
class Server_Eco(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	@commands.command(aliases=['sv_coins'])
	async def server_coins(self,ctx):
		await open_bank(ctx.author.guild)
		guild = ctx.author.guild
		guilds = await get_bank_data()
		wallet_amt = ("%.2f" % (guilds[str(guild.id)]["coins"]))
		boost_amt = int((guilds[str(guild.id)]["boosts"]))
		em = discord.Embed(title=f'**__{ctx.author.guild.name} Coins__**',color = discord.Color.random())
		em.add_field(name="**Server Coins 🪙**", value=f"`{wallet_amt}`")
		em.add_field(name="**Server Boosts 🚀**", value=f"`{boost_amt}`")
		await ctx.send(embed= em)
	@commands.Cog.listener()
	async def on_message(self,ctx):
		guild = ctx.author.guild
		guilds = await get_bank_data()
		earnings = 0.0005
		guilds[str(guild.id)]["coins"] += earnings
		with open("servers_bank.json",'w') as f:
			json.dump(guilds,f)
	@commands.command(aliases=['svs_shop'])
	async def servers_shop(self,ctx):
		shop_em = discord.Embed(title="**__Shop__**",description="**1 Boost 🚀 = ``100 Coins``**")
		await ctx.reply(embed=shop_em)
	@commands.command()
	async def buy_item(self,ctx,item: str=None):
		if item == None:
			await ctx.reply("Please Write The Item Name!")
		elif item == "boost":
			guild = ctx.author.guild
			guilds = await get_bank_data()
			if guilds[str(guild.id)]["coins"] > 100:
				guild = ctx.author.guild
				guilds = await get_bank_data()
				guilds[str(guild.id)]["boosts"] += 1
				guilds[str(guild.id)]["coins"] -= 100
				boost_em = discord.Embed(title="Annoucement!",description=f"**Admin {ctx.author.mention} Bought ``1`` Nitro!**",color=discord.Colour.green())
				boost_em.set_image(url="https://i.pinimg.com/originals/74/5f/d3/745fd3d279f7c5f27dc4e12fd583e68f.gif")
				await ctx.reply(embed=boost_em)
				with open("servers_bank.json",'w') as f:
					json.dump(guilds,f)
			else:
				await ctx.reply("You Dont Have Enough Coins!")
	@commands.command(aliases=['give_sv'])
	@commands.is_owner()
	async def addcoins_sv(self,ctx,amount : int=None):
		if amount==None:
			await ctx.reply("Please Enter Amount")
		else:
			sv = ctx.author.guild
			guild = sv
			guilds = await get_bank_data()
			bg = discord.Embed(title=f"**ALERT !**" , description=f"""
Owner {ctx.author.mention} Donated `{amount}` to {ctx.author.guild.name}""" , color = discord.Colour.random())
			await ctx.reply(embed=bg)
			guilds[str(guild.id)]["coins"] += amount
			with open("servers_bank.json",'w') as f:
				json.dump(guilds,f)
#######################################################################################



async def get_bank_data():
	with open('servers_bank.json','r') as f:
		guilds = json.load(f)
		return guilds
async def open_bank(guild):
	guilds = await get_bank_data()
	if str(guild.id) in guilds:
		return False
	else:
		guilds[str(guild.id)] = {}
		guilds[str(guild.id)]["coins"] = 0
		guilds[str(guild.id)]["boosts"] = 0
		with open('servers_bank.json','w') as f:
			json.dump(guilds,f)
			return True
