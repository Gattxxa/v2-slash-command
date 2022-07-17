from discord import app_commands, Object
from discord.ext import commands

from main import GUILD_ID


# Guild Command - Calc
class Calc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # /calc num_a* num_b* num_c
    # *: require
    @app_commands.command(
        name='calc',
        description='与えられた数を足し算します。')
    @app_commands.describe(
        num_a='足される値（必須）', 
        num_b='足す値その１（必須）',
        num_c='足す値その２')
    async def calc(self, ctx, num_a:int, num_b:int, num_c:int=0):
        calc_result = f'{num_a}+{num_b}+{num_c} = {num_a + num_b + num_c}'
        await ctx.response.send_message(calc_result)


async def setup(bot):
    await bot.add_cog(Calc(bot), guilds=[Object(id=GUILD_ID),])
