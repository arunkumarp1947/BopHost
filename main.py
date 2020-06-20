import discord
import json
import random
import os
from discord.ext import commands
import Prefix
import aiohttp
import time


def get_prefix(client, message):
    try:
        with open('prefixes.json') as f:
            prefixes = json.load(f)

        return commands.when_mentioned_or(prefixes[str(message.guild.id)])(client, message)
    except:
        return commands.when_mentioned_or("-")(client, message)


client = commands.Bot(command_prefix=get_prefix, case_insensitive=True)

client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,
                                                           name="{} servers | -help".format(len(client.guilds))))
    print(' ☑️  Bop has awoken.. ☑️')


@client.command(name='ping', description='Returns the bots latency (ms)')
async def ping(ctx):
    t1 = time.perf_counter()
    message = await ctx.send("checking ping...")
    t2 = time.perf_counter()
    ping = round((t2 - t1) * 1000)
    pingme = str(ping)
    em = discord.Embed(
        title='Bot latency:',
        description='`' + pingme + '`' + 'ms',
        colour=discord.Colour.blue()

    )
    em.add_field(name='Discord Latency:', value=f'`{round(client.latency * 1000)}`ms')
    await ctx.send(embed=em)
    await message.delete()


@client.command(aliases=['commands'])
async def help(ctx):
    pre = Prefix.getprefix(ctx.guild)
    embed = discord.Embed(
        title='A list of commands in categories',
        colour=discord.Colour.blue()
    )
    embed.add_field(name="**Server Prefix**", value=f"`{Prefix.getprefix(ctx.guild)}`")
    embed.add_field(name="**Fun**",
                    value=f"```{pre}fact, {pre}quote, {pre}8ball, {pre}coinflip, {pre}roll, {pre}kill, {pre}lenny, {pre}number, {pre}bug, {pre}email, {pre}tweet, {pre}declare, {pre}sort, {pre}say, {pre}bet, {pre}reddit, {pre}meme, {pre}idiotsandwich```",
                    inline=False)
    embed.add_field(name="**Moderation**",
                    value=f"```{pre}mute, {pre}unmute, {pre}kick, {pre}ban, {pre}clear, {pre}joinmessage```", )
    embed.add_field(name="**Images**",
                    value=f"```{pre}salad, {pre}brownies, {pre}sandwich, {pre}burger, {pre}corona, {pre}food, {pre}cheese, {pre}popcorn, {pre}cat, {pre}dog, {pre}avatar, {pre}skechers```",
                    inline=False)
    embed.add_field(name="**Miscellanous**",
                    value=f"```{pre}ping, {pre}issue, {pre}suggest, {pre}creator, {pre}coronacount, {pre}urban, {pre}userinfo, {pre}botinfo , {pre}choose, {pre}server, {pre}support```",
                    inline=True)
    embed.set_author(name="Help", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


@client.command()
async def fakespawn(ctx):
    embed = discord.Embed(
        title='‌‌A wild pokémon has аppeаred!',
        description='Guess the pokémon аnd type p!cаtch <pokémon> to cаtch it!',
        colour=0x00b36f

    )
    responses = random.choice(
        ['https://media.discordapp.net/attachments/693584026140672020/694218579700088862/PokecordSpawn.jpg',
         'https://media.discordapp.net/attachments/696121556119715890/710175100959195156/1200px-383Groudon.png?width=502&height=502',
         'https://media.discordapp.net/attachments/696121556119715890/710175364634247168/151Mew.png?width=502&height=502',
         'https://media.discordapp.net/attachments/696121556119715890/710175423283069081/150Mewtwo.png?width=502&height=502'])
    embed.set_image(url=responses)
    await ctx.send(embed=embed)
    await ctx.message.delete()


@client.command()
async def british(ctx):
    embed = discord.Embed(
        title='British picture for you',
        colour=discord.Colour.blue()
    )
    responses = random.choice([
                                  'https://media.discordapp.net/attachments/625842127284469760/708018725508349972/queen-elizabeth-ii.png?width=777&height=519',
                                  'https://media.discordapp.net/attachments/625842127284469760/708019220121649694/WIPO.png?width=692&height=519',
                                  'https://media.discordapp.net/attachments/625842127284469760/708019360265928793/english-crumpets-1500-58a4acc13df78c4758cd2323.png?width=779&height=519',
                                  'https://media.discordapp.net/attachments/625842127284469760/708019575094116472/OIP.png',
                                  'https://media.discordapp.net/attachments/704779434674225283/708379024262430750/maxresdefault.png?width=879&height=495',
                                  'https://media.discordapp.net/attachments/625842127284469760/708377809621483550/image1.jpg?width=879&height=495',
                                  'https://media.discordapp.net/attachments/625842127284469760/708378115813933066/image0.png',
                                  'https://media.discordapp.net/attachments/625842127284469760/708380885317189632/image0.jpg',
                                  'https://media.discordapp.net/attachments/625842127284469760/708380885598339132/image1.jpg?width=755&height=503',
                                  'https://media.discordapp.net/attachments/625842127284469760/708380886143336548/image2.jpg?width=670&height=503',
                                  'https://media.discordapp.net/attachments/625842127284469760/708380886718087208/image3.jpg?width=252&height=503'])
    embed.set_image(url=responses)
    await ctx.send(embed=embed)


@client.event
async def on_command_error(ctx, error):
    if str(error) == "Command raised an exception: Forbidden: 403 Forbidden (error code: 50013): Missing Permissions":
        message = "I dont have permission to do that! Please give me administrator permissions to use the **{}** command".format(
            ctx.command)
    elif "Command raised an exception: KeyError:" in str(error):
        message = "Invalid warn ID!"
    else:
        message = "**" + str(error) + "**"
    if "not found" not in str(error):
        em = discord.Embed(title="Error", description=str(message), colour=discord.Colour.blue())
        await ctx.send(embed=em)


@client.command(aliases=['url', 'link', ])
async def invite(ctx):
    embed = discord.Embed(
        title='Click below to invite the bot to any server!',
        colour=discord.Colour.blue()
    )
    embed.add_field(name='Link',
                    value='[Invite](https://discordapp.com/api/oauth2/authorize?client_id=694229303964991529&permissions=0&scope=bot)')
    await ctx.send(embed=embed)


@client.command()
async def coolo2(ctx):
    embed = discord.Embed(
        title='Coolo2',
        description='A person that helped me a ton making this bot',
        colour=discord.Colour.blue()
    )
    embed.add_field(name='Youtube', value='[Click here](https://www.youtube.com/channel/UClqTOwlCslNUDzwnO0r0-Ow)')
    embed.add_field(name='Twitter', value='[Click here](https://twitter.com/ItsCoolo2)')
    embed.add_field(name='Reddit', value='[Click here](https://www.reddit.com/user/Coolo2)')
    embed.add_field(name='Twitch', value='[Click here](https://www.twitch.tv/itscoolo2)')
    embed.set_image(
        url='https://cdn.discordapp.com/avatars/368071242189897728/55b476cc8b6403087923f4da1d7b5541.webp?size=1024')
    await ctx.send(embed=embed)


@client.command(aliases=['about'])
async def botinfo(ctx):
    embed = discord.Embed(
        title='Information about Bop',
        description='A fun bot with moderation commands and many fun commands!',
        colour=discord.Colour.blue()
    )
    embed.add_field(name='ID', value='694229303964991529')
    embed.add_field(name='Creator', value='Suteki#3477')
    embed.set_thumbnail(
        url='https://images-ext-1.discordapp.net/external/VSgY9tM_E0q2ihF7jLLhSafPyweBiESWlRRIGYw5LSM/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/694229303964991529/176125221fdfd75cc1a13f7a81691697.webp?width=502&height=502')
    embed.add_field(name='Server count', value=len(client.guilds))
    embed.add_field(name='Created with', value='Python 3.8, Visual Studio Code')
    embed.add_field(name='Created at', value='March 30, 2020')
    await ctx.send(embed=embed)


@client.command()
async def servercount(ctx):
    await ctx.send('I am currently in **{}** servers'.format(len(client.guilds)))


@client.event
async def on_member_join(member):
    try:
        channel = discord.utils.get(member.guild.channels, name='bjoins')
        await channel.send(f'{member.mention} has joined **{member.guild.name}**.')
    except:
        pass


@client.command()
async def joinmessage(ctx):
    await ctx.send(
        'If you would like join and leave messages from Bop, please create a channel named #bjoins and #bleaves. Currently, they cannot be custom messages.')


@client.event
async def on_member_remove(member):
    try:
        channel = discord.utils.get(member.guild.channels, name='bleaves')
        await channel.send(f'**{member.name}** has left **{member.guild.name}**.')
    except:
        pass


@client.command()
@commands.cooldown(1, 20, commands.BucketType.user)
async def suggest(ctx, *, suggestion):
    await client.get_user(449662597927665666).send(f'{ctx.author} has suggested something: `{suggestion}`')
    embed = discord.Embed(
        title=f'You have suggested {suggestion}',
        description='The owner will review your suggestion',
        colour=discord.Colour.blue()
    )
    await ctx.send(embed=embed)


@client.command()
@commands.cooldown(1, 20, commands.BucketType.user)
async def report(ctx, *, issue=None):
    if issue == None:
        await ctx.send(f'**What issue have you found?**\n\nCorrect Usage: `{Prefix.getprefix(ctx.guild)}report <issue>')
    else:
        await client.get_user(449662597927665666).send(f'{ctx.author} has found an **issue**: `{issue}`')
        embed = discord.Embed(
            title=f'You have reported {issue}',
            description='The owner will review it soon..',
            colour=discord.Colour.blue()
        )
        await ctx.send(embed=embed)


@client.command(name="setup", description="Setup the bot for a server")
@commands.has_permissions(manage_guild=True)
async def setup(ctx, choice=None, channel=None, *, message=None):
    prefix = Prefix.getprefix(ctx.guild)
    if choice == None:
        embed = discord.Embed(title="Help for {}setup".format(prefix), color=0xFF8700)
        embed.add_field(name="What it does", value="{}setup - Setup the bot for a server".format(prefix), inline=False)
        embed.add_field(name="Arguments", value=f"""
        {prefix}setup logging [#channel]
        """, inline=False)
        await ctx.send(embed=embed)
    if choice == "logging":
        if channel != None:
            channel = channel.replace("<", "").replace(">", "").replace("#", "").replace("!", "")
            with open(r'Setup.json') as f:
                prefixes = json.load(f)
            data = {
                'logchannel': str(channel),
            }
            prefixes[str(ctx.message.guild.id)] = data
            with open(r'Setup.json', 'w') as f:
                json.dump(prefixes, f, indent=4)
            with open(r'Setup.json') as f:
                prefixes = json.load(f)
            await ctx.send("> Set logging channel to <#{}>".format(str(channel)))
        else:
            embed = discord.Embed(title="Help for {}setup logging".format(prefix), color=0xFF8700)
            embed.add_field(name="What it does", value="{}setup logging - Setup channel for logging".format(prefix),
                            inline=False)
            embed.add_field(name="Arguments", value=f"{prefix}setup logging [#channel]", inline=False)
            await ctx.send(embed=embed)


@client.event
async def on_guild_join(guild):
    lol = client.get_channel(714539664509501452)
    em = discord.Embed(color=discord.Color.blue())
    em.title = "Someone added Bop to a server!"
    em.description = "Server Name: `" + guild.name + "`"
    em.set_thumbnail(url=guild.icon_url)
    em.add_field(name="ID: ", value=str(guild.id))
    em.add_field(name="Servers: ", value="I am now in **{}** servers".format(str(len(client.guilds))))
    await lol.send(embed=em)
    payload = {"server_count": len(client.guilds)}
    async with aiohttp.ClientSession() as aioclient:
        await aioclient.post(url, data=payload, headers=headers)
        global counter
        counter = 0
        servers = list(client.guilds)
        for x in range(len(servers)):
            server = servers[x - 1]
            counter = counter + len(server.members)
        coolo = len(client.guilds)
        payload = {"server_count": len(client.guilds)}
        async with aiohttp.ClientSession() as aioclient:
            await aioclient.post(url, data=payload, headers=headers)


@client.event
async def on_guild_remove(guild):
    lol = client.get_channel(714539664509501452)
    em = discord.Embed(color=discord.Color.blue())
    em.title = "Someone kicked Bop from a server.."
    em.description = "Server: " + guild.name
    em.add_field(name="Servercount ", value="I am in **{}** servers".format(str(len(client.guilds))))
    em.set_thumbnail(url=guild.icon_url)
    await lol.send(embed=em)
    payload = {"server_count": len(client.guilds)}
    async with aiohttp.ClientSession() as aioclient:
        await aioclient.post(url, data=payload, headers=headers)
        global counter
        counter = 0
        servers = list(client.guilds)
        for x in range(len(servers)):
            server = servers[x - 1]
            counter = counter + len(server.members)
            coolo = len(bot.guilds)
            payload = {"server_count": len(client.guilds)}
            async with aiohttp.ClientSession() as aioclient:
                await aioclient.post(url, data=payload, headers=headers)


@client.command()
async def support(ctx):
    embed = discord.Embed(
        title="Support",
        description="[Invite link](https://top.gg/bot/694229303964991529?__cf_chl_jschl_tk__=9906c33bec1bca7a446a8553bf16b62c93748615-1592494029-0-AeiAZIvRIFKE3Uw-DZOJrXK6EB3m_6_H96kUPbpCKeIhc8h5Rb5h1CPCWtgUBPSgKRXp2bi6x4AdMm7v48PfdjI6j4btOQf66pT8XqbII0gyDcBJOWqvXFzy2HovMkDVqCR1XKxrdNo1vAKkyGFOKwtV_EX_IjZZwjybLtFvUa48pli6fc2_2jZqaULdY6cbimhUdazTOfBSO3dh0mPBaE27_0VFlcRpn0jA-ykyvGM-CdeWJb5qREfQsSeSKYCzyrleUsYJccRC6j2jpa9jRWCDDGRNLgzaswO0bTwMhIWu0ua72kng-BWaljw5fbOXnQ)"
    )
    embed.add_field(name="**To view bot commands**", value=f"`{Prefix.getprefix(ctx.guild)}help`", inline=False)
    embed.add_field(name="**To report a bug**", value=f"`{Prefix.getprefix(ctx.guild)}report <issue>`", inline=False)
    embed.add_field(name="**Contact the owner**",
                    value="My Discord username is `Suteki#3477`. You can also join my [Support Server](https://discord.gg/bSfqurB)")
    await ctx.send(embed=embed)


extensions = ['fun', 'misc', 'image', 'utility', 'logs']

if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
            print('Loaded {}'.format(extension))
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))


client.run("Njk0MjI5MzAzOTY0OTkxNTI5.Xuz5_g.rZnxmIMQB32Eu7B09OvOxApM4Vc")
