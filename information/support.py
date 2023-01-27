import discord
from discord.ext import commands
from discord import File , ButtonStyle
from discord.ui import Button , View
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
async def support(ctx):
    embed = discord.Embed(title="Bot Commands ??" ,  description="""
**Here Are Some Basic Information:**
```• Prefix: c!
• Owner: CLOWN#9899
```
**How Can I Ask For Support? :**
```• You Can Ask The Support By Joining The Evil Clowns Discord
Server
```
""" , colour= EVENTS_COLOR)
    embed.set_footer(text="welcome")
    embed.set_image(url="https://media.discordapp.net/attachments/1059151958570713098/1062413232809181304/standard_3.gif?width=738&height=415")
    invite = Button(label="Invite me" , url="https://discord.com/api/oauth2/authorize?client_id=1022850160201584681&permissions=8&redirect_uri=https%3A%2F%2Fdiscord.gg%2FHbxRqqraqz&response_type=code&scope=bot" , emoji="🤖")
    server = Button(label="Server Support" , url="https://discord.gg/HbxRqqraqz" , emoji="🤡")
    myview = View(timeout=180)
    myview.add_item(invite)
    myview.add_item(server)
    await ctx.reply(embed=embed , view=myview)