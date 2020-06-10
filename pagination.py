from discord.ext import commands
from discord.ext import buttons


class MyPaginator(buttons.Paginator):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @buttons.button(emoji=u"\U0001F44D")
    async def record_button(self, ctx):
        await ctx.send('This button sends a silly message! But could be programmed to do much more.')

    @buttons.button(emoji=u"\U0001F44C")
    async def silly_button(self, ctx):
        await ctx.send('Beep boop...')


bot = commands.Bot(command_prefix='c!')


@bot.command()
async def test(ctx):
    pagey = MyPaginator(title='Silly Paginator', colour=0xc67862, embed=True, timeout=90, use_defaults=True,entries=[1, 2, 3], length=1, format='**')

    await pagey.start(ctx)


@bot.event
async def on_ready():
    print('Ready!')


bot.run('Token_Here')