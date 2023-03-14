import discord
from discord.http import handle_message_parameters
from discord.ext import commands,tasks
from discord import File , ButtonStyle
from discord.ui import Button , View
import os , random , youtube_dl , datetime , asyncio , json
import random
from random import choice
########### IMPORT CONFIGS ##############
import config
from config import *
################################
########### BOT INTENTS AND PREFIX ##############
bot = commands.Bot(command_prefix= prefix, intents=discord.Intents.all())
######### IMPORT COMMANDS #######
import help
from help import *
import moderation
from moderation.ban import *
from moderation.kick import *
from moderation.clear import *
from moderation.poll import *
import information
from information.ping import *
from information.server import *
from information.serverlist import *
from information.support import *
from information.vote import *
import events
from events.darkweb import *
from events.giveaway import *
from events.numbers import *
import economy
from economy.system import *
from economy.servers_system import *
from economy.shop import *
import ticket_system
from ticket_system.system import *
import music
from music.music import *
bot.remove_command('help')
bot.add_command(help)
################################
bot.add_command(support)
bot.add_command(server)
################################
bot.remove_command('number')
bot.add_command(number)
bot.add_command(giveaway)
bot.add_command(darkweb)
######################################
bot.remove_command('balance')
bot.add_command(balance)
bot.remove_command('work')
bot.add_command(work)
bot.remove_command('deposit')
bot.add_command(deposit)
bot.remove_command('withdraw')
bot.add_command(withdraw)
bot.remove_command('beg')
bot.add_command(beg)
bot.remove_command('shop')
bot.add_command(shop)
bot.remove_command('buy')
bot.add_command(buy)
bot.remove_command('sell')
bot.add_command(sell)
bot.add_command(richest)
#bot.remove_command()
#bot.add_command()
bot.remove_command('bag')
bot.add_command(bag)
bot.remove_command('addmoney')
bot.add_command(addmoney)
bot.remove_command('kill')
bot.add_command(kill)
#bot.add_command(server_coins)
##########################
@bot.command(name="reboot")
@commands.is_owner()
async def reboot(ctx):
    await ctx.reply("Rebooting...")
    await asyncio.sleep(5)
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title="Alert!", description="**Bot Rebooted!**", color=discord.Colour.red())
    await ctx.reply(embed=embed)
    os.system("break")
    os.system("python main.py")
############# BOT STATUS ###############
@bot.event
async def on_command_error(ctx,error):
	if isinstance(error,commands.errors.NotOwner):
		await ctx.reply("YOU ARE NOT A DEVELOPER")
	elif isinstance(error,commands.MissingPermissions):
		await ctx.reply("You Do Not Have Permissions To Use This Command!")
	elif isinstance(error, commands.CommandOnCooldown):
		timeremaining = str(datetime.timedelta(seconds = int(error.retry_after)))
		error_em = discord.Embed(title="CoolDown!", description=f"**Try again in ``{timeremaining}`` Hours/Minutes**", color = discord.Colour.red())
		await ctx.reply(embed=error_em)
@bot.event
async def on_ready():
	await bot.change_presence(status=discord.Status.online , activity=discord.Game(f'j!help | {len(bot.guilds)} Guilds'))
	await bot.add_cog(Music(bot))
	await bot.add_cog(Ping(bot))
	await bot.add_cog(Kick(bot))
	await bot.add_cog(Ban(bot))
	await bot.add_cog(Clear(bot))
	await bot.add_cog(Poll(bot))
	await bot.add_cog(Ticket(bot))
	await bot.add_cog(Server_Eco(bot))
	await bot.add_cog(Vote(bot))
	print("bot is ready!")
bot.run(token)
