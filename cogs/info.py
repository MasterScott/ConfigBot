import discord
from discord.ext import commands

class Info(commands.Cog):
	def __init__(self,bot):
		self.bot = bot
		
	@commands.command(pass_context=True)
	async def info(self,ctx):
		embed = discord.Embed(title='Bot Information',colour= discord.Colour.green())
		embed.add_field(name="Creator",value = "Mian#0001")
		embed.add_field(name="Special Thanks",value="LethalLuck#6698 for encouraging me to make the bot\nPure#9257 for helping and hosting the bot\nThanks to Sp00f for helping Revamp this bot.")
		embed.add_field(name="Made For",value="Made especially for anomaly discord server")
		embed.add_field(name="Donation",value="Donations are appreciated If you want to donate then btc address is\n1F7bi92kEPgiLhupkpzEeRYFndjVyQqyFn")
		await ctx.send(embed=embed)
		
def setup(bot):
	bot.add_cog(Info(bot))