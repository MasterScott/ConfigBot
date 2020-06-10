import discord
from discord.ext import commands
from os import listdir
from os.path import isfile
from os.path import isfile, join
import traceback

cogs_dir = "cogs"
configs = "cogs/configs"

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')
	await bot.change_presence(status=discord.Status.online,activity=discord.Activity(type=discord.ActivityType.playing,name="{Providing Configs!"))

@bot.event
async def on_command_error(ctx,error):
	await ctx.send("Something happened "+str(error))
	
if __name__ == "__main__":
	for extension in [f.replace('.py', '') for f in listdir(cogs_dir) if isfile(join(cogs_dir, f))]:
		try:
			bot.load_extension(cogs_dir + "." + extension)
		except Exception as e:
			print(f'Failed to load extension {extension}.')
			traceback.print_exc()

bot.run('Token_Here')
