from inspect import Parameter
import discord
from discord import file
from discord.ext import commands
from discord.flags import Intents
from core.classes import Cog_Extension


class Main(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} ms')



def setup(bot):
    bot.add_cog(Main(bot))