import discord
from discord.ext import commands
import random , datetime , asyncio
########### IMPORT CONFIGS ##############
import config
from config import *

bot = commands.Bot(command_prefix= prefix, intents=discord.Intents.all(), help_command=None)

THEME_COLOUR = discord.Colour.random()
EVENTS_COLOR = discord.Colour.random()
INFO_COLOR = discord.Colour.blurple()
MOD_COLOR = discord.Colour.blurple()
ERROR_COLOUR = discord.Colour.red()
@bot.command()
async def giveaway(ctx, mins : int , * , prize: str):
	embed = discord.Embed(title="**Giveaway! 🎉 **:", description=f"**Prize : {prize}**" , color= discord.Colour.random())
	end = datetime.datetime.utcnow() + datetime.timedelta(seconds = mins*60)
	embed.add_field(name = "```Ends At:```",value= f"```{end} UTC```")
	embed.set_footer(text=f"Ends After {mins} Mins From Now")
	my_msg = await ctx.send(embed = embed)
	await my_msg.add_reaction("⏰")
	await asyncio.sleep(mins * 60)
	new_msg = await ctx.channel.fetch_message(my_msg.id)
	import random
	user = random.choice(ctx.guild.members)
	emb = discord.Embed(title="Winner! 🎉 : " , description=f"**Congratulations! {user.mention} Won {prize}**" , color = discord.Colour.random())
	await ctx.send(embed=emb)
