from discord.ext import commands


lineList = [line.rstrip('\n') for line in open("abuses/abuses.txt")]

class censor(commands.Cog):
	def __init__(self,bot):
		self.bot= bot
		
	@commands.command(pass_context=True)
	async def add(self,ctx,arg):
		await ctx.send("added")
		f = open("cogs\abuses\abuses.txt","a+")
		f.write(f"{arg}\n")
		with open("cogs\abuses/abuses.txt", "r") as f:
				lines = f.readlines()
		with open("cogs\abuses/abuses.txt", "w") as f:
			for line in lines:
				if line.strip("\n") != arg:
					f.write(line)
	
			
def setup(bot):
	bot.add_cog(censor(bot))
