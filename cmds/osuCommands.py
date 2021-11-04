import discord
from discord.ext import commands
from core.classes import Cog_Extension
from api.osuApi import Osu
import json
import datetime

with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class osuCommands(Cog_Extension, Osu):
    @commands.command()
    async def Osu_BP1(self, ctx):
        beatmapset_data = Osu.get_best_beatmapset()
        embed=discord.Embed()
        embed.set_author(name=beatmapset_data['title_unicode'], icon_url=beatmapset_data['covers']['list'])
        embed.add_field(name="artist", value=beatmapset_data['artist'], inline=False)
        embed.add_field(name="source", value=beatmapset_data['source'], inline=False)
        embed.add_field(name="creator", value=beatmapset_data['creator'], inline=True)
        embed.add_field(name="status", value=beatmapset_data['status'], inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(osuCommands(bot))
        