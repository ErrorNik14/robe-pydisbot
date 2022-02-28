from sqlite3 import connect
import nextcord
from nextcord.ext import commands
import sqlite3

class EcoFuncs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def saddle(self, id, type, amount=None):
        connection = sqlite3.connect("Databases/Economy.db")
        crsr = connection.cursor()
        if type == "return":
            crsr.execute(f"SELECT saddle FROM userinfo WHERE id={id}")
            return crsr.fetchone()[0]
        elif type == "reduce":
            crsr.execute(f"SELECT * FROM userinfo WHERE id={id}")
            record = crsr.fetchone()
            crsr.execute(f"""UPDATE userinfo
            SET
                id={id},
                bank={record[1]},
                saddle={record[2] + amount},
                balmax={record[3]}
                exp={record[4]},
                expmax={record[5]},
                lv={record[6]}
            WHERE id={id}
            """)
        elif type == "increase":
            crsr.execute(f"SELECT * FROM userinfo WHERE id={id}")
            record = crsr.fetchone()
            crsr.execute(f"""UPDATE userinfo
            SET
                id={id},
                bank={record[1]},
                saddle={record[2] - amount},
                balmax={record[3]}
                exp={record[4]},
                expmax={record[5]},
                lv={record[6]}
            WHERE id={id}
            """)
        connection.close()





class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def lol(self, ctx):
        await ctx.reply("test")

    @lol.error
    async def lolcooldown(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.reply("cooldown test")
        else:
            raise error
    

def setup(bot):
    bot.add_cog(Economy(bot))