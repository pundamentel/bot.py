import discord
from discord.ext import commands
from bot import gen_pass
from sigmalogic import coinflip
import random

intents = discord.Intents.default()
intents.message_content = True


client = commands.Bot(command_prefix='$', intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

     
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("Bye!")
    elif message.content.startswith('$gen'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$coinflip'):
        await message.channel.send(coinflip())
    elif message.content.startswith('$heh'):
        if len(message.content) > 4:
            count_heh = int(message.content[4:])
        else:
            count_heh = 5
        await message.channel.send("he" * count_heh)
    
    

    
    
    await client.process_commands(message)

@client.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@client.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

client.run("token")
