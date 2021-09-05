import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):
    @commands.command()
    async def 圖片(self, ctx):
        random_photo = random.choice(jdata['photo'])
        photo = discord.File(random_photo)
        await ctx.send(file = photo)

    @commands.command()
    async def 網路圖片(self, ctx):
        random_url_photo = random.choice(jdata['url_photo'])
        await ctx.send(random_url_photo)

def setup(bot):
    bot.add_cog(React(bot))