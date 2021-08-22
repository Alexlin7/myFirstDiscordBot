from inspect import Parameter
import discord
from discord import file
from discord.ext import commands
from discord.flags import Intents
import json
import random


with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='[', intents = intents)


@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    print(f'{member} join!')

@bot.command()
async def 圖片(ctx):
    random_photo = random.choice(jdata['photo'])
    photo = discord.File(random_photo)
    await ctx.send(file = photo)

@bot.command()
async def 網路圖片(ctx):
    random_url_photo = random.choice(jdata['url_photo'])
    await ctx.send(random_url_photo)

@bot.event
async def on_member_remove(member):
    print(f'{member} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} ms')

bot.run(jdata['TOKEN'])

