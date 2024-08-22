# import discord

# from pass_gen import gen_pass

# Variabel intents menyimpan hak istimewa bot
# intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
# intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
# client = discord.Client(intents=intents)
# @client.event
# async def on_ready():
#     print(f'Kita telah masuk sebagai {client.user}')
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#     if message.content.startswith('$halo'):
#         await message.channel.send("Hi!")
#     elif message.content.startswith('$bye'):
#         await message.channel.send("\\U0001f642")
#     elif message.content.startswith('$genpass'):
#         await message.channel.send(gen_pass(10))    
#     else:
#         await message.channel.send(message.content)

# client.run("")

import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def guess(ctx):
    await ctx.send('Guess a number between 1 and 10.')

@bot.command()
async def answer(ctx,n):
    if n == random.randint(1,10):
        await ctx.send('Good Job!')
    else:
        await ctx.send('Try Again!')

bot.run("")
 
