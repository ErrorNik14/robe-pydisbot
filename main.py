import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='c?', intents = intents, case_insensitive=True)
bot.remove_command('help')

@bot.event
async def on_connect():
    await bot.change_presence(status=nextcord.Status.online, activity=nextcord.Activity(type=nextcord.ActivityType.playing, name="c?help"))
    print("Bot activated")


@bot.command()
async def say(ctx, *cont):
    msg = ""
    for i in cont:
        msg = msg + " " + i
    await ctx.message.delete()
    await ctx.send(msg)

    

print("hi")

print("ok nob")


bot.run("OTQ2NDA2OTA5NDc1NDMwNDQx.YheQHg.aIzKzywJrI2LuR6r12z7SYFrNb0")
