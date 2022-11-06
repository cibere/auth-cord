import discord
from discord.ext import commands

import auth_cord


# we can create an instance of our authcord instance in setup_hook
class MyBot(commands.Bot):
    async def setup_hook(self) -> None:
        auth = auth_cord.Authorization(
            client_id=123, client_secret="...", redirect_url="..."
        )
        # creating our actual client variable, and setting it to a botvar so we can access anywhere else in the bot
        self.oauth2 = auth_cord.Client(auth)


intents = discord.Intents.default()
intents.message_content = True
bot = MyBot(command_prefix=">", intents=intents)


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


bot.run("token")
