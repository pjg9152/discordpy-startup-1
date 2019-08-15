# -*- coding: utf-8 -*-
import discord
import asyncio

client = discord.Client()

# ログを削除する処理
@client.event
async def on_message(message):
    await asyncio.sleep(86400)
    count = 0
    while count < 5:
        try:
            await client.delete_message(message)
            print("%sの発言を削除しました"%message.author.name)
            break
        except:
            count += 1
            print("発言の削除失敗%d回目"%count)
            await asyncio.sleep(30)
@client.event
async def on_message(message):
    if message.content == '!clean':
        if message.author.guild_permissions.administrator:
            await message.channel.purge()
            await message.channel.send('スイープしたじょ🎵')
        else:
            await message.channel.send('何様のつもり？')

client.run("NDU2NDUxNDI0ODU5OTc5Nzc4.DgYFqA.5Mc8q9y9nWU8kSvvBAhp6BNGfD4")
