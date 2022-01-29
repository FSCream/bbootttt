import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='d!')
TOKEN = 'OTM2OTkzMjQyMDMxOTkyOTQz.YfVQ9Q.yVDnSyeRNUMM2w-gKWE5wfq9UEE'

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('신우가 좋아하는 국자를 수제작 하는 중'))
    print('[알림][봇이 정상적으로 구동되었습니다!]')

@bot.event
async def on_massage(msg):
    if msg.author.bot: return None
    await bot.process_commands(msg)

@bot.command()
async def 안녕(ctx):
    await ctx.channel.send('반말하지 마세요')

@bot.command()
async def 삭제(ctx):
    await ctx.channel.purge(limit=10)
    await ctx.channel.send('최근에 보낸 메세지 10개를 삭제했어요')

@bot.command()
async def 소개(ctx):
    embed = discord.Embed(title='제 소개를 해드릴게요!')
    await ctx.channel.send(embed=embed)

@bot.command()
async def 입장(ctx):
    if not ctx.author.voice:
        return
    await ctx.author.voice.channel.connect()

@bot.command()
async def 퇴장(ctx):
    if not ctx.author.voice or not ctx.voice_client:
        return
    await ctx.voice_client.disconnect()

@bot.command()
async def 재생(ctx):

bot.run('OTM2OTkzMjQyMDMxOTkyOTQz.YfVQ9Q.yVDnSyeRNUMM2w-gKWE5wfq9UEE')