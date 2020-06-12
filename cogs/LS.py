from discord.ext import commands
from discord.ext import buttons
import os

present_configs = os.listdir("cogs/configs")

class MyPaginator(buttons.Paginator):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
class viewLS(commands.Cog):
	def __init__(self,bot):
		self.bot= bot
		
	@commands.command(pass_context=True)
	@commands.guild_only()
	async def LS(self,ctx,arg):
		lwrcase = arg.lower()
		if "loli" in lwrcase:
			lwrarg = lwrcase
		elif "loli" not in lwrcase:
			lwrarg = lwrcase + ".loli"
		fp = f"cogs/configs/{lwrarg}"
		if lwrarg in present_configs:
			with open(fp) as f:
				read = f.readlines()
				
				pagey = MyPaginator(title='Loli Script', colour=0xc67862, embed=True, timeout=120, use_defaults=True, entries=read, length=20, format='**')
		
				await pagey.start(ctx)
		else:
			await ctx.send("Config not found")
	
def setup(bot):
	bot.add_cog(viewLS(bot))
