#-------------------------------------------------------------------------------------------
import discord, asyncio
import random, datetime, os, time, datetime
from discord import *
from discord.ext import commands
#-------------------------------------------------------------------------------------------
with open('ScoBot_old\\TOKEN.txt') as f:
  token= f.readline()
client = discord.Client()
p = ";"
ver = "0.23"
ready = f'''
-------------------------------------------------------
ScoBot has been activated. / ver {ver}
스코봇
814035803974008904
-------------------------------------------------------
'''
#-------------------------------------------------------------------------------------------
@client.event
async def on_ready():
  
  print(ready)
  print(str(len(client.guilds)) + '개의 서버에서 봇이 작동중입니다.\n')
  print('ScoBot_Server_log')
  f = open("C:\\Users\\Administrator\\Desktop\\Workspace\Python\\ScoBot\\ScoLog.txt", 'a', encoding='UTF8')
  f.write("ScoBot_log - " + str(datetime.datetime.now())[0:19] + " : ScoBot Started\n")
  f.close()
  '''
  await client.get_channel(844107317527576616).send(embed=embed)
   # online - 온라인                     
   # do_not_disturb - 다른 용무 중               
   # idle - 자리 비움
   # offline                
  ''' 
  await bt([';help, ;h, ;도움', '스코봇 0.23'])
async def bt(games):
  await client.wait_until_ready()
  while not client.is_closed():
      for g in games:
          await client.change_presence(status = discord.Status.online, activity = discord.Game(g))
          await asyncio.sleep(5)
        
@client.event
async def on_message(message):
  if message.author.bot:
    return None
# 테스트 명령어들
  if message.content == f"{p}help" or message.content == f"{p}h" or message.content == f"{p}도움":
    embed=discord.Embed(title=f"스코봇 {ver}", description="아래 숫자 버튼을 누르면 자세히 확인 할 수 있습니다!", color=0x62c1cc)
    embed.set_thumbnail(url=client.user.avatar_url)
    embed.add_field(name="도움", value="```;help, ;h, ;도움```", inline=False)
    embed.add_field(name="1 Page", value="```테스트 명령어 설명을 볼 수 있어요.```", inline=False)
    embed.add_field(name="2 Page", value="```명령어들 설명을 볼 수 있어요.```", inline=False)
    embed.add_field(name="3 Page", value="```관리 명령어 설명을 볼 수 있어요.```", inline=False)
    embed.add_field(name=";helpmd", value="```전체 명령어 목록 & 에러 코드 도움말을 내보내요.```", inline=False)
    embed.set_footer(text="With StrangeCode")
    msg=await message.channel.send(embed=embed)
    reaction_msg = ['1️⃣', '2️⃣', '3️⃣']
    for r in reaction_msg:
      await msg.add_reaction(r)
    def check(reaction, user):
            return str(reaction) in reaction_msg and user == message.author and reaction.message.id == msg.id
    try:
          reaction, _user = await client.wait_for("reaction_add", check=check, timeout=15)
    except asyncio.TimeoutError:
            pass
    else:
            if str(reaction) == '1️⃣':
                embed=discord.Embed(title="스코봇 Help", description="테스트용 명령어들이에요.", color=0x62c1cc)
                embed.set_thumbnail(url=client.user.avatar_url)
                embed.set_footer(text="1 Page")
                embed.add_field(name=";test", value="```스코봇이 정상 작동중인지 테스트해요. DM 메세지로 와요.```", inline=False)
                embed.add_field(name="스코봇", value="```스코봇을 불러와요.```", inline=False)
                embed.add_field(name=";ping", value="```스코봇의 현재 접속 상태를 나타내요.```", inline=False)
                await msg.edit(embed=embed)

            if str(reaction) == '2️⃣':
                embed=discord.Embed(title="스코봇 Help", description="명령어들이에요.", color=0x62c1cc)
                embed.set_thumbnail(url=client.user.avatar_url)
                embed.set_footer(text="2 Page")
                embed.add_field(name=";주사위", value="```1~6의 랜덤 수를 출력해요.```", inline=False)
                embed.add_field(name=";time, ;시간", value="```현재 시간을 나타내요.```", inline=False)
                embed.add_field(name=";tts", value="```입력된 메세지를 tts로 읽어줘요.```", inline=False)
                embed.add_field(name=";타자연습", value="```타자연습을 진행해요. (0.2 신규 업데이트!)```", inline=False)
                await msg.edit(embed=embed)

            if str(reaction) == '3️⃣':
                embed=discord.Embed(title="스코봇 Help", description="관리 명령어들이에요.", color=0x62c1cc)
                embed.set_thumbnail(url=client.user.avatar_url)
                embed.set_footer(text="3 Page")
                embed.add_field(name=";ivt, ;초대", value="```봇 초대 링크를 출력해요.```", inline=False)
                embed.add_field(name=";pn, ;패치노트", value="```스코봇 패치노트를 불러와요.```", inline=False)
                embed.add_field(name=";sctl", value="```strangecode discord방 링크를 출력해요.```", inline=False)
                embed.add_field(name=";del", value="```a개의 메세지를 삭제해요. (;del a)```", inline=False)
                await msg.edit(embed=embed)
            else:
                pass
            return
  if message.content == f"{p}helpmd":
    file = discord.File("C:\\Users\\Administrator\\Desktop\\Workspace\\Python\\ScoBot\\Source\\helpmd.md")
    await message.channel.send(file=file)

  if message.content == f"{p}test":
    await message.author.send("ScoBot - 테스트를 시작합니다.")
    f = open("C:\\Users\\Administrator\\Desktop\\Workspace\Python\\ScoBot\\ScoLog.txt", 'a', encoding='UTF8')
    f.write("ScoBot_log - " + str(datetime.datetime.now())[0:19] + " : Tested By" + str(message.author))
    await message.author.send("스코봇 로그 파일 접근 성공...33%")
    f.close()
    file = discord.File("C:\\Users\\Administrator\\Desktop\\Workspace\\Python\\ScoBot\\Source\\helpmd.md")
    test1 = await message.author.send(file=file)
    await asyncio.sleep(2)
    await test1.delete()
    await message.author.send(";helpmd 접근 성공...66%")
    file = discord.File("C:\\Users\\Administrator\\Desktop\\Workspace\\Python\\ScoBot\\Source\\patchnotes.md")
    test2 = await message.author.send(file=file)
    await asyncio.sleep(2)
    await test2.delete()
    await message.author.send(";patchnotes 접근 성공...99%")
    await asyncio.sleep(1.9)
    await message.author.send("```테스트 - 스코봇 정상 작동 중```")

  if message.content == "스코봇":
    embed=discord.Embed(title="스코봇", color=0x62c1cc)
    embed.set_thumbnail(url=client.user.avatar_url)
    embed.add_field(name="스코봇이 왔어요^.^", value=f"{message.author.mention}님, 안녕하세요.", inline=True)
    await message.channel.send(embed=embed)
  
  if message.content == f"{p}ping":
    embed=discord.Embed(title="ScoBot ping", description=str(client.latency*1000)[0:6] + 'ms', color=0x37ff00)
    await message.channel.send(embed=embed)
