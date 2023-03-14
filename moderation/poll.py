import discord
from discord.ext import commands
########### IMPORT CONFIGS ##############
import config
from config import *

bot = commands.Bot(command_prefix= prefix, intents=discord.Intents.all(), help_command=None)

class Poll(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	@commands.command(name="poll")
	@commands.has_permissions(administrator=True)
	async def poll(self,ctx,*, poll=None):
		if poll == None:
			await ctx.send("Please send a message to make a poll please.")
		else:
			owner =  ctx.message.author.display_name
			poll_embed = discord.Embed(title="***__Poll Message__***", description=f"""
```yaml
 {poll}
```
***__Owner__***
```yaml
{owner}
```""", color=THEME_COLOUR)
			poll_embed.set_image(url=POLL_EMBED)
			em = await ctx.send(embed=poll_embed)
			await em.add_reaction('✅')
			await em.add_reaction('❌')
