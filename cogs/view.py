from discord.ext import commands
from cogs.database.db import Configs
from cogs.database.database import session
from discord.ext import buttons

class MyPaginator(buttons.Paginator):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

class viewconfigs(commands.Cog):
	def __init__(self,bot):
		self.bot= bot
		
#	def channel():
#		def predicate(ctx):
#			return ctx.channel.id == 612354326228107314
#			return ctx.channel.id == 588781109542912031
#		return commands.check(predicate)
	
	@commands.command(pass_context=True)
	@commands.guild_only()
#       @channel()
	async def configs(self,ctx):
		configs = session.query(Configs).order_by(Configs.name).all()
		rows = [[c.name]for c in configs]
		pagey = MyPaginator(title='List of configs', colour=0xc67862, embed=True, timeout=90, use_defaults=True, entries=rows, length=50, format='**')
		
		await pagey.start(ctx)
		
def setup(bot):
	bot.add_cog(viewconfigs(bot))
