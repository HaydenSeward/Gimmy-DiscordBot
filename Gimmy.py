from discord.ext import commands
from os import environ
from boto.s3.connection import S3Connection

TOKEN = S3Connection(os.environ["TOKEN"])
bot = commands.Bot(command_prefix = "!")



@bot.command()
async def test(ctx):
    f = open("UserData", "w")
    f.write("Test")
    f.close()
    await ctx.send('Maybe {0}'.format(ctx.author))

@bot.command()
async def Hope(ctx):
    ctx.send("AT LEASE THIS WORKS")

bot.run(TOKEN)
