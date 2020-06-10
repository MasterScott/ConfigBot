import discord
from discord.ext import commands

class reload(commands.Cog):
	def __init__(self,bot):
		self.bot = bot
		
	@commands.command(hidden = True)
	@commands.guild_only()
	async def reload(self,ctx):
		try:
			self.bot.reload_extension("cogs.request")
			self.bot.reload_extension("cogs.upload")
			self.bot.reload_extension("cogs.download")
			self.bot.reload_extension("cogs.view")
			self.bot.reload_extension("cogs.delete")
			self.bot.reload_extension("cogs.search")
			self.bot.reload_extension("cogs.info")
			self.bot.reload_extension("cogs.LS")
					
		except commands.ExtensionError as e:
			await ctx.send(f'{e.__class__.__name__}: {e}')
		else:
			await ctx.send(f"Done\N{OK HAND SIGN}")
			
def setup(bot):
	bot.add_cog(reload(bot))