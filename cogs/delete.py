import discord
from discord.ext import commands
import os
from cogs.database.db import Base, Configs
from cogs.database.database import session

present_configs = os.listdir("cogs/configs")
class delete(commands.Cog):
	def __init__(self,bot):
		self.bot = bot
		
	def allowed():
		def predicate(ctx):
			return ctx.guild.id == <Place Server ID Here>
		return commands.check(predicate)
		
	@commands.command(hidden = True)
	@commands.has_role("Config Moderator Role")
	@commands.guild_only()
	@allowed()
	async def delete(self,ctx,arg):
		lwrcase = arg.lower()
		if ".loli" in lwrcase:
			lwrarg = lwrcase
		else:
			lwrarg = str(arg.lower())+".loli"
		if lwrarg in present_configs:
			os.remove(f"cogs/configs/{lwrarg}")
			await ctx.send("Successfully deleted config")
			name = session.query(Configs).filter(Configs.name == lwrarg).first()
			session.delete(name)
			session.commit()
		else:
			await ctx.send("Config not deleted")
		self.bot.reload_extension("cogs.request")
		self.bot.reload_extension("cogs.upload")
		self.bot.reload_extension("cogs.download")
		self.bot.reload_extension("cogs.view")
		self.bot.reload_extension("cogs.delete")
		self.bot.reload_extension("cogs.search")
		await ctx.send("Database reloaded successfully.")
			
def setup(bot):
	bot.add_cog(delete(bot))
