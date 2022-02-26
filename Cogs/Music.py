import nextcord
from nextcord.ext import commands
import os
import wavelink

class Music(commands.Cog):
    def __init__(self, bot:nextcord.Client):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.loop.create_task(self.node_connect())
    
    @commands.Cog.listener()
    async def on_wavelink_node_ready(self, node:wavelink.Node):
        print(f"Node {node.identifier} is ready for VC commands!")

    async def node_connect(self):
        await self.bot.wait_until_ready()
        await wavelink.NodePool.create_node(bot=self.bot, host="lava.link", port=80, password="dismusic")

    @commands.command()
    async def play(self, ctx, *, search:wavelink.YouTubeTrack):
        if not ctx.voice_client:
            vc:wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
        elif not ctx.author.voice_client:
            return await ctx.send("join vc first\n||smh||")
        else:
            vc:wavelink.Player = ctx.voice_client
        
        await vc.play(search)


def setup(bot):
    bot.add_cog(Music(bot))