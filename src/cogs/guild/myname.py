from discord import app_commands, Object
from discord.ext import commands

from main import GUILD_ID


# Guild Command - MyName
class MyName(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # /myname
    @app_commands.command(
        name='myname',
        description='コマンド使用者の名前を表示します。')
    async def myname(self, ctx):
        your_name = f'あなたの名前は{ctx.user.name}！'
        await ctx.response.send_message(your_name)


async def setup(bot):
    await bot.add_cog(MyName(bot), guilds=[Object(id=GUILD_ID),])
