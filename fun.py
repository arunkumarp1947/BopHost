from discord.ext import commands
import discord
import Prefix
import aiohttp
import random
import json


class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="meme", description="Get a random reddit meme")
    async def meme(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.reddit.com/r/dankmemes/random") as r:
                data = await r.json()
                title = data[0]["data"]["children"][0]["data"]["title"]
                author = data[0]["data"]["children"][0]["data"]["author"]
                upvotes = data[0]["data"]["children"][0]["data"]["ups"]
                r = lambda: random.randint(0, 255)
                colour = '#%02X%02X%02X' % (r(), r(), r())
                e = discord.Embed(title=f"{title}", colour=random.randint(0, 0xffffff))
                e.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
                e.set_footer(text=f"👍 {upvotes}")
                await ctx.send(embed=e)

    @commands.command(name="doggy", description="Get a random reddit puppy", aliases=['dog', 'puppy'])
    async def doggy(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.reddit.com/r/puppysmiles/random") as r:
                data = await r.json()
                e = discord.Embed(title="A picture of a random doggy", colour=0xFF8700)
                e.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
                e.set_footer(text=f'Requested by {ctx.author}')
                await ctx.send(embed=e)

    @commands.command(name="randomreddit", description="Get a random reddit kitty", aliases=['kitty', 'cat'])
    async def randomreddit(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.reddit.com/r/kitty/random") as r:
                data = await r.json()
                e = discord.Embed(title="A picture of a random kitty", colour=discord.Colour.blue())
                e.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
                e.set_footer(text=f'Requested by {ctx.author}')
                await ctx.send(embed=e)

    @commands.command()
    async def reddit(self, ctx, sub=None):
        async with aiohttp.ClientSession() as session:
            if sub == None:
                await ctx.send(f"**Which subreddit do you want to see?**\n\nCorrect Usage: `{Prefix.getprefix(ctx.guild)}reddit <subreddit>`")
            else:
                async with session.get(f"https://api.reddit.com/r/{sub}/random") as r:
                    data = await r.json()
                    title = data[0]["data"]["children"][0]["data"]["title"]
                    author = data[0]["data"]["children"][0]["data"]["author"]
                    upvotes = data[0]["data"]["children"][0]["data"]["ups"]
                    r = lambda: random.randint(0, 255)
                    colour = '#%02X%02X%02X' % (r(), r(), r())
                    e = discord.Embed(title=f"{title}", colour=random.randint(0, 0xffffff))
                    e.add_field(name="**Subreddit**", value=f"`{sub}`")
                    e.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
                    e.set_footer(text=f"👍 {upvotes}")
                    await ctx.send(embed=e)

    @commands.command(name="food", description="Get some food")
    async def food(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.reddit.com/r/food/random") as r:
                data = await r.json()
                e = discord.Embed(title="A picture of some food", colour=discord.Colour.blue())
                e.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
                e.set_footer(text=f'Requested by {ctx.author}')
                await ctx.send(embed=e)

    @commands.command()
    async def email(self, ctx, member: discord.Member, *, thing=None):
        if thing == None:
            await ctx.send(
                f'What do you want to email?\n\n Correct Usage:\n`{Prefix.getprefix(ctx.guild)}email (user) (message)`')
        else:
            await ctx.send('{}, you have mail from {}!'.format(member.mention, ctx.author.mention))
            embed = discord.Embed(
                title='Mail',
                description=f'{thing}',
                colour=discord.Colour.red()
            )
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/696121556119715890/704429198080606278/Envelope-PNG-Picture.png')
            embed.set_footer(text=f'to {member} from {ctx.author.name}')
            await ctx.send(embed=embed)
            await ctx.message.delete()

    @commands.command(name="cute", description="Get a random cute picture", aliases=['aww'])
    async def cute(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.reddit.com/r/aww/random") as r:
                data = await r.json()
            r = lambda: random.randint(0, 255)
            colour = '#%02X%02X%02X' % (r(), r(), r())
            e = discord.Embed(title="A cute picture from r/aww", colour=random.randint(0, 0xffffff))
            e.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
            e.set_footer(text=f'Requested by {ctx.author}')
            await ctx.send(embed=e)

    @commands.command()
    async def declare(self, ctx, *, text=None):
        if text == None:
            await ctx.send(
                f'What would you like to declare?\n\nCorrect Usage:\n`{Prefix.getprefix(ctx.guild)}declare <message>`')
        else:
            embed = discord.Embed(
                title='Declaration',
                description=f'{ctx.author.name} has declared that {text}!',
                colour=discord.Colour.blue()
            )
            await ctx.send(embed=embed)
            await ctx.message.delete()

    @commands.command()
    async def bug(self, ctx, member: discord.Member = None):
        if member == None:
            await ctx.send(
                f'Who would you like to bother?\n\nCorrect Useage:\n `{Prefix.getprefix(ctx.guild)}bug <user>')
        else:
            await ctx.send(f'{member.mention} 2 ping {member.mention}')
            await ctx.send(f"{member.mention} 4 ping {member.mention}")
            await ctx.send(f'{member.mention} 8 ping {member.mention}')
            await ctx.send('hehe')

    @commands.command()
    async def number(self, ctx):
        random.randit(1, 100)
        embed = discord.Embed(
            title=f'Random number between 0 and 100 for {ctx.author.name}',
            description=f'{random.choice(responses)}',
            colour=discord.Colour.blue()

        )
        await ctx.send(embed=embed)

    @commands.command()
    async def kill(self, ctx, *, thing=None):
        if thing == None:
            await ctx.send(f'Who do you want dead?\n\nCorrect Usage:\n{Prefix.getprefix(ctx.guild)}kill <person>')
        else:
            responses = [f'{thing} has been smelt', f'{thing} accidentally fell into his grave',
                         f'{thing} died from swallowing a dorito, it scratched his throat',
                         'you killed him/her and tried making it secret. Why would you do this command? Well, now it is known that you killed him/her',
                         f'{thing} was walking in the woods until a dying tree fell on him',
                         f'{thing}  tripped on a rock in suicide forest', f'{thing} was bit my a monkey',
                         f'{thing} was hit by a cannon',
                         f'{thing} accidentally shot himself in court to demonstrate how the victim might have killed a person',
                         f'{thing} went for a swim in some poison', f'{thing} was hit by a pitch',
                         f'{thing} fell down a chimney after mistaking it for a balcony',
                         f'{thing} got a B- on a test and his dad found it in the trash',
                         f'{thing} was told a couple horrible jokes',
                         f'{thing} was revving his engine to show off his Ferrari until it burned',
                         f'{thing} was electrocuted by a microphone', f'{thing} was struck by a flying landmower',
                         f'{thing} handcuffed himself to a tree', f'{thing} was the man in the dancing coffin meme',
                         f'{thing} was listening to music and their playlist landed on justin beiber',
                         f'{thing} tried eating a big mac in one bite and choked', f'{thing} choked on his own tongue',
                         f'{thing} drank too much anti-freeze', f'{thing} tried to fly', f'{thing} drowned in jello',
                         f'{thing} was walking across quicksand with an anvil', f'{thing} got stabbed with a cucumber',
                         f'{thing} ate medicine out of date']
            await ctx.send(f'\n{random.choice(responses)}')

    @commands.command()
    async def roll(self, ctx):
        responses = ['The dice landed on 1', 'The dice landed on 2', 'The dice landed on 3', 'The dice landed on 4',
                     'The dice landed on 5', 'The dice landed on 6',
                     'Roll again. It landed sideways. Why are you rolling on discord anyway? Roll on a flat surface.']
        embed = discord.Embed(
            title=f'{random.choice(responses)}',
            colour=discord.Colour.blue()
        )
        embed.set_thumbnail(
            url='https://media.discordapp.net/attachments/696121556119715890/703780627446628372/dice.png')
        embed.set_footer(text=f'Requested by {ctx.author}')
        await ctx.send(embed=embed)

    @commands.command()
    async def coinflip(self, ctx):
        embed = discord.Embed(
            title='Coinflip',
            colour=discord.Colour.blue()
        )
        responses = random.choice([
                                      'https://media.discordapp.net/attachments/625842127284469760/708375437457490101/139362185558690588heads-md.png',
                                      'https://media.discordapp.net/attachments/625842127284469760/708375634384125962/1393621733287511319tails-md.png'])
        embed.set_image(url=responses)
        embed.set_footer(text=f'Requested by {ctx.author}')
        await ctx.send(embed=embed)

    @commands.command()
    async def lenny(self, ctx):
        await ctx.send('( ͡° ͜ʖ ͡°)')
        await ctx.message.delete()

    @commands.command()
    async def quote(self, ctx):
        responses = [
            'The difference between the master and the student is that the master has failed more than the student has tried',
            'Fools speak cause they have to say something wise, men speak because they have something to say',
            'The darkest  shadows are made by the brightest lights',
            'One man can be seen as a villain to some and a hero to others', 'There are no accidents -MASTER OOGWAY',
            'Deception is the key to knowledge or destruction',
            'Laziness is the  mother of all bad habits but ultimately she is a mother and we should respect her',
            'The Knight who jumps too far falls prey to a pawn', 'Loneliness is not eternal but  happiness could be',
            'All warfare is based of deception', 'Honor and pride don’t matter, you win you win',
            'History tends to rewrite itself', 'I have not failed 10,000 I just found 10000 that won’t work',
            'In all situations of life strategy is needed but not all situations in life need power, speed, or money',
            'Its either people change or they die before they do, could be for the better or the worse',
            'Im selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to handle. But if you cant handle me at my worst, then you sure as hell dont deserve me at my best.',
            'Two things are infinite: the universe and human stupidity; and Im not sure about the universe.',
            'Be who you are and say what you feel, because those who mind dont matter, and those who matter dont mind.',
            'You only live once, but if you do it right, once is enough.']
        embed = discord.Embed(
            title='Quote',
            description=f'{random.choice(responses)}',
            colour=discord.Colour.blue()
        )
        embed.set_footer(text=f'Requested by {ctx.author}')
        await ctx.send(embed=embed)

    @commands.command()
    async def fact(self, ctx):
        responses = [
            'The average person will spend six months waiting for red lights to turn green.',
            'A bolt of lightning contains enough energy to toast 100,000 slices of bread.',
            'You can hear a blue whales heartbeat two miles away',
            'Nearly 30,000 rubber ducks were lost at sea in 1992 and are still being discovered.',
            'The inventor of the frisbee was turned into a frisbee after he died',
            'Instead of saying "cheese" before taking a picture, Victorians said "prunes"',
            'Roosters have built-in earplugs.', 'The netherlands is so safe, it imports criminals to fill jails',
            'Coke saved one town from the Deppresion', 'You can smell rain.',
            'A wild dog is the most successful predator.', 'Medicine bottle foil exists because of poison.',
            'Cold water is just as cleansing as hot water',
            'Glitter was accidentally invented by a New Jersey cattle rancher.',
            'Hawaiian pizza was invented by a Greek man in Canada', 'Wild boars wash their food',
            'Walmart accepts fewer applicants than Harvard.', 'The world’s first cosmonaut was a dog.',
            'More than half the world’s population is under 30.',
            'A day is longer than a year on Venus.', 'The world’s oldest operational hotel was built in 705AD.',
            'The word “radar” is an acronym.',
            'There’s a tarantula named after Johnny Cash.', 'Russia was founded by Vikings',
            'Armadillos are bulletproof.', 'Abraham Lincoln was a licensed bartender.',
            'Penicillin was originally called “mold juice”.', 'All blue-eyed people have a common ancestor.',
            'A toddler could fit inside a blue whale’s arteries.',
            'There are more than 200 dead bodies on Mount Everest',
            'Workers are most productive on Mondays.',
            'The idea of Sunday as a day of rest was started by a Roman emperor.',
            'Did you know carrots weren’t always orange?',
            'The human eye can detect the light of a candle from over a mile away.',
            '80% of taste is determined by aroma.', 'About 99.9% of human genes are identical',
            'The scientific name for a stomach grumble is “borborygmi”.',
            'The oldest “your mom” joke dates from ancient Babylonia.',
            'Penguin urine makes up about 3% of Antarctica’s glaciers',
            'Dolly Parton once lost to a man in a Dolly Parton look-alike contest.',
            'The sandwich was invented so a noble could gamble longer.',
            'The name for the fear of long words is 36 letters long.',
            'Nutella was originally invented as a way to stretch chocolate rations.', 'Rats can laugh.',
            'Flamingoes aren’t really pink.', 'The word “freelancer” was originally a synonym for “mercenary.”',
            'Candyland was invented to entertain kids hospitalized for polio.',
            'A cat named Sweet Tart is the Mayor of Omena, Michigan.',
            'There is a medical procedure to remove the sense of fear.',
            'Every panda in a zoo around the world is on loan from China.',
            'Medical errors are the third-leading cause of death in the United States.',
            'Sliced bread wasn’t invented until 1928.', 'enghis Khan has about 16 million living descendants.',
            'Hippopotamuses kill more people each year than lions, sharks, and wolves combined.',
            'Grapes are toxic to dogs.',
            'The ancient Greeks may have used computers.',
            'More than 3 billion people watched the 2014 FIFA World Cup.',
            'Only two countries use purple in their national flag.', 'Wombats have cube-shaped poop.',
            'Footprints left on the moon’s surface will last for a million years',
            'Some snakes can sense when an earthquake is coming.',
            'The green sea slug is part plant and part animal.', 'Roundworms can survive over 30,000 frozen in ice.',
            'There are over two dozen states of matter.', 'Killer whales aren’t really whales.',
            '90% of the world’s fresh water is in Antarctica.',
            'The largest natural cave is twice the size of Wembley Stadium.',
            'A pregnant woman can give birth after death.',
            'The average human body is home to between 2 and 6 pounds of bacteria.',
            'Thursday is “Teacher’s Day” in Buddhist Thailand.',
            'September 19th is International Talk like a Pirate Day.',
            'Saturday is the only Germanic day name derived from a Roman god.',
            'here’s a pickle festival every July in Pittsburgh.', 'Tuesday is the most common day to apply for a job.',
            'Bread is sacred in Uzbekistan.',
            'Chewing on ice could be a sign of anemia.',
            'The average person’s body gives off enough heat in 30 minutes to boil a gallon of water.',
            'Graffiti was found in the ruins of Pompeii.', 'Australia is wider than Pluto.',
            'Shakespeare invented more than 1,700 words.',
            'Some starfish can regenerate a new body from a single severed arm.',
            'eland’s population still hasn’t fully recovered from the potato famine.',
            'The human brain can process 50,000 times more data than the most powerful supercomputer.',
            'It is impossible  to sneeze with your eyes open,', 'Dolphins have names.',
            'Neptune was discovered mathematically before it was observed.',
            'You can survive longer without food than you can without sleep.',
            'he average person’s skin completely replaces itself about 900 times in their lifetime.',
            '2/3 of the people who have ever lived to be 65 are alive today.',
            'On average, a person will walk 115,000 miles in their life.',
            'People with bigger brains have more friends.',
            'Engineering students at Purdue University built a machine to find out how many licks it takes to get to the center of a Tootsie Pop',
            'France didn’t stop doing executions by guillotine until 1977.',
            'There’s a garbage patch in the Pacific Ocean three times the size of France.',
            'The founding fathers got wasted during the Constitutional Convention.',
            'A mouse can fit through a hole the width of a #2 pencil.',
            'It rains fish at least once a year in the Honduran city of Yoro.',
            'The largest living creature in the world is a fungus.',
            'There is a church in Argentina that worships a soccer player.',
            'The first Native American to greet the pilgrims already spoke English.',
            'High heels were originally worn by men.', 'Scientist Neil DeGrasse Tyson was a dancer in college.',
            'Bread was invented in Egypt around 8,000 BC.', 'Freddie Mercury was born in Africa.',
            '26 nations have a 100% adult literacy rate.',
            'The Florida Everglades are the only place you can find both alligators and crocodiles.',
            'Cows have accents.', 'Chameleons change color based on mood, not their surroundings.',
            'Koala fingerprints are nearly identical to a human’s.', 'Ghost crabs growl using teeth in their stomachs.',
            'There are over 800 languages spoken in Papua New Guinea.',
            'One city in Pakistan produces about half the world’s soccer balls.',
            'More twins are born in Nigeria than anywhere else in the world.',
            'Nobody knows how many islands are in Indonesia.',
            'Uganda is home to over 1,000 species of birds.', 'It rains diamonds on Jupiter.', 'Mercury is shrinking',
            'When two pieces of the same metal touch in space, they bond permanently.',
            'Neutron stars spin as fast as 600 times a second.', 'The Milky Way galaxy is on a collision course.',
            'It’s illegal to cut down a cactus in Arizona.', 'Georgia has an official state possum.',
            'More than 20% of the popcorn in the U.S. comes from Indiana.',
            'Kentucky was originally a county of Virginia.', 'There is a 40-acre desert in Maine.',
            'Melbourne, Australia used to be called Batmania.', 'Denver is the only city to turn down the Olympics.',
            'There’s an entire city of tunnels under Toronto, Canada.',
            'Chicago’s nickname isn’t based on its weather.',
            'A highway in Lancaster, California plays the “William Tell Overture.”']

        embed = discord.Embed(
            title='Fact',
            description=f'{random.choice(responses)}',
            colour=discord.Colour.blue()
        )
        embed.set_footer(text=f'Requested by {ctx.author}')
        await ctx.send(embed=embed)

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question=None):
        if question == None:
            await ctx.send(
                f'What answers do you seek from the Great 8ball?\n\nCorrect Usage:\n`{Prefix.getprefix(ctx.guild)}8ball <question>`')
        else:
            responses = ['Certainly', 'Maybe..', 'Without a doubt', 'Yes-definitely.', 'As I see, yes', 'Most likely',
                         'Sign points to yes', 'Sign points to no', 'Of course not',
                         'This is a question even an 8ball cannot answer.']
            embed = discord.Embed(
                title=f'{question}',
                description=f'{random.choice(responses)}',
                colour=discord.Colour.blue()
            )
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/696772245166620774/703698122697605271/image-removebg-preview.png')
            await ctx.send(embed=embed)

    @commands.command()
    async def say(self, ctx, *, thing=None):
        if thing == None:
            await ctx.send(
                f'What does The Great and Wise {ctx.author.name} say?\n\nCorrect Usage:\n{Prefix.getprefix(ctx.guild)}say <anything>')
        else:
            await ctx.send(f'A wise {ctx.author.name} once said: {thing}')
            await ctx.message.delete()

    @commands.command()
    async def rps(self, ctx, choice=None):
        if choice == 'paper':
            responses = (['I won! I chose **scissors**', 'I lost! I chose **rock**', 'We tied! I chose **paper**'])
            embed = discord.Embed(
                title='Rock, Paper, Scissors',
                description=(random.choice(responses)),
                colour=discord.Colour.blue()
            )
            embed.set_footer(text=f'Played with {ctx.author}')
            await ctx.send(embed=embed)
        if choice == None:
            await ctx.send(
                f'Well how do I play with you if you are not gonna select a choice?\n\nCorrect Usage:\n`{Prefix.getprefix(ctx.guild)}rps <rock, paper, or scissors>`')
        if choice == 'rock':
            responses = ['I win! I chose **paper**', 'I lost! I chose **scissors**', 'We tied! I chose **rock**']
            embed = discord.Embed(
                title='Rock, Paper, Scissors',
                description=(random.choice(responses)),
                colour=discord.Colour.blue()
            )
            embed.set_footer(text=f'Played with {ctx.author}')
            await ctx.send(embed=embed)
        if choice == 'scissors':
            responses = ['I won! I chose **rock**', 'I lost! I chose **paper**', 'We tied! I chose **scissors**']
            embed = discord.Embed(
                title='Rock, Paper, Scissors',
                description=(random.choice(responses)),
                colour=discord.Colour.blue()
            )
            embed.set_footer(text=f'Played with {ctx.author}')
            await ctx.send(embed=embed)

    @commands.command(
        aliases=['idontcare', 'nobodyasked', 'ididntask', 'whoasked', 'whocares', "didiask", "idontrememberasking"])
    async def nobodycares(self, ctx, dude=None):
        if dude == None:
            embed = discord.Embed(
                title='Looks like nobody asked..',
                colour=discord.Colour.blue()

            )
            responses = random.choice([
                                          'https://media.discordapp.net/attachments/625842127284469760/712803081682944030/looking-for-where-i-asked-for-your-opinion-21405696.png',
                                          'https://media.discordapp.net/attachments/625842127284469760/712803090000248913/s-l1000.png?width=569&height=569',
                                          'https://media.discordapp.net/attachments/625842127284469760/712803129917177986/67d.png',
                                          'https://media.discordapp.net/attachments/625842127284469760/712803170375696474/me-looking-for-who-asked-for-your-opinion-cant-seem-3765173.png?width=454&height=568',
                                          'https://media.discordapp.net/attachments/625842127284469760/712803213564182538/remember-when-asked-for-your-opinion-yea-me-neither-4736818.png',
                                          'https://media.discordapp.net/attachments/625842127284469760/712803261983227924/image.png?width=433&height=569',
                                          'https://media.discordapp.net/attachments/625842127284469760/712803642612121670/unknown.png',
                                          'https://media.discordapp.net/attachments/625842127284469760/712804035249569924/image0.jpg?width=571&height=569',
                                          'https://media.discordapp.net/attachments/625842127284469760/712804129889845300/unknown.png',
                                          'https://cdn.discordapp.com/attachments/675896760585027588/714531080438415460/image0.png',
                                          'https://cdn.discordapp.com/attachments/625842127284469760/714527973725700096/image0.jpg',
                                          'https://cdn.discordapp.com/attachments/625842127284469760/714527230017142884/image0.png',
                                          'https://media.discordapp.net/attachments/675896760585027588/717731270037078116/image0_copy_3.png?width=509&height=538',
                                          'https://media.discordapp.net/attachments/675896760585027588/717731241268609084/image0.png',
                                          'https://media.giphy.com/media/VkICFY01bWIeI/source.gif',
                                          'https://media.discordapp.net/attachments/700094917468356668/720858606798372934/image0.png?width=611&height=574',
                                          'https://media.discordapp.net/attachments/700094917468356668/720858529212268584/image0.png?width=983&height=519',
                                          'https://media.discordapp.net/attachments/700094917468356668/720858514658164836/image_search_1591936399980.jpg?width=674&height=574',
                                          'https://media.discordapp.net/attachments/700094917468356668/720858514515427328/image_search_1591936417223.jpg',
                                          'https://media.discordapp.net/attachments/700094917468356668/720858514330746960/image_search_1591936413418.jpg',
                                          'https://media.discordapp.net/attachments/700094917468356668/720858514137940008/image_search_1591936403964.jpg',
                                          'https://media.discordapp.net/attachments/700094917468356668/720858513928224838/image_search_1591936423935.jpg',
                                          'https://media.discordapp.net/attachments/700094917468356668/720858459842674701/image0.png',
                                          'https://media.discordapp.net/attachments/700094917468356668/720858427190149120/image0.png',
                                          'https://media.discordapp.net/attachments/713600868834082819/722983485626777640/unknown.png',
                                          'https://media.discordapp.net/attachments/713600868834082819/722965884120858644/image2.jpg',
                                          'https://media.discordapp.net/attachments/713600868834082819/722965273203835040/image1.jpg',
                                          'https://media.discordapp.net/attachments/713600868834082819/722965272851513424/image0.jpg?width=491&height=573',
                                          'https://images-ext-1.discordapp.net/external/TWLUDAHzXTTWDa1uE8G-u97tfxeoq7823RAwnJy4c1o/https/i.redd.it/foqy8fo93be41.jpg?width=612&height=573'])
            embed.set_image(url=responses)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Looks like nobody asked, {dude}',
                colour=discord.Colour.blue()

            )
            responses = random.choice([
                                          'https://media.discordapp.net/attachments/625842127284469760/712803081682944030/looking-for-where-i-asked-for-your-opinion-21405696.png',
                                          'https://media.discordapp.net/attachments/625842127284469760/712803090000248913/s-l1000.png?width=569&height=569',
                                          'https://media.discordapp.net/attachments/625842127284469760/712803129917177986/67d.png',
                                          'https://media.discordapp.net/attachments/625842127284469760/712803170375696474/me-looking-for-who-asked-for-your-opinion-cant-seem-3765173.png?width=454&height=568',
                                          'https://media.discordapp.net/attachments/625842127284469760/712803213564182538/remember-when-asked-for-your-opinion-yea-me-neither-4736818.png',
                                          'https://media.discordapp.net/attachments/625842127284469760/712803261983227924/image.png?width=433&height=569',
                                          'https://media.discordapp.net/attachments/625842127284469760/712803642612121670/unknown.png',
                                          'https://media.discordapp.net/attachments/625842127284469760/712804035249569924/image0.jpg?width=571&height=569',
                                          'https://media.discordapp.net/attachments/625842127284469760/712804129889845300/unknown.png',
                                          'https://cdn.discordapp.com/attachments/675896760585027588/714531080438415460/image0.png',
                                          'https://cdn.discordapp.com/attachments/625842127284469760/714527973725700096/image0.jpg',
                                          'https://cdn.discordapp.com/attachments/625842127284469760/714527230017142884/image0.png',
                                          'https://media.discordapp.net/attachments/675896760585027588/717731270037078116/image0_copy_3.png?width=509&height=538',
                                          'https://media.discordapp.net/attachments/675896760585027588/717731241268609084/image0.png',
                                          'https://media.giphy.com/media/VkICFY01bWIeI/source.gif',
                                          'https://media.discordapp.net/attachments/700094917468356668/720858606798372934/image0.png?width=611&height=574',
                                          'https://media.discordapp.net/attachments/700094917468356668/720858529212268584/image0.png?width=983&height=519',
                                          'https://media.discordapp.net/attachments/700094917468356668/720858514658164836/image_search_1591936399980.jpg?width=674&height=574',
                                          'https://media.discordapp.net/attachments/700094917468356668/720858514515427328/image_search_1591936417223.jpg',
                                          'https://media.discordapp.net/attachments/700094917468356668/720858514330746960/image_search_1591936413418.jpg',
                                          'https://media.discordapp.net/attachments/700094917468356668/720858514137940008/image_search_1591936403964.jpg',
                                          'https://media.discordapp.net/attachments/700094917468356668/720858513928224838/image_search_1591936423935.jpg',
                                          'https://media.discordapp.net/attachments/700094917468356668/720858459842674701/image0.png',
                                          'https://media.discordapp.net/attachments/700094917468356668/720858427190149120/image0.png',
                                          'https://media.discordapp.net/attachments/713600868834082819/722983485626777640/unknown.png',
                                          'https://media.discordapp.net/attachments/713600868834082819/722965884120858644/image2.jpg',
                                          'https://media.discordapp.net/attachments/713600868834082819/722965273203835040/image1.jpg',
                                          'https://media.discordapp.net/attachments/713600868834082819/722965272851513424/image0.jpg?width=491&height=573',
                                          'https://images-ext-1.discordapp.net/external/TWLUDAHzXTTWDa1uE8G-u97tfxeoq7823RAwnJy4c1o/https/i.redd.it/foqy8fo93be41.jpg?width=612&height=573'])
            embed.set_image(url=responses)
            await ctx.send(embed=embed)

    @commands.command()
    async def bet(self, ctx, choice=None):
        if choice == None:
            await ctx.send(
                f'**Please choose a number between 1-6**.\n\nCorrect Usage: `{Prefix.getprefix(ctx.guild)}bet <number>`')
        if choice == '1':
            responses = ['I rolled **1**, we tied..', 'I rolled **2**, I win!', 'I rolled 3, I win!',
                         'I rolled **4**, I win!', 'I rolled **5**, I win!', 'I rolled **6**, I win!']
            await ctx.send(random.choice(responses))
        if choice == '2':
            responses = ['I rolled **1**, I lost!', 'I rolled **2**, we tied..', 'I rolled **3**, I won!',
                         'I rolled **4**, I won!', 'I rolled **5**, I won!', 'I rolled **6**, I won!']
            await ctx.send(random.choice(responses))
        if choice == '3':
            responses = ['I rolled **1**, I lost!', 'I rolled **2**, I lost!', 'I rolled **3**, we tied..',
                         'I rolled **4**, I won!', 'I rolled **5**, I won!', 'I rolled **6**, I won!']
            await ctx.send(random.choice(responses))
        if choice == '4':
            responses = ['I rolled **1**, I lost!', 'I rolled **2**, I lost', 'I rolled **3**, I lost!',
                         'I rolled **4**, we tied..', 'I rolled **5**, I  won!', 'I rolled **6**, I won!']
            await ctx.send(random.choice(responses))
        if choice == '5':
            responses = ['I rolled **1**, I lost!', 'I rolled **2**, I lost!', 'I rolled **3**, I lost!',
                         'I rolled **4**, I lost!', 'I rolled **5**, we tied..', 'I rolled **6**, I won!']
            await ctx.send(random.choice(responses))
        if choice == '6':
            bruhs = ['I rolled **1**, I lost!', 'I rolled **2**, I lost!', 'I rolled **3**, I lost!',
                     'I rolled **4**, I lost!', 'I rolled **5**', 'I  lost!', 'I rolled **6**, we tied..']
            await ctx.send(random.choice(bruhs))
        if int(choice) > 6:
            await ctx.send('That is an invalid number! Please select a number beteween 1-6')
        if int(choice) < 0:
            await ctx.send('That is an invalid number! Please select a number beteween 1-6')

    @commands.command()
    async def ship(self, ctx, person, prsn):
        percent = random.choice(
            ['1%', '2%', '10%', '20%', '40%', '50%', '30%', '60%', '70%', '80%', '90%', '0%..', '100%!!'])
        await ctx.send(f'***Matchmaking Machine***\n\n`{person}` | `{prsn}`\n\n**{percent}**')

    @commands.command(aliases=['telephone'])
    async def phone(self, ctx, person=None, *, swkd=None):
        if swkd == None:
            await ctx.send(
                f'**Who do you want to call and what do you want to say?**\n\nCorrect Usage:`{Prefix.getprefix(ctx.guild)}phone <person> <message>`')
        else:
            if person == None:
                await ctx.send(
                    f'**Who do you want to call and what do you want to say?**\n\nCorrect Usage:`{Prefix.getprefix(ctx.guild)}phone <person> <message>`')
            else:
                responses = random.choice(
                    ['Go away..', 'Why are you calling me?', 'Leave me alone', 'Omg no way!', "I couldn't care less..",
                     '**hangs up**', 'Hello, your computer has virus. Call 810-666-6666 to block this', 'uh.. IM gAy'])
                embed = discord.Embed(
                    title='📱Calling on the telephone.. 📱',
                    description=f'Calling {person}',
                    colour=discord.Colour.blue()
                )
                embed.add_field(name='**What you said**', value=f'{swkd}', inline=False)
                embed.add_field(name='**Their response**', value=f'{responses}')
                await ctx.send(embed=embed)

    @commands.command()
    async def sort(self, ctx, *, dude):
        house = random.choice(['Hufflepuff', 'Ravenclaw', 'Gryffindor', 'Slytherin', 'Muggle'])
        embed = discord.Embed(
            title='The Sorting Hat',
            description=f"{dude} has been sorted into **{house}**!",
            colour=discord.Colour.blue()
        )
        embed.set_thumbnail(
            url="http://images.amcnetworks.com/bbcamerica.com/wp-content/uploads/2014/12/sortinghat.jpg")
        await ctx.send(embed=embed)

    @commands.command()
    async def idiotsandwich(self, ctx):
        embed = discord.Embed(
            title="An idiot sandwich..",
            colour=discord.Colour.blue()
        )
        embed.set_image(url="https://media.giphy.com/media/3o85xnoIXebk3xYx4Q/source.gif")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(fun(bot))