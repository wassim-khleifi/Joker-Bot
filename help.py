import discord
from discord.ext import commands
from discord import File , ButtonStyle,SelectOption
from discord.ui import Button , View , Select
########### IMPORT CONFIGS ##############
import config
from config import *

bot = commands.Bot(command_prefix= prefix, intents=discord.Intents.all(), help_command=None)
THEME_COLOUR = discord.Colour.random()
EVENTS_COLOR = discord.Colour.random()
INFO_COLOR = discord.Colour.blurple()
MOD_COLOR = discord.Colour.blurple()
ERROR_COLOUR = discord.Colour.red()
class Select(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="Moderation",emoji="⚙️",description="Display Moderation Commands"),
            discord.SelectOption(label="Ticket",emoji="🎫",description="Display Ticket Commands"),
            discord.SelectOption(label="Events",emoji="🎁",description="Display Events Commands"),
            discord.SelectOption(label="Information",emoji="ℹ️",description="Display Information Commands"),
            discord.SelectOption(label="Economy",emoji="💰",description="Display Economy Commands")
            ]
        super().__init__(placeholder="Select an option",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        main = embed = discord.Embed(title="Bot Commands ??" ,  description=f"""
Help Commands
""" , colour= EVENTS_COLOR)
        mod = discord.Embed(title="***Moderation Commands***", description=f"""
```yaml
> {prefix}ban
> {prefix}kick
> {prefix}clear```
""")
        events = discord.Embed(title="***Moderation Commands***", description=f"""
```yaml
> {prefix}darkweb
> {prefix}number
> {prefix}giveaway 'mins' 'prize'```
""")
        events.set_image(url="https://media.discordapp.net/attachments/1059151958570713098/1062780734915481670/standard_5.gif?width=738&height=415")
        information = discord.Embed(title="***Moderation Commands***", description=f"""
```yaml
> {prefix}ping
> {prefix}server
> {prefix}support```
""")
        information.set_image(url="https://media.discordapp.net/attachments/1059151958570713098/1062780735313952912/standard_6.gif?width=738&height=415")
        economy = discord.Embed(title="***Moderation Commands***", description=f"""
```yaml
> {prefix}balance
> {prefix}work
> {prefix}beg
> {prefix}deposit
> {prefix}withdraw
> {prefix}shop
> {prefix}bag
> {prefix}buy
> {prefix}sell```
""")
        ticket = discord.Embed(title="***Ticket Commands***", description=f"""
```yaml
> {prefix}tcreate 'reason'
> {prefix}tclose 'reason'
> {prefix}tsetadmin 
> {prefix}tsetmanager
> {prefix}tservice 'off/on'
> {prefix}setrole [@role (Ticket Manager Role)] [@role (Ticket Admin Role)]
```
""")
        if self.values[0] == "Moderation":
            await interaction.response.edit_message(embed=mod)
        elif self.values[0] == "Ticket":
            await interaction.response.edit_message(embed=ticket)
        elif self.values[0] == "Events":
            await interaction.response.edit_message(embed=events)
        elif self.values[0] == "Information":
            await interaction.response.edit_message(embed=information)
        elif self.values[0] == "Economy":
            await interaction.response.edit_message(embed=economy)

class SelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        invite = Button(label="Invite me" , url="https://discord.com/api/oauth2/authorize?client_id=1022850160201584681&permissions=8&redirect_uri=https%3A%2F%2Fdiscord.gg%2FHbxRqqraqz&response_type=code&scope=bot" , emoji="🤖")
        dv = Button(label="Source Code" , url="https://github.com/clown83848474" , emoji="🤡")
        super().__init__(timeout=timeout)
        self.add_item(Select())
        self.add_item(invite)
        self.add_item(dv)
@bot.command()
async def help(ctx):
	embed = discord.Embed(title="Help Menu" ,  description=f"""
** Basic Information **
>>> ```yaml
• Prefix: c!
• Owner : Clown
```
** Bot Source Code **
```yaml
• You Can Now Make This Bot Using Replit Or Any Other Code Editor!
• Click The Button Below To See The Source Code!
```
""" , colour= EVENTS_COLOR)
	embed.set_image(url="https://media.discordapp.net/attachments/1059151958570713098/1062413232809181304/standard_3.gif?width=738&height=415")
	invite = Button(label="Invite me" , url="https://discord.com/api/oauth2/authorize?client_id=1022850160201584681&permissions=8&redirect_uri=https%3A%2F%2Fdiscord.gg%2FHbxRqqraqz&response_type=code&scope=bot" , emoji="🤖")
	dv = Button(label="Developer" , url="https://github.com/clown83848474" , emoji="🤡")
	await ctx.send(embed=embed,view=SelectView())