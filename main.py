# -----{ Imports requirements }-----
import discord
from discord.ext import commands
import os  # default module
from dotenv import load_dotenv
import tweepy

# ----------{ Global variables }----------
guild_id = '954021637060173884'
guild_id_test = '961268598800777286'  # Testing

api_key = str(os.getenv('T_API_KEY'))
api_key_secret = str(os.getenv('T_API_KEY_TOKEN'))
bearer_token = str(os.getenv('BEARER_TOKEN'))
access_token = str(os.getenv('T_ACCESS_SECRET'))
access_token_secret = str(os.getenv('T_ACCESS_SECRET_TOKEN'))

# Tweepy setup
client = tweepy.Client(bearer_token=bearer_token,
                       consumer_key=api_key,
                       consumer_secret=api_key_secret,
                       access_token=access_token,
                       access_token_secret=access_token_secret)

'''
auth = tweepy.OAuth1UserHandler(
    'pKb6leDVN4DOvRKG8IFRxuqnD',
    'fF2L1WgWOKB6akAc25cs4PnYMGboxPgIHtkPDPe5qokvbwP7yE',
    '1288088636408373250-xvRhVEwu4JLDHzYUj1Lm4jBZ6XCvtB',
    'uTpKqUttQ8Xkb9OwjfWf9a45Zn2MTSCeyBQ224Eo5gKVN'
)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print('Tweepy connected.')
except:
    print('Tweepy connection failed.')
'''

# Discord setup
load_dotenv()  # load all the variables from the env file
bot = commands.Bot(guild_ids=[guild_id, guild_id_test],
                   command_prefix="/",
                   intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("---------------------------------------------------")
    print("RRC - Code Generator, bot is loaded & ready to use!")
    print(f"{bot.user} is online & Watching {len(bot.guilds)} servers.")
    print("---------------------------------------------------")


cogFiles = []
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        cogFiles.append("cogs." + filename[:-3])

for cogFile in cogFiles:
    try:
        print("Loading file " + cogFile)
        bot.load_extension(cogFile)
    except Exception as err:
        print(err)

bot.run(os.getenv('TOKEN'))
