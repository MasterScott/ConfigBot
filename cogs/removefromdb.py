import discord
from discord.ext import commands
import os
from cogs.database.db import Base, Configs
from cogs.database.database import session

class remove(commands.Cog):
	def __init__(self,bot):
		self.bot = bot
		
	def allowed():
		def predicate(ctx):
			return ctx.guild.id == <Server ID>
		return commands.check(predicate)
		
	@commands.command(pass_context=True)
	@commands.has_role("Config Maker")
	@commands.guild_only()
	@allowed()
	async def remove(self,ctx,arg):
		lwrcase = arg.lower()
		if ".loli" in lwrcase:
			lwrarg = lwrcase
		else:
			lwrarg = str(arg.lower())+".loli"
		name = session.query(Configs).filter(Configs.name == lwrarg).first()
		session.delete(name)
		session.commit()
		
		self.bot.reload_extension("cogs.request")
		self.bot.reload_extension("cogs.upload")
		self.bot.reload_extension("cogs.download")
		self.bot.reload_extension("cogs.view")
		self.bot.reload_extension("cogs.delete")
		self.bot.reload_extension("cogs.search")
		await ctx.send("Database reloaded successfully")
def setup(bot):
	bot.add_cog(remove(bot))