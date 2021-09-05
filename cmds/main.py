from inspect import Parameter
import discord
from discord import file
from discord.ext import commands
from discord.ext.commands.core import command
from discord.flags import Intents
from core.classes import Cog_Extension
import datetime


class Main(Cog_Extension):
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} ms')

    @commands.command()
    async def em(self, ctx):
        embed=discord.Embed(title="About", url="https://www.facebook.com/ali97008/", description="About the bot and me", color=0x095ce1, timestamp= datetime.datetime.utcnow())
        embed.set_author(name="Alexlin7", icon_url="https://i.imgur.com/8kWu1Wi.png")
        embed.set_thumbnail(url="https://i.imgur.com/8kWu1Wi.png")
        embed.add_field(name="ID", value="Alexlin7", inline=True)
        embed.add_field(name="dfsdf", value="1432", inline=True)
        embed.add_field(name="asfas", value="11561", inline=False)
        embed.add_field(name="asfas", value="11561", inline=False)
        embed.add_field(name="asfas", value="11561", inline=True)
        embed.set_footer(text="測試用訊息 ")
        await ctx.send(embed=embed)
        
    @commands.command()
    async def sayd(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def purge(self, ctx, num : int):
        await ctx.channel.purge(limit = num + 1)



def setup(bot):
    bot.add_cog(Main(bot))