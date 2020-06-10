import discord
from discord.ext import commands
import os
from tabulate import tabulate
from cogs.database.db import Base, Configs
from cogs.database.database import session

present_configs = os.listdir("cogs/configs")

class download(commands.Cog):
	def __init__(self,bot):
		self.bot = bot
	def channel():
		def predicate(ctx):
			return ctx.channel.id == <Channel ID>
		return commands.check(predicate)

	@channel()
	@commands.command(pass_context=True)
	@commands.guild_only()
	@commands.has_role("Config Permission Role")
	async def download(self,ctx,arg):
		lwrcase = arg.lower()
		list = str(lwrcase).split(",")
		for elem in list:
			if ".loli" in elem:
				lwrarg = elem
			else:
				lwrarg = str(elem)+".loli"
			try:
				configs = session.query(Configs).filter(Configs.name == lwrarg).first()
				if lwrarg not in present_configs:
					await ctx.send("Config not found, please request it !")
					return
				user = ctx.message.author
				info = [['Name',configs.name],['Captcha',configs.captcha],['Capture',configs.capture],['Proxies',configs.proxies],['Author',configs.author],['Uploaded by',configs.uploaded_by],["Wordlists",configs.wordlist1+"|"+configs.wordlist2]]
				file = discord.File(f"cogs/configs/{lwrarg}")
				await user.send("```\n"+tabulate(info)+"```",file=file)
			except Exception as e:
				await ctx.send("Could not complete your command.")
				print(e)
		await ctx.send("Sent you a DM containing the config.")
		
def setup(bot):
	bot.add_cog(download(bot))
