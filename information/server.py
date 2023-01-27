import discord
from discord.ext import commands
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
async def server(ctx):
  membros = len(ctx.guild.members)
  cargos = len(ctx.guild.roles)
  x = discord.Embed(title='Server Information:' , colour= EVENTS_COLOR)
  x.add_field(name='Server Name :', value=ctx.guild.name, inline=False)
  x.add_field(name='Server ID:', value=ctx.guild.id, inline=False)
  x.add_field(name='Server Owner:', value=ctx.guild.owner.mention, inline=False)
  x.add_field(name='Server Created Time:', value=ctx.guild.created_at.strftime('Data: %d/%m/%Y Hora: %H:%M:%S %p'), inline=False)
  x.add_field(name='Members:', value=f'{membros}', inline=False)
  await ctx.send(embed=x)