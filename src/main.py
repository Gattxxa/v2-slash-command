from discord import Intents, Object
from discord.ext import commands

TOKEN = 'YourDiscordBotTOKEN'
GUILD_ID = 1234567890


# Implementation
class SampleBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='/', intents=Intents.default())

    async def setup_hook(self):
        # Global Slash Commands
        GLOBAL_EXTENSION_COGS_ = ['cogs.global.sample']
        for gec in GLOBAL_EXTENSION_COGS_:
            await self.load_extension(gec)
        await bot.tree.sync(guild=None)

        # Guild Slash Commands
        GUILD_EXTENSION_COGS_ = ['cogs.guild.myname', 'cogs.guild.calc']
        for gec in GUILD_EXTENSION_COGS_:
            await self.load_extension(gec)
        await bot.tree.sync(guild=Object(id=GUILD_ID))


if __name__ == '__main__':
    bot = SampleBot()
    bot.run(TOKEN)