# 명령어들
  if message.content == f"{p}주사위":
    result = random.randint(1, 6)
    await message.channel.send(f":package:{result}")

  if message.content == f"{p}time" or message.content == f"{p}시간" :
    await message.channel.send(":alarm_clock:현재 시간입니다.")
    await message.channel.send(datetime.datetime.now())

  if message.content.startswith(f"{p}tts"):
    msgtts = message.content.split(" ")[1:]
    await message.channel.send(msgtts, tts=True)

  if message.content == f"{p}타자연습":
    scotaja=0
    embed=discord.Embed(title="스코봇 타자연습", color=0x000000)
    embed.set_thumbnail(url=client.user.avatar_url)
    embed.add_field(name="3초 후 10회의 타자게임을 시작합니다.", value=f"10초 안에 해당 문장을 적어주세요. / 종료하기 위해선 아무 말이나 적어주세요.", inline=False)
    channel = message.channel
    msg1 = await message.channel.send(embed=embed)
    await asyncio.sleep(3)
    while scotaja < 11:
      f = open('ScoBot_old\\Source\\Typing.txt', 'rt', encoding='UTF8')
      randomLine = random.choice(list(f.readlines())).splitlines()[0]
      await message.channel.send(randomLine)
      def check(m):
        return m.author == message.author and m.channel == channel
      try:
        msg2 = await client.wait_for('message', timeout=10.0, check=check)
      except asyncio.TimeoutError:
        embed=discord.Embed(title="스코봇 타자연습", color=0x000000)
        embed.set_thumbnail(url=client.user.avatar_url)
        embed.add_field(name="타자게임 종료", value=f"10초의 시간제한이 끝났습니다! 다시 도전해주세요!", inline=False)
        await message.channel.send(embed=embed)
        return
      else:
        bot_prov=str(randomLine)
        user_prov=str(msg2.content)
        anwser = ""
        if bot_prov == user_prov:
          if scotaja == 10:
            await message.channel.send(":star: 타자연습 완료! :star:")
            break
          else:
            await message.channel.send("맞았습니다!")
            msg2 = 'empty'
            scotaja += 1
        else:
          embed=discord.Embed(title="스코봇 타자연습", color=0x000000)
          embed.set_thumbnail(url=client.user.avatar_url)
          embed.add_field(name="타자게임 종료", value="틀렸습니다! 다시 도전해주세요!", inline=False)
          await message.channel.send(embed=embed)
          scotaja += 55
    f.close()
# 관리
  if message.content == f"{p}pn" or message.content == f"{p}패치노트":
    file = discord.File("C:\\Users\\Administrator\\Desktop\\Workspace\\Python\\ScoBot\\Source\\patchnotes.md")
    await message.channel.send(file=file)

  if message.content == f"{p}ivt" or message.content == f"{p}초대":
    embed=discord.Embed(title=f"ScoBot {ver} 초대 링크", color=0x000000)
    embed.set_thumbnail(url=client.user.avatar_url)
    embed.add_field(name="관리자 초대하기 (권장)", value="https://discord.com/api/oauth2/authorize?client_id=814035803974008904&permissions=8&scope=bot", inline=False)
    embed.add_field(name="기본으로 초대하기", value="https://discord.com/api/oauth2/authorize?client_id=814035803974008904&permissions=0&scope=bot", inline=False)
    await message.channel.send(embed=embed)

  if message.content == f"{p}sctl":
    await message.channel.send("https://discord.gg/BFC74CerQj")

  if message.content.startswith(f"{p}del"):
    number = int(message.content.split(" ")[1])
    await message.delete()
    await message.channel.purge(limit=number)
    await message.channel.send(f"{message.author.mention}님, {number}개의 메세지가 삭제되었습니다.")

# log
@client.event
async def on_message_delete(message):
	print("ScoBot_log-" + str(datetime.datetime.now())[0:19] + " : " + str(message.author) + " deleted " + "\'" + str(message.content) + "\'")
	return

client.run(token)

# await message.author.send("응답") - DM 발신
# await ctx.author.send("응답") - DM 발신
'''
@tasks.loop(seconds=5)
async def change_status():
    await LOD.change_presence(activity=discord.Game(next(playing)), status=discord.Status.online)
playing = cycle([p+"help", "두번쨰"])
change_status.start()
'''