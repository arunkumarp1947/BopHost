from discord.ext import commands
import discord
import Prefix
import json
import random
import aiohttp


class image(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def popcorn(self, ctx):
        embed = discord.Embed(
            title=f'Some popcorn for {ctx.author.name}',
            colour=discord.Colour.blue()
        )
        embed.set_image(
            url='https://media.discordapp.net/attachments/625842127284469760/704728263980875816/Movie-Popcorn_0.png?width=450&height=630')
        await ctx.send(embed=embed)

    @commands.command()
    async def cheese(self, ctx):
        embed = discord.Embed(
            title=f'Some cheese for {ctx.author.name}',
            colour=discord.Colour.blue()
        )
        embed.set_image(
            url='https://media.discordapp.net/attachments/625842127284469760/704727288134107366/thinkstockphotos470340853.png?width=883&height=630')
        await ctx.send(embed=embed)

    @commands.command()
    async def sketchers(self, ctx):
        embed = discord.Embed(
            title='Here are your awesome light up sketchers',
            colour=discord.Colour.blue()
        )
        embed.set_image(
            url='https://media.discordapp.net/attachments/625842127284469760/697451876714807346/GUEST_70109a81-d6ee-47f7-a2f0-2d31f274c4ee.png')
        await ctx.send(embed=embed)

    @commands.command()
    async def brownies(self, ctx):
        embed = discord.Embed(
            title=f'Some brownies for {ctx.author.name}',
            colour=discord.Colour.blue()
        )
        embed.set_image(
            url='https://media.discordapp.net/attachments/625842127284469760/697105610248028260/image0.jpg?width=914&height=609')
        await ctx.send(embed=embed)

    @commands.command()
    async def sandwich(self, ctx):
        embed = discord.Embed(
            title=f'A sandwich for {ctx.author.name}',
            colour=discord.Colour.blue()
        )

        embed.set_image(
            url='https://media.discordapp.net/attachments/625842127284469760/696780006017204414/image0.jpg?width=707&height=530')
        await ctx.send(embed=embed)

    @commands.command()
    async def burger(self, ctx):
        embed = discord.Embed(
            title=f'A burger for {ctx.author.name}',
            colour=discord.Colour.blue()
        )
        embed.set_image(
            url='https://media.discordapp.net/attachments/625842127284469760/696780920908283995/image0.jpg?width=406&height=609')
        await ctx.send(embed=embed)

    @commands.command()
    async def corona(self, ctx):
        embed = discord.Embed(
            title=f'Hah you thought. Some beer for {ctx.author.name}',
            colour=discord.Colour.blue()
        )
        embed.set_image(
            url=' https://media.discordapp.net/attachments/625842127284469760/696781476037132318/image0.jpg?width=913&height=609')
        await ctx.send(embed=embed)

    @commands.command()
    async def salad(self, ctx):
        embed = discord.Embed(
            title=f'Some salad for {ctx.author.name}',
            colour=discord.Colour.blue()
        )
        embed.set_image(
            url='https://media.discordapp.net/attachments/625842127284469760/696783918208385114/image0.jpg?width=471&height=609')
        await ctx.send(embed=embed)

    @commands.command()
    async def holdup(self, ctx):
        embed = discord.Embed(
            title='Hol Up',
            colour=discord.Colour.blue()

        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/625842127284469760/696115251468566699/d74.png')
        await ctx.send(embed=embed)

    @commands.command()
    async def tweet(self, ctx, username: str = None, *, text: str):
        if username == None:
            await ctx.send('**What would you like to tweet?**\n\nCorrect Usage: `-tweet <username> <text>`')
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={text}") as r:
                res = await r.json()
                embed = discord.Embed(
                    color=discord.Colour.blue(),
                    title=f"Tweet from {username}"
                )
                embed.set_image(url=res["message"])

                await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(image(bot))