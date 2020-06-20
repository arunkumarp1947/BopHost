from discord.ext import commands
import discord
import Prefix


class utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['purge'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f'I have cleared **{amount}** messages', delete_after=2)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def warn(self, ctx, member: discord.Member = None, *, reason=None):
        if member == None:
            await ctx.send('Who do you want to warn?')
        else:
            embed = discord.Embed(
                title=f'{member.name} has been warned!',
                description=f'Reason: {reason}',
                colour=discord.Colour.red()

            )
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/696121556119715890/707310613671706705/warning.png?width=784&height=519')
            await ctx.send(embed=embed)
            await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member = None, *, reason=None):
        if member == None:
            await ctx.send("Who do you want to kick?")
        else:
            await member.kick(reason=reason)
            embed = discord.Embed(
                title=f'{member.name} has been kicked',
                description=f'Reason: {reason}',
                colour=discord.Colour.red()

            )
            await ctx.send(embed=embed)
            await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, *, reason=None):
        if member == None:
            await ctx.send("Who do you want to ban?")
        else:
            await member.ban(reason=reason)
            embed = discord.Embed(
                title=f'{member.name} has been banned',
                description=f'Reason: {reason}',
                colour=discord.Colour.red()

            )
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/625842127284469760/704711229675012136/6623_banhammer.png')
            await ctx.send(embed=embed)
            await ctx.message.delete()

    @commands.command()
    async def unmute(self, ctx, member: discord.Member):
        guild = ctx.guild

        for role in guild.roles:
            if role.name == "Muted":
                await member.remove_roles(role)
                await ctx.send(f"**{member}** has been unmuted")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member : discord.Member, *, reason=None):
        try:
            role = discord.utils.get(ctx.guild.roles, name="Muted")
            await member.add_roles(role)
            embed=discord.Embed(
                title=f"{member.name} has been muted!",
                description=f"Reason: {reason}",
                colour=discord.Colour.red()
            )
            await ctx.send(embed=embed)
        except:
            embed=discord.Embed(
                title='Error!',
                description="Please make a role named `Muted` and remove its permissions to speak.",
                colour=discord.Colour.red()
            )
            embed.set_thumbnail(url="http://www.pngall.com/wp-content/uploads/2016/04/Red-Cross-Mark-PNG-Pic.png")
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(utility(bot))

