import discord

token = 'Nzk0MTE0ODQyNTc5MzA0NDU4.X-2HFA.4E3yiS5mxgWq6T67i9U572XSs3o'

client = discord.Client()

@client.event
async def on_ready():
    print('起動しました')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if '。' in message.content:
        return
    if message.content == 'いってきます':
        await message.channel.send('いってら！今日もがんばれ👍')
    if message.content == '勉強する':
        await message.channel.send('了解！勉強がんばれ👍')
    if message.content == 'おはよう' or message.content == 'おはす' or message.content == 'おはやう' or message.content == 'おはすー' or message.content == 'おはょ' or message.content == 'おはよ' or message.content == 'おはよー':
        await message.channel.send('おは！今日も一日がんばれ👍')
    if message.content == 'おやすみ' or message.content == 'おやすみー' or message.content == 'おやす' or message.content == 'おやすー' or message.content == 'good night' or message.content == 'おやすみぃ':
        await message.channel.send('おう！おやすみ！睡眠がんばれ👍')
    if message.content == 'こんにちは' or message.content == 'こんにちはー' or message.content == 'こんちゃ' or message.content == 'こんちゃす' or message.content == 'こんちゃすー' or message.content == 'Hi' or message.content == 'Hello':
        await message.channel.send('こんちゃ！頑張ってるかい？応援するぜ！がんばれ👍')
    if message.content == 'こんばんは' or message.content == 'こんばんはー':
        await message.channel.send('こんばんは！まだ今日は終わってないぞ！がんばれ👍')
    if message.content == 'ただいまー' or message.content == 'ただいま' or message.content == 'おかえり' or message.content == 'おかえりぃ':
        await message.channel.send('おかえりぃ！頑張れたかい？')
    if message.content == 'がんばる' or message.content == '頑張る' or message.content == 'がんばる！' or message.content == '頑張る！' or message.content == 'がんばろう！' or message.content == '頑張ろう！' or message.content == 'がんばろう' or message.content == '頑張ろう' or message.content == 'がんばれ👍':
        await message.channel.send('がんばれ👍！')
    if message.content == 'がんばれ君' :
        await message.channel.send('呼んだ？')
    if message.content == 'がんばれ' or message.content == '頑張れ' or message.content == 'がんばれ！' or message.content == '頑張れ！':
        await message.channel.send('俺も応援するぜ！がんばれ👍')
    if message.content == 'がんばった' or message.content == 'がんばったよ':
        await message.channel.send('よく頑張った！今後もがんばれ👍')
    if '/p' in message.content:
        plus_list_str = message.content.split()
        plus_list_str.remove('/p')
        plus_list = map(int, plus_list_str)
        plus = sum(plus_list)
        await message.channel.send(plus)
    if '/m' in message.content:
        minus_list2_str = message.content.split()
        minus_list2_str.remove('/m')
        minus_str = minus_list2_str[0]
        minus1 = int(minus_str)
        minus_list2_str.remove(minus_list2_str[0])
        minus_list2 = map(int, minus_list2_str)
        minus_list = [i * -1 for i in minus_list2]
        minus2 = sum(minus_list)
        minus = minus1 + minus2
        await message.channel.send(minus)
    if '/t' in message.content:
        time_list_str = message.content.split()
        time_list_str.remove('/t')
        time_list = map(int, time_list_str)
        time = reduce(lambda x, y: x * y, time_list)
        await message.channel.send(time)
    if '/d' in message.content:
        divide0, divide1_str, divide2_str = message.content.split()
        divide1 = int(divide1_str)
        divide2 = int(divide2_str)
        divide = divide1 / divide2
        await message.channel.send(divide)
    if 'o' in message.content:
        oio0, oio1_str, oio2_str = message.content.split( )
        oio1 = int(oio1_str)
        oio2 = int(oio2_str)
        oio = oio1 % oio2
        ii = oio1 // oio2
        iioio = f'{ii}あまり{oio}'
        await message.channel.send(iioio)
    if '/x' in message.content:
        xx0, xx1_str, xx2_str == message.content.split()
        xx1 = int(xx1_str)
        xx2 = int(xx2_str)
        xx = xx1 ** xx2
        await message.channel.send(xx)

client.run(token)
