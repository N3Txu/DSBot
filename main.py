import discord
from discord.ext import commands
import requests
from dotenv import load_dotenv
import os
import BotServer

load_dotenv()

intents = discord.Intents.default() 
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

TOKEN = os.getenv('DSTOKEN')

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

@bot.command()
async def poke(ctx, arg):
    try:
        pokemon = arg.split(" ",1)[0].lower()
        result = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
        if result.status_code != 200:
            await ctx.send(f'Pokémon {pokemon} not found.')
        else:
            image_url = result.json()['sprites']['front_default']
            print(f"Image URL: {image_url}")
            await ctx.send(image_url)
    except Exception as e:
        print(f"Error: {e}")
        
@poke.error
async def poke_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please provide a Pokémon name.')
    else:
        await ctx.send('An error occurred while processing your request.')
        
@bot.command()
async def clear(ctx):
    if ctx.author.guild_permissions.manage_messages:
        await ctx.channel.purge(limit=100)
        await ctx.send('Chat cleared!', delete_after=2)
    else:
        await ctx.send('You do not have permission to clear the chat.')
        
BotServer.keep_alive()
print("Starting BotServer...")
bot.run(TOKEN)