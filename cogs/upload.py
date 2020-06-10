import discord
from discord.ext import commands
from cogs.database.db import Base, Configs
from cogs.database.database import session
import asyncio
from datetime import timedelta
import os
import json
import re

present_configs = os.listdir("cogs/configs")

class upload(commands.Cog):
	def __init__(self,bot):
		self.bot = bot
				
	@commands.command(pass_context = True)
	@commands.guild_only()
	async def upload(self,ctx,arg):
		lwrcase = arg.lower()
		list = str(lwrcase).split(",")
		for elem in list:
			attachments = ctx.message.attachments
			if not attachments:
				await ctx.send("No config file was attached")
				return
			else:
				if ".loli" in elem:
					lwrarg = elem
				else:
					lwrarg = str(elem)+".loli"
				if lwrarg in present_configs:
					await ctx.send("This config is already present")
				elif lwrarg in present_configs:
					await ctx.send("This config is already present")
				else:
					fp = (f"cogs/configs/{lwrarg}")
					for attachment in attachments:
						await attachment.save(fp)
						with open(fp, 'r') as f:
							file = f.read()
							endindex = file.find("\n\n[SCRIPT")
							f.close()
						with open(fp,'r')as input:
							data = input.read()[10:endindex]
							jsdata = json.loads(data)
							author = (jsdata["Author"])
							proxy = (jsdata["NeedsProxies"])
							wordlist1 = (jsdata["AllowedWordlist1"])
							wordlist2 = (jsdata["AllowedWordlist2"])
							input.close()
							with open(fp,"r")as file:
								jsondata = file.read().replace('\n', '')
								capture = re.findall(r'CAP "(.+?)"', jsondata)
						read = open(fp).readlines()
						if any("RECAPTCHA" in item for item in read):
							recaptcha = "True"
						else:
							recaptcha = "False"
					await ctx.send("Your config is successfully uploaded. Thank you for uploading.")
					await ctx.message.delete()
					uploaded_by = ctx.message.author
		
					configs = Configs(name=str(lwrarg),captcha = recaptcha,capture=str(capture),proxies=str(proxy),author=str(author),uploaded_by=str(uploaded_by),wordlist1=str(wordlist1),wordlist2=str(wordlist2),Location=fp)
					session.add(configs)
					session.commit()
					
		self.bot.reload_extension("cogs.request")
		self.bot.reload_extension("cogs.upload")
		self.bot.reload_extension("cogs.download")
		self.bot.reload_extension("cogs.view")
		self.bot.reload_extension("cogs.delete")
		self.bot.reload_extension("cogs.search")
		self.bot.reload_extension("cogs.info")
		self.bot.reload_extension("cogs.LS")
		await ctx.send("Reloaded database successfully.")
		
def setup(bot):
	bot.add_cog(upload(bot))
