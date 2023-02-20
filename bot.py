#(not)real main blase file
import discord, json
from utils import default, permissions
from utils.data import Bot
from discord.ext import commands

config = default.config()
color = discord.Color.light_gray()

bot = Bot(
    command_prefix=config["prefix"], prefix=config["prefix"],
    owner_ids=config["owners"], command_attrs=dict(hidden=True),
    allowed_mentions=discord.AllowedMentions(roles=False, users=False, replied_user=False, everyone=False),
    intents=discord.Intents( 
        guilds=True, members=True, messages=True, reactions=True, presences=True, message_content=True,
    )
)

try:
    bot.run(config["token"])
except Exception as e:
    print(f"Error when logging at: {e}")
