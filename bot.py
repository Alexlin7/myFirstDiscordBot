from inspect import Parameter
import discord
from discord import file
from discord.ext import commands
from discord.flags import Intents
import json
import random
import os

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


@bot.event
async def on_member_remove(member):
    print(f'{member} leave!')

@bot.command()
async def load(ctx,extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done .')

@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Unloaded {extension} done .')

@bot.command()
async def reload(ctx,extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Reladed {extension} done .')


for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])

