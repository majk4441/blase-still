# funfuct, this is the actual main blase file 

import discord

from utils import default
from utils.data import Bot, HelpFormat

config = default.config()
print("Logging in")

bot = Bot(
    command_prefix=config["prefix"], prefix=config["prefix"],
    owner_ids=config["owners"], command_attrs=dict(hidden=True), help_command=HelpFormat(),
    allowed_mentions=discord.AllowedMentions(roles=False, users=True, everyone=False),
    intents=discord.Intents( 
        guilds=True, members=True, messages=True, reactions=True, presences=True, message_content=True,
    )
)

try:
    bot.run(config["token"])
except Exception as e:
    print(f"Error when logging at: {e}")