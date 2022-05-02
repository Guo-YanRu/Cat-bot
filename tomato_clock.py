import g

from discord import channel
from discord_buttons_plugin import *
import os
from dotenv import load_dotenv
import asyncio
from datetime import datetime
import traceback

# 開始計時&設定循環長度
async def tomato_clock(message, study_minute, rest_minute):
    global point  
    global exp  
    global i
    try:
        print(study_minute,rest_minute)
        
        
        
        i =  0
        while(i < 5):
            await message.channel.send('Start studying')
            g.exp += study_minute*5
            #額外積分區
            if study_minute <= 30:    
                g.point += (2+i)              
            elif study_minute <= 40:   
                g.point += (3+i)             
            elif study_minute <= 50:    
                g.point += (4+i) 
            else:
                g.point += (5+i)                 
            await asyncio.sleep(int(study_minute)*2)  
            await message.channel.send('Study time is up')
            print('exp, point', g.exp, g.point)
            i += 1  
        
            await message.channel.send('break or continue?')
            channel = message.channel
            def check(m):   
                return (m.content in ['break', 'continue'] and m.channel == channel)
                # 如果你們希望使用者回傳 continue 和 break 
                # 可以用 x in ['1', '2']

            msg = await g.bot.wait_for('message', check = check)
            print(msg, msg.content, type(msg))

        # 我也覺得是ww
        # 不過為什麼continue之後是接結束 這是正常的ㄇ><
        # >< 不是 bugQQ
        #不正常吧? 
        #好神奇(? 那好像是語法
        # 因為 L62 的 if 剛剛寫錯哦 ._. 沒教 class 真的慘QwQ
         
            '''
            choice = ('Break or Continue? ') # 持續上次週期
            while(choice != 'Break' and choice != 'Continue'):
                await message.channel.send('Choose Break or Continue. Try again.')
             ''' 
            
            # 不奇怪吧 是 https://discordpy.readthedocs.io/en/stable/api.html?highlight=wait_for#discord.Message
            # 這裡要用 msg.content owo 喔喔了解
            if(msg.content == "continue"):
                await message.channel.send('Start resting ') 
                start_rest_time = datetime.now()
                print(start_rest_time)
                #user_start_time['user'].append(message.author)
                #user_start_time['start_rest_time'].append(start_rest_time)
                await asyncio.sleep(int(rest_minute)*5)  
                await message.channel.send('Rest time is up')
                continue
            else:
                await message.channel.send('結束')
                break           
            
    except Exception as e:  #驗證輸入為整數
    # 這裡要把 exception 印出來吧
        await message.channel.send('錯誤')
        print(traceback.print_exc())
        # tomato_clock()
        