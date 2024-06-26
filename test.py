import discord
from discord.ext import commands
from dotenv import load_dotenv
import os 
load_dotenv()
# Initialize bot
intents = discord.Intents.default()
intents.members = True  # Required to fetch member info
bot = commands.Bot(command_prefix='!', intents=intents)

# Runs when Bot Succesfully Connects
@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

@bot.command()
async def square(ctx, arg): # The name of the function is the name of the command
    print(arg) # this is the text that follows the command
    await ctx.send(int(arg) ** 2) # ctx.send sends text in chat

@bot.command()
async def ping(ctx): # The name of the function is the name of the command
    await ctx.send("pong GITHUB (render)") # ctx.send sends text in chat
    
@bot.event
async def on_message(message):
    # Make sure the Bot doesn't respond to it's own messages
    if message.author == bot.user: 
        return
    
    if message.content == 'hello':
        await message.channel.send(f'Hi {message.author}')
    if message.content == 'bye':
        await message.channel.send(f'Goodbye {message.author}')

    await bot.process_commands(message)
TOKEN = os.getenv("TOKEN1")
bot.run(TOKEN)
