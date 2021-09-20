import discord
from discord.ext import commands
from discord.ext.commands.core import command
from core.classes import Cog_Extension
import json, asyncio, datetime

class Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.counter = 0
        self.oc=True

        async def time_task():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(883986916796682290)

            while not self.bot.is_closed():
                if(self.oc == True):
                    with open('setting.json','r',encoding='utf-8') as jfile:
                        jdata = json.load(jfile)
                    now_time = datetime.datetime.now().strftime('%H%M')
                    if now_time == jdata['task_time'] and self.counter == 0:
                        await self.channel.send(jdata['task_msg'])                                                
                        self.counter = 1
                    else:
                        pass
           
                await asyncio.sleep(1)
            
        self.bg_task = self.bot.loop.create_task(time_task())
        
    @commands.command()
    async def task_on(self,ctx):
        self.oc = True

    @commands.command()
    async def task_stop(self, ctx):
        self.oc = False    

    @commands.command()
    async def set_channel(self, ctx, ch:int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'Set Channel:{self.channel.mention}')
    
    @commands.command()
    async def set_msg(self, ctx, msg):
        self.counter = 0
        with open('setting.json','r',encoding='utf-8') as jfile:
            jdata = json.load(jfile)
        jdata['task_msg'] = msg
        with open('setting.json','w',encoding='utf-8') as jfile:
            json.dump(jdata,jfile,indent=4)

    @commands.command()
    async def set_time(self, ctx, time):
        self.counter = 0
        with open('setting.json','r',encoding='utf-8') as jfile:
            jdata = json.load(jfile)
        jdata['task_time'] = time
        with open('setting.json','w',encoding='utf-8') as jfile:
            json.dump(jdata,jfile,indent=4)

    
def setup(bot):
    bot.add_cog(Task(bot))