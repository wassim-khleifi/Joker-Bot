import discord
from discord.http import handle_message_parameters
from discord.ext import commands,tasks
from discord import File , ButtonStyle
from discord.ui import Button , View
import os , random , youtube_dl , datetime , asyncio , json
import random
from random import choice
from dotenv import load_dotenv
########### IMPORT CONFIGS ##############
import config
from config import *
################################
########### BOT INTENTS AND PREFIX ##############
bot = commands.Bot(command_prefix= prefix, intents=discord.Intents.all())
################################
############## EMBEDS COLORS #################
THEME_COLOUR = discord.Colour.random()
embed_color = discord.Colour.random()
#################################
######### IMPORT COMMANDS #######
import help
from help import *
import moderation
from moderation.ban import *
from moderation.kick import *
from moderation.clear import *
import information
from information.ping import *
from information.server import *
from information.serverlist import *
from information.support import *
import events
from events.darkweb import *
from events.giveaway import *
from events.numbers import *
import economy
from economy.system import *
from economy.shop import *
import ticket_system
from ticket_system.system import *
bot.remove_command('help')
bot.add_command(help)
################################
bot.add_command(support)
bot.add_command(server)
bot.add_command(ping)
################################
bot.remove_command('number')
bot.add_command(number)
bot.add_command(giveaway)
bot.add_command(darkweb)
################################
bot.add_command(kick)
bot.add_command(clear)
bot.add_command(ban)
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
bot.remove_command('tcreate')
bot.add_command(tcreate)
bot.remove_command('tclose')
bot.add_command(tclose)
bot.remove_command('tsetadmin')
bot.add_command(tsetadmin)
bot.remove_command('tservice')
bot.add_command(tservice)
bot.remove_command('tsetrole')
bot.add_command(tsetrole)
#bot.add_command(box)
############# BOT STATUS ###############
@bot.event
async def on_ready():
	await bot.change_presence(status=discord.Status.dnd , activity=discord.Game('DEVELOPER CLOWN IS STILL WORKING ON BOT'))
	print("bot is ready!")
bot.run(token)