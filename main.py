import g
import discord
import os
from dotenv import load_dotenv
import asyncio
from datetime import datetime
import traceback

#貓貓區chi & fish

# 需要存取 global variable 的 module #拆分檔案區
from tomato_clock import tomato_clock
from get_rest_time import get_rest_time
from music import music_handler
#from cat_img import cat_image
a = []

def level_up():   #升等 
    if g.exp >= g.exp_max:
        g.level += 1
        g.exp -= g.exp_max  #重置經驗值 
        g.exp_max = g.exp_max * 3 + 22    #暫定
'''
def exp_change():
    global exp
    exp += study_minute 
    return exp        
'''
'''
def change_pic():
    if level == 1:
'''
#儲存使用者開始休息時間及查詢時時間        
user_start_time={
    'user':[],
    'start_rest_time':[],
}
user_now_time={
    'user':[],
    'now_rest_time':[],
}


#指令區(prefix)
@g.bot.event
async def on_message(message):
    try:
        await music_handler(message)
    except:
        traceback.print_exc()
    if message.author == g.bot.user:
        return

    #help 使用說明
    if message.content == g.prefix + "help":
        embed = discord.Embed(title="歡迎使用 貓貓番茄鐘", description="這是一隻幫助你專心讀書的貓咪，使用^^加上下列指令即可開始使用")
        embed.add_field(name="^^study <讀書時間> <休息時間> ", value="設定番茄鐘循環時間並開始讀書", inline=False)
        embed.add_field(name="^^resttime", value="查看剩餘休息時間", inline=False)
        embed.add_field(name="^^rounds", value="查看今日連續循環數", inline=False)
        embed.add_field(name="^^checkpoint", value="查看當前積分", inline=False)
        embed.add_field(name="^^checkexp", value="查看當前經驗值", inline=False)
        embed.add_field(name="^^checklevel", value="查看當前等級", inline=False)
        embed.add_field(name="^^musiclist", value="加入語音並檢視音樂選單", inline=False) 
        embed.add_field(name="^^play <曲目編號>", value="撥放所選音樂", inline=False)
        embed.add_field(name="^^pause", value="暫停音樂", inline=False)
        embed.add_field(name="^^resume", value="重新開始撥放音樂", inline=False)
        embed.add_field(name="^^stop", value="停止音樂", inline=False)
        await message.channel.send(embed=embed)
    
    #checktime 查看剩餘休息時間(先決條件要先下study指令且目前為休息時間)
    if message.content == g.prefix+"resttime":
        global now_rest_time
        global start_rest_time
        now_rest_time = datetime.now()
        user_now_time['user'].append(message.author) # message.author
        user_now_time['now_rest_time'].append(now_rest_time)
        get_rest_time( message , start_rest_time , now_rest_time)
    #checkpoint 查看當前積分
    if message.content == g.prefix+"checkpoint":#好
    # builtins 的東西可以直接在 global 被找到
        await message.channel.send(f"你目前的積分為: **{g.point}**\n可以兌換：功能一 **{1}** 次、功能二 **{1}** 次") 
    #checkexp 查看當前經驗值
    if message.content == g.prefix+"checkexp":
        level_up()
        #exp_change()
        await message.channel.send(f"你目前的經驗值為: **{g.exp}** ，距離第 **{g.level+1}** 級還需要 **{g.exp_max-g.exp}** 點經驗值 \n加油，再去多念點書吧，喵ฅ•ω•ฅ")
    #checklevel 查看當前等級
    if message.content == g.prefix+"checklevel":
        level_up()
        await message.channel.send(f"你目前的等級為: **{g.level}** 級貓咪，升級以解鎖更多造型，喵ฅ•ω•ฅ")
        #pic = discord.File(f"{level}.jpg")
        catpic = {
            'l1': "https://i.imgur.com/R30VNgp.jpg",
            'l2': "https://i.imgur.com/utbU2oB.jpg",
            'l3': "https://i.imgur.com/go7VT3Z.jpg",
            'l4': "https://i.imgur.com/LBMBsiM.jpg",
            'l5': "https://i.imgur.com/B3zoSWm.jpg",
            'l6': "https://i.imgur.com/VeywLEF.jpg",
            'l7': "https://i.imgur.com/2oLF6S9.jpg",
            'l8': "https://i.imgur.com/9rIvBgk.jpg",
            'l9': "https://i.imgur.com/BeiJDNk.jpg",
            'l10': "https://i.imgur.com/VeywLEF.jpg"
        }
        await message.channel.send(catpic[f'l{g.level}'])
    #study 設定番茄鐘循環時間並開始讀書  (格式 ^^study (分1) (分2))
    instructment = message.content.split(' ')[0]
    if instructment == g.prefix + "study" :
        try:
            global study_minute
            global rest_minute
            study_minute = int(message.content.split(' ')[1])   
            rest_minute = int(message.content.split(' ')[2])    
    
            print(study_minute)
            print(rest_minute)
            await tomato_clock(message,study_minute, rest_minute)
            g.exp += study_minute * g.i
            
        except Exception as e:
            await message.channel.send('請輸入整數數字:')
            print('Error:', traceback.print_exc())
            # 可以參考 https://docs.python.org/3/tutorial/errors.html#defining-clean-up-actions
            # divide 的範例和你們要的東西應該差不多
    

#optional區(有時間的話再做的區)
#進出通知Hao
# import discord
# intents = discord.Intents.default()
# intents,typing = False
# intents.presences = False

@g.bot.event
async def on_ready():
    g.channel = g.bot.get_channel(id=871443387352498282)
    await g.channel.send(">>bot is online<<")

@g.bot.event
async def on_member_join(member):
    await g.channel.send("f'{member}join!")

@g.bot.event
async def on_member_remove(member):
    await g.channel.send("f'{member}leave!") 

if __name__ == "__main__":
    load_dotenv()
    g.bot.run(os.getenv("TOKEN"))


