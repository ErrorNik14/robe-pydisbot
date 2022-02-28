import nextcord
from nextcord.ext import commands
import os

intents = nextcord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='c?', intents = intents, case_insensitive=True)
bot.remove_command('help')

@bot.event
async def on_connect():
    await bot.change_presence(status=nextcord.Status.online, activity=nextcord.Activity(type=nextcord.ActivityType.playing, name="c?help"))
    print("Bot activated")

@bot.command()
async def bedwar(ctx):
    await ctx.send("am pro")


@bot.command()
async def say(ctx, *cont):
    msg = ""
    for i in cont:
        msg = msg + " " + i
    await ctx.message.delete()
    await ctx.send(msg)

    
bot.load_extension("Cogs.Economy")
bot.load_extension("Cogs.Fun")

bot.run(str(os.environ("TOKEN")))
#Replace the Run line with the bot token if you are testing it, but
#always change it back to bot.run(str(os.environ("TOKEN"))) before pull-requesting/commiting