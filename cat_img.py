"""
#圖片區 hao
async def cat_image(message):  
    l1 = "https://i.imgur.com/R30VNgp.jpg"
    l2 = "https://i.imgur.com/utbU2oB.jpg"
    l3 = "https://i.imgur.com/go7VT3Z.jpg"
    l4 = "https://i.imgur.com/LBMBsiM.jpg"
    l5 = "https://i.imgur.com/B3zoSWm.jpg"
    l6 = "https://i.imgur.com/VeywLEF.jpg"
    l7 = "https://i.imgur.com/2oLF6S9.jpg"
    l8 = "https://i.imgur.com/9rIvBgk.jpg"
    l9 = "https://i.imgur.com/BeiJDNk.jpg"
    l10= "https://i.imgur.com/VeywLEF.jpg"
    if message.author == bot.user:
        return
    
    if message.content == prefix+" l1 " and level == 1:#這裡的level可以讀取到嗎? 應該可，因為我沒放在def裡面
        await message.channel.send(" your cat is at level 1 ",fild=discord.File(""))#圖1
    
    elif message.content == prefix+" l2 " and level == 2:
        await message.channel.send(" your cat is at level 2 ",fild=discord.File(""))#圖2
    
    elif message.content == prefix+" l3 " and level == 3:
        await message.channel.send(" your cat is at level 3 ",fild=discord.File("test.jpg"))#圖3
    
    elif message.content == prefix+" l4 " and level == 4:
        await message.channel.send(" your cat is at level 4 ",fild=discord.File("test.jpg"))#圖4
    
    elif message.content == prefix+" l5 " and level == 5:
        await message.channel.send(" your cat is at level 5 ",fild=discord.File("test.jpg"))#圖5

    elif message.content == prefix+" l6 " and level == 6:
        await message.channel.send(" your cat is at level 6 ",fild=discord.File("test.jpg"))#圖6
        
    elif message.content == prefix+" l7 " and level == 7:
        await message.channel.send(" your cat is at level 7 ",fild=discord.File("test.jpg"))#圖7
    
    elif message.content == prefix+" l8 " and level == 8:
        await message.channel.send(" your cat is at level 8 ",fild=discord.File("test.jpg"))#圖8

    elif message.content == prefix+" l9 " and level == 9:
        await message.channel.send(" your cat is at level 9 ",fild=discord.File(""))#圖9
    
    elif message.content == prefix+" l10 " and level == 10:
        await message.channel.send(" your cat is at level 10 ",fild=discord.File("l10"))#圖10
    
"""