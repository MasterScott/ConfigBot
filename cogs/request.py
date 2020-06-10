import discord
from discord.ext import commands
import os
import base64

loli = os.listdir("cogs/configs")
anom = os.listdir("cogs/configs")

loli = ([s.replace('.loli', '') for s in loli])
anom = ([s.replace('.anom', '') for s in anom])


class request(commands.Cog):
	def __init__(self,bot):
		self.bot = bot
		
		
	@commands.command(pass_context = True)
	@commands.guild_only()
	async def request(self,ctx):
		def check(m):
			return m.author == ctx.author
		await ctx.send("Enter name of config:")
		name = await self.bot.wait_for("message",check=check,timeout=60.0)
		if (name.content) in loli:
			await ctx.send("This config already exist,Use command !download <name> to get it")
		if (name.content) in anom:
			await ctx.send("This config already exist,Use command !download <name> to get it")
		else:
			await ctx.send("Enter website Link:")
			link = await self.bot.wait_for("message",check=check,timeout=60.0)
			await ctx.send("Does the site has Recaptcha or captcha,if yes which version?")
			captcha = await self.bot.wait_for("message",check=check,timeout=60.0)
			await ctx.send("Does the site require proxies?")
			proxy = await self.bot.wait_for("message",check=check,timeout=60.0)
			await ctx.send("What you want to capture?")
			capture = await self.bot.wait_for("message",check=check,timeout=60.0)
			await ctx.send("Enter valid account")
			acc = await self.bot.wait_for("message",check=check,timeout=60.0)
			encode = base64.b64encode(acc.content.encode("utf-8"))
			account = str(encode,"utf-8")
			await ctx.send("Your request is successfully submitted")
			Requested_by = ctx.message.author
			
			channel = self.bot.get_channel(<Request Channel ID>)
			embed = discord.Embed(title = "New Config Request", color=0xe91e63)
			
			embed.add_field(name="name",value=name.content , inline=True)
			embed.add_field(name="Link",value=link.content,inline=True)
			embed.add_field(name="Captcha",value=captcha.content,inline=True)
			embed.add_field(name="Proxy",value=proxy.content,inline =True)
			embed.add_field(name="Capture",value=capture.content,inline=True)
			embed.add_field(name="Valid Account",value=account,inline=True)	
			embed.set_footer(text="Requested by "+str(Requested_by))
			
			await channel.send(embed=embed)
		
def setup(bot):
	bot.add_cog(request(bot))