from discord.ext import commands
import discord
import Prefix
import json
import aiohttp
import urllib.request
import random


class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['av', 'pfp'])
    async def avatar(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        show_avatar = discord.Embed(
            title=f'{member}',
            colour=discord.Colour.blue()

        )
        show_avatar.set_image(url='{}'.format(member.avatar_url))
        await ctx.send(embed=show_avatar)

    @commands.command(name="poll", description="Make a poll", aliases=['vote'])
    async def poll(self, ctx, *, args=None):
        prefix = Prefix.getprefix(ctx.guild)
        embed = discord.Embed(description=f'{args}', color=discord.Colour.blue())
        embed.set_author(name=f"Poll from {ctx.author}", icon_url=ctx.author.avatar_url)
        reactthis = await ctx.send(embed=embed)
        await reactthis.add_reaction("\U0001F44D")
        await reactthis.add_reaction("\U0001F44E")
        await ctx.message.delete()

    @commands.command(name="prefix", description="Set, fetch and reset prefixes")
    async def prefix(self, ctx, what=None, set=None):
        try:
            with open('prefixes.json') as f:
                prefixes = json.load(f)
                srvr = prefixes[str(server.id)]
        except:
            theprefix = "-"
            srvr = theprefix
            embed = discord.Embed(title=f"{Prefix.getprefix(ctx.guild)}prefix", color=discord.Colour.blue())
            embed.add_field(name="Command help:", value='Please use one of these commands', inline=False)
            embed.add_field(name="Usage:",
                            value=f"{Prefix.getprefix(ctx.guild)}prefix set [prefix]\n{Prefix.getprefix(ctx.guild)}prefix fetch\n{Prefix.getprefix(ctx.guild)}prefix reset",
                            inline=False)
        if what == None:
            await ctx.send(embed=embed)
        elif what == 'set':
            if ctx.message.author.guild_permissions.manage_guild:
                with open('prefixes.json') as f:
                    prefixes = json.load(f)
                prefixes[str(ctx.guild.id)] = set
                with open('prefixes.json', 'w') as f:
                    json.dump(prefixes, f, indent=4)
                await ctx.send("> The prefix for **" + ctx.guild.name + "** has been set to **" + set + "**")
            else:
                await ctx.send("Go get some perms and try again.")
        elif what == 'fetch':
            await ctx.send('The prefix for **{}** is **{}**'.format(ctx.guild.name, Prefix.getprefix(ctx.guild)))
        elif what == 'reset':
            if ctx.message.author.guild_permissions.manage_guild:
                with open('prefixes.json') as f:
                    prefixes = json.load(f)
                prefixes[str(ctx.guild.id)] = "-"
                with open('prefixes.json', 'w') as f:
                    json.dump(prefixes, f, indent=4)
                await ctx.send('The prefix for **{}** has been reset to **-**'.format(ctx.guild.name))
            else:
                await ctx.send("Go get some perms and try again.")
        else:
            await ctx.send(embed=embed)

    @commands.command()
    async def coronacount(self, ctx):
        await ctx.send('https://www.worldometers.info/coronavirus/')

    @commands.command()
    async def issue(self, ctx):
        embed = discord.Embed(
            title='If you have any issues, run this command',
            description=f'{Prefix.getprefix(ctx.guild)}report <issue>'
        )
        embed.add_field(name='Or Join and Report in', value='[This server](https://discord.gg/4dYzmYS)')
        await ctx.send(embed=embed)

    @commands.command(aliases=['author'])
    async def creator(self, ctx):
        embed = discord.Embed(
            title='Creator',
            description='Suteki#3477',
            colour=discord.Colour.blue()

        )

        embed.set_image(
            url="https://images-ext-1.discordapp.net/external/FR-mA0PVavjPibdTQNwr-UECIu93_Bcxxy8pj4zMU1Y/https/images-ext-2.discordapp.net/external/ZIeUgIKSBKeH9HLuziNvR4KG-NB8e_pI1ev7ccUMgQI/https/media.discordapp.net/attachments/696121556119715890/703691658797252657/image0.png?width=971&height=546")
        embed.add_field(name='Youtube', value="[Click Here!](https://www.youtube.com/channel/UCUlVOye5aOCp7eqhkQAXZhg)")
        embed.add_field(name='Created on', value='Python 3.8. Script written on Visual Studio Code')
        embed.add_field(name='Suteki Reddit', value='[Click here!](https://www.reddit.com/user/Watashi-sugoi)')
        embed.add_field(name='Support Server', value='[Click Here!](https://discord.gg/MddDvR7)')
        embed.add_field(name='Name meaning', value='Suteki means "Fantastic" in Japanese')
        embed.add_field(name='Someone who helped me a ton making this bot',
                        value='Coolo2 #5499 (try command `-coolo2`)')
        await ctx.send(embed=embed)

    @commands.command(aliases=['userinfo'])
    async def whois(self, ctx, member: discord.Member = None):
        if member == None:
            embed = discord.Embed(
                colour=discord.Colour.blue()
            )
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.set_footer(text=f'Requested by {ctx.author}')

            embed.add_field(name='**ID**', value=ctx.author.id, inline=False)
            embed.add_field(name='**Name**', value=f"{ctx.author}", inline=False)
            embed.add_field(name='**Guild Nickname**', value=ctx.author.display_name, inline=False)

            embed.add_field(name='**Created at**',
                            value=ctx.author.created_at.strftime('%a, %#d, %B, %Y, %I :%M %p UTC'), inline=False)
            embed.add_field(name='**Top Role**', value=ctx.author.top_role.mention, inline=False)
            embed.add_field(name='**Joined at**', value=ctx.author.joined_at.strftime("%a, %d %B %Y, %I : %M %p UTC"),
                            inline=False)
            embed.add_field(name='**Bot?**', value=ctx.author.bot, inline=False)
            embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(
                colour=discord.Colour.blue()
            )
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(text=f'Requested by {ctx.author}')

            embed.add_field(name='**ID**', value=member.id, inline=False)
            embed.add_field(name='**Name**', value=f"{member}", inline=False)
            embed.add_field(name='**Guild Nickname**', value=member.display_name, inline=False)

            embed.add_field(name='**Created at**', value=member.created_at.strftime('%a, %#d, %B, %Y, %I :%M %p UTC'),
                            inline=False)
            embed.add_field(name='**Top Role**', value=member.top_role.mention, inline=False)
            embed.add_field(name='**Joined at**', value=member.joined_at.strftime("%a, %d %B %Y, %I : %M %p UTC"),
                            inline=False)
            embed.add_field(name='**Bot?**', value=member.bot, inline=False)
            embed.set_author(name=f"{member.name}", icon_url=member.avatar_url)
            await ctx.send(embed=embed)

    @commands.command()
    async def announce(self, ctx, *, announcement=None):
        if announcement == None:
            await ctx.send(
                f'What would you like to announce?\n\nCorrect Usage:\n`{Prefix.getprefix(ctx.guild)}announce <announcement>')
        else:
            embed = discord.Embed(
                title=f'{ctx.author.name} has made an announcement!',
                description=f'{announcement}',
                colour=discord.Colour.blue()
            )
            embed.set_footer(text=f'Announced by {ctx.author}')
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/696121556119715890/709806706057674872/announcements-icon.png?width=502&height=502')
            await ctx.send(embed=embed)
            await ctx.message.delete()

    @commands.command()
    async def clap(self, ctx, word, word1, word2=None, word3=None, word4=None):
        if word3 == None:
            await ctx.send(f'{word} 👏 {word1} 👏 {word2} 👏 {word}')
        else:
            await ctx.send(f'{word} 👏 {word1} 👏 {word2} 👏 {word3}')

    @commands.command(aliases=['dictionary', 'urban'])
    async def define(self, ctx, word=None):
        if word == None:
            await ctx.send(
                f'**What do you want from the Urban Dictionary?**\n\nCorrect Usage: `{Prefix.getprefix(ctx.guild)}define <word>`')
        else:
            url = 'http://api.urbandictionary.com/v0/define?term=%s' % (word)

            response = urllib.request.urlopen(url)
            data = json.loads(response.read())
            definition = data['list'][0]['definition']
            e = discord.Embed(title=word, description=str(definition), colour=discord.Colour.blue())

            e.set_footer(text='Note: This is the urban dictionary so the definitions may not be very accurate..')
            e.set_thumbnail(
                url='https://images-ext-2.discordapp.net/external/HMmIAukJm0YaGc2BKYGx5MuDJw8LUbwqZM9BW9oey5I/https/i.imgur.com/VFXr0ID.jpg')
            await ctx.send(embed=e)

    @commands.command(aliases=['birth', 'bday'])
    async def birthday(self, ctx, member: discord.Member = None):
        if member == None:
            embed = discord.Embed(
                title=f'Birthday of {ctx.author.name}',
                description=ctx.author.created_at.strftime('%a, %#d, %B, %Y, %I :%M %p UTC'),
                colour=discord.Colour.blue()
            )
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.set_author(name="Birthday", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Birthday of {member.name}',
                description=member.created_at.strftime('%a, %#d, %B, %Y, %I :%M %p UTC'),
                colour=discord.Colour.blue()
            )
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_author(name="Birthday", icon_url=member.avatar_url)
            await ctx.send(embed=embed)

    @commands.command(aliases=['pick'])
    async def choose(self, ctx, word=None, word2=None):
        responses = [f"{word}", f"{word2}"]
        if word == None:
            await ctx.send(
                f"**What would you like Bop to choose for you?**\n\nCorrect Usage: `{Prefix.getprefix(ctx.guild)}choose <option> <option 2>`")
        else:
            if word2 == None:
                await ctx.send(
                    f"**What would you like Bop to choose for you?**\n\nCorrect Usage: `{Prefix.getprefix(ctx.guild)}choose <option> <option 2>`")
            else:
                embed = discord.Embed(
                    title=f"{word} or {word2}",
                    description=f"Bop chose `{random.choice(responses)}`",
                    colour=discord.Colour.blue()
                )
            await ctx.send(embed=embed)

    @commands.command()
    async def server(self, ctx):
        embed = discord.Embed(
            title="Join Bop's support server!",
            description="In this server you can report an issue, view Bop's changelog, etc.",
            colour=discord.Colour.blue()
        )
        embed.add_field(name="**Link**", value="https://discord.gg/4dYzmYS")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(misc(bot))