from discord.ext import commands
import discord
import Prefix
import json
from datetime import datetime, timedelta
import time

class logs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.Cog.listener()
    async def on_message_delete(self, message):
        with open(r'Setup.json') as f:
            prefixes = json.load(f)
        try:
            logchannel = prefixes[str(message.guild.id)]['logchannel']
        except:
            logchannel = "none"
        try:
            for channel in message.guild.channels:
                if channel.id == int(logchannel):
                    if message.author != self.bot.user:
                        embed = discord.Embed(title="Message Deleted", color=0x71368a)
                        embed.add_field(name="**Message:=**", value= message.content, inline=False)
                        embed.add_field(name="**Sent by**", value= "<@" + str(message.author.id) + ">", inline=False)
                        embed.add_field(name="**Channel**", value= "<#" + str(message.channel.id) + ">", inline=False)
                        embed.set_footer(text=Commands.footer(str(self.bot.user) + " logs"))
                        embed.set_author(name="User: " + str(message.author), icon_url=message.author.avatar_url)
                        t=datetime.datetime.now
                        embed.set_footer(text=t)
                        await channel.send(embed=embed)
        except:
            pass



def setup(bot):
    bot.add_cog(logs(bot))