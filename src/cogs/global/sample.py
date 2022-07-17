from discord import app_commands
from discord.ext import commands


# Global Command - Sample
class SampleCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Make '/samplebot' Group
    samplebot = app_commands.Group(name='samplebot', description='コマンドグループ')

    # /samplebot calc num_a* num_b* num_c
    # *: require
    @samplebot.command(
        name='calc',
        description='与えられた数を足し算します。（グローバル）')
    @app_commands.describe(
        num_a='足される値（必須）', 
        num_b='足す値その１（必須）',
        num_c='足す値その２')
    async def calc(self, ctx, num_a:int, num_b:int, num_c:int=0):
        calc_result = f'{num_a}+{num_b}+{num_c} = {num_a + num_b + num_c}'
        await ctx.response.send_message(calc_result)
    
    # /samplebot myname
    @samplebot.command(
        name='myname',
        description='コマンド使用者の名前を表示します。（グローバル）')
    async def myname(self, ctx):
        your_name = f'あなたの名前は{ctx.user.name}！'
        await ctx.response.send_message(your_name)


async def setup(bot):
    await bot.add_cog(SampleCommands(bot))