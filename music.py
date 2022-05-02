import g

import youtube_dl
import opuslib
import discord
#from discord_buttons_plugin import *
from discord import FFmpegPCMAudio
import requests


#放讀書音樂(研究中)
async def music_handler(message):
    if message.author == g.bot.user:
        return
    '''
    join voice channel and show music list
    '''
    if message.content == g.prefix + "musiclist":
        if message.author.voice is None: # 使用者沒有連線到語音
            await message.channel.send('請加入語音頻道')    
            
        if message.guild.voice_client is None: # bot沒有連線到語音
            await message.author.voice.channel.connect()    # bot做連線動作
        else:
            embed=discord.Embed(title="選擇學習音樂", description="使用^^ play <曲目編號> 來選擇歌曲")
            embed.add_field(name="1", value="rain white noise", inline=False)
            embed.add_field(name="2", value="coffe shop white noise", inline=False)
            embed.add_field(name="3", value="study lo-fi", inline=False)
            embed.add_field(name="4", value="study jazz", inline=False)
            await message.channel.send(embed=embed)

        if message.guild.voice_client.channel != message.author.voice.channel:    # bot和使用者連到不同語音頻道
            await message.guild.voice_client.move_to(message.author.voice.channel)# 那else就是不連線的狀況?
        else:
            embed=discord.Embed(title="選擇學習音樂", description="使用^^ play <曲目編號> 來選擇歌曲")
            embed.add_field(name="1", value="rain white noise", inline=False)
            embed.add_field(name="2", value="coffe shop white noise", inline=False)
            embed.add_field(name="3", value="study lo-fi", inline=False)
            embed.add_field(name="4", value="study jazz", inline=False)
            await message.channel.send(embed=embed)

    voice = discord.utils.get(g.bot.voice_clients, guild=message.guild)
    '''        
    play music
    '''
    if message.content.split(' ')[0] == g.prefix + "play":
        musiclist = [
            'https://www.youtube.com/watch?v=buqt6_CjtuI',
            'https://www.youtube.com/watch?v=gaGrHUekGrc',
            'https://www.youtube.com/watch?v=_DYAnU3H7RI',
            'https://www.youtube.com/watch?v=_DYAnU3H7RI'
        ]

        songnum = int(message.content.split(' ')[1])
        #Solves a problem I'll explain later

        FFMPEG_OPTS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        
        url = musiclist[songnum-1]
        with youtube_dl.YoutubeDL({'format': 'bestaudio', 'noplaylist':'True'}) as ydl:
            r = ydl.extract_info(url, download=False)
            source = r['formats'][0]['url']
            # print('source', source)
        #voiceplay = get(message.voice_client, guild=message.guild)

        #await join(ctx, voice)
        #await ctx.send(f'Now playing {info['title']}.')

        voice.play(FFmpegPCMAudio(source, **FFMPEG_OPTS), after=lambda e: print('done', e))
        # print('is_playing', voice.is_playing())

    '''
    pause music
    '''
    #voice = discord.utils.get(message.voice_client, guild=message.guild)
    if message.content == g.prefix+ "pause":
        if voice.is_playing():
            voice.pause()
        else:
            await message.channel.send("目前無音樂正在撥放")
    '''
    resume music
    '''
    #voice = discord.utils.get(message.voice_client, guild=message.guild)
    if message.content == g.prefix+ "resume":
        if voice.is_paused():
            voice.resume()
        else:
            await message.channel.send("目前無音樂在暫停狀態")

    '''
    stop music
    '''
    #voice = discord.utils.get(message.voice_client, guild=message.guild)
    if message.content == g.prefix+ "stop":
        voice.stop()
        await voice.disconnect()
        await message.channel.send("音樂已停止")





        

#songlist
'''
rain white noise
https://www.youtube.com/watch?v=buqt6_CjtuI
coffee shop white noise
https://www.youtube.com/watch?v=gaGrHUekGrc
study lofi
https://www.youtube.com/watch?v=_DYAnU3H7RI
study jazz
https://www.youtube.com/watch?v=Y-JQ-RCyPpQ
'''

#source code from youtube
'''
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegPCMAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/watch?v=buqt6_CjtuI'])
    
    source = FFmpegPCMAudio() ###
    player = voice.play(source)
'''
#get video info from youtube
'''
from youtube_dl import YoutubeDL
from requests import get

#Get videos from links or from youtube search
def search(query):
    with YoutubeDL({'format': 'bestaudio', 'noplaylist':'True'}) as ydl:
        try: requests.get(arg)
        except: info = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
        else: info = ydl.extract_info(arg, download=False)
    return (info, info['formats'][0]['url'])
'''
#play the music video
'''
from discord import FFmpegPCMAudio
from discord.ext import commands
from discord.utils import get


@bot.command()
async def play(ctx, *, query):# query=搜尋網只/關鍵字
    #Solves a problem I'll explain later
    FFMPEG_OPTS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    video, source = search(query)
    voice = get(bot.voice_clients, guild=ctx.guild)#done

    #await join(ctx, voice)
    #await ctx.send(f'Now playing {info['title']}.')

    voice.play(FFmpegPCMAudio(source, **FFMPEG_OPTS), after=lambda e: print('done', e))
    voice.is_playing()
'''






#await message.VoiceChannel.connect(*, timeout=60.0 , reconnect=True , cls=<class 'discord.voice_client.VoiceClient'> )

        
#ytdl.download(['https://www.youtube.com/watch?v=buqt6_CjtuI'], filter: 'audioonly')
#discord.VoiceState.channel 用戶在的語音頻道/None
#discord.VoiceChannel

#// 播放音樂
#this.dispatcher[guildID] = this.connection[guildID].play(ytdl(musicInfo.url, { filter: 'audioonly' }));
#await connect( * , timeout=60.0 , reconnect=True , cls=<class 'discord.voice_client.VoiceClient'> )
        
#這邊是別人打的我參考用而已
'''
async def _check_ignore_non_voice(self, msg):
    if msg.guild.me.voice:
        vc = msg.guild.me.voice.channel
    else:
        vc = None

    # If we've connected to a voice chat and we're in the same voice channel
    if not vc or (msg.author.voice and vc == msg.author.voice.channel):
        return True
    else:
        raise exceptions.PermissionsError(
            "you cannot use this command when not in the voice channel (%s)" % vc.name, expire_in=30)
'''


