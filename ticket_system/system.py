import discord
import datetime
from discord.ext import commands
import asyncio
from discord import File , ButtonStyle,SelectOption
from discord.ui import Button , View , Select
import random
########### IMPORT CONFIGS ##############
import config
from config import *

#Bot prefix
bot = commands.Bot(command_prefix= prefix, intents=discord.Intents.all())
# --- Variable ---
max_ticket_channel = 10
ticket_service = True
ticket_manager_role = None
ticket_admin_role = None

# ----- TICKET COMMANDS -----
class Ticket(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="tcreate",pass_context=True)
  @commands.has_permissions(administrator=True)
  async def tick(self,ctx,reason="Support"):
    #########################################################
    async def open_callback(interaction):
      overwrite={
      ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
      interaction.user:discord.PermissionOverwrite(send_messages=True,read_messages=True,read_message_history=True),
      ctx.author:discord.PermissionOverwrite(read_messages=True,send_messages=True,read_message_history=True),
      }
      guild =  ctx.message.guild
      ch = await guild.create_text_channel(name=f"Ticket-{random.randint(0,9999999999)}",overwrites=overwrite)
      time = datetime.datetime.utcnow()
      open_embed = discord.Embed(title="***__Ticket Opened!__***", description=f"""
***__Information__***
```yaml
> • Author : {interaction.user}
> • Reason : {reason}
> • Time : {time}
```
***__Usage__***
```yaml
> • Write 'j!close' To Close This Ticket (Admin Only)
> • Support Will Be Here SOON
> • Do Not Spam Tickets!
```
        """, color=THEME_COLOUR)
      open_embed.set_image(url=TICKET_EMBED)
      await ch.send(f"{interaction.user.mention}", embed=open_embed)
    #########################################################
    embed = discord.Embed(title="**Ticket System**", description=f"""
***__Usage__***
```yaml
> • Ticket Is Made For {reason}
```      
      """, color = THEME_COLOUR)
    embed.set_image(url=TICKET_EMBED)
    open = Button(label="Open",emoji="🎫",style=ButtonStyle.grey)
    open.callback = open_callback
    #########################################################
    myview = View(timeout=180)
    myview.add_item(open)
    await ctx.reply("Creating Your Ticket...")
    await asyncio.sleep(5)
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=embed,view=myview)


  @commands.command(name="tclose",pass_context=True)
  @commands.has_permissions(administrator=True)
  async def close(self,ctx):
    embed = discord.Embed(title="Closing Ticket!", description=f"{ctx.author.mention} **Are U Sure You Want To Close This Ticket?**", color = THEME_COLOUR)
    yes = Button(label="Yes",style=ButtonStyle.primary)
    no = Button(label="Cancel",style=ButtonStyle.danger)
    async def yes_callback(interaction):
      await interaction.channel.delete()
    async def no_callback(interaction):
      await ctx.reply("Canceled!")
    yes.callback = yes_callback
    no.callback = no_callback
    myview = View(timeout=180)
    myview.add_item(yes)
    myview.add_item(no)
    await ctx.reply(embed=embed,view=myview)