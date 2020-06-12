from discord.ext import commands
from tabulate import tabulate
from cogs.database.db import Configs
from cogs.database.database import session

class searchconfig(commands.Cog):
	def __init__(self,bot):
		self.bot = bot
	def channel():
		def predicate(ctx):
			return ctx.channel.id == 686674676432502880
		return commands.check(predicate)

	@channel()
	@commands.command(pass_context=True)
	@commands.guild_only()
	async def search(self,ctx,arg):
		lwrcase= arg.lower()
		if ".loli" in lwrcase:
			lwrarg = lwrcase
		else:
			lwrarg = lwrcase + ".loli"
		try:
			if ".loli" not in lwrcase and len(lwrcase) > 1 :
				configs = session.query(Configs).filter(Configs.name.contains(lwrcase)).all()
				headers = ['Names']
				rows = [[c.name]for c in configs]
				table = tabulate(rows,headers,tablefmt = "github")
				await ctx.send("```\n"+table+"```")
			elif len(lwrcase) > 1 and ".loli" in lwrarg:
				configs = session.query(Configs).filter(Configs.name==lwrarg).first()
				info = [['Name',configs.name],['Captcha',configs.captcha],['Capture',configs.capture],['Proxies',configs.proxies],['Author',configs.author],['Uploaded by',configs.uploaded_by],["Wordlists",configs.wordlist1+"|"+configs.wordlist2]]
				await ctx.send("```\n"+tabulate(info,tablefmt="plain")+"```")
			elif len(lwrcase) == 1 and lwrcase != lwrarg:
				configs = session.query(Configs).filter(Configs.name.startswith(lwrcase)).all()
				headers = ['Names']
				rows = [[c.name]for c in configs]
				table = tabulate(rows,headers,tablefmt = "github")
				await ctx.send("```\n"+table+"```")
			if not configs:
				await ctx.send("Config not found")
				return
		except Exception as e:
			await ctx.send("Could not complete your request")
			print(e)		
		
def setup(bot):
	bot.add_cog(searchconfig(bot))
