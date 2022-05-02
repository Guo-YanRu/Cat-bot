import g

import discord
from discord_buttons_plugin import *
from dotenv import load_dotenv


#取得剩餘休息時間  
async def get_rest_time(message,start_rest_time, now_rest_time):
    print(start_rest_time)
    print(now_rest_time)
    start_time = start_rest_time
    now_time = now_rest_time
    time = now_time - start_time
    await message.channel.send(f'Elapsed: {time} ')

    