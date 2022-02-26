import nextcord
from nextcord.ext import commands

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def test(self, ctx):
        await ctx.send("lol")
        

def setup(bot):
    bot.add_cog(Economy(bot))