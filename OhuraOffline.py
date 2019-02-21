#coding: utf-8
import discord
import random
import threading
from time import sleep

client = discord.Client()
server_channel_ID = 546568411317010433
server_channel = discord.Object(id=server_channel_ID)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    

#---------------------------てめぇなんだ？

#dictにリストされたてめぇなんだ？を数える関数
def dict_count(output):
    output = len(dict)
    return output

#てめぇなんだ？がコメントされるとここにリストされる
dict = []

#-------ダメです

dict2_mini1 = "ダメです"
dict2_mini2 = "ダメですダメですダメですダメです"
dict2_mini3 = "ダメですダメですダメですダメですダメですダメですダメですダメですダメですダメですダメですダメですダメですダメですダメですダメですダメですダメですダメですダメです"
dict2_mini4 = "ダメですダメですダメですダメですダメですダメですダメですダメですダメですダメです"
dict2_mini5 = "かなりいいぞ"

dict2 = [dict2_mini1,dict2_mini2,dict2_mini3,dict2_mini4,dict2_mini5]

#-------俺も行くか

dict3_mini1 = "ダメですダメですダメですダメですダメですダメですダメですダメですダメですダメですダメですダメですダメですダメですダメですダメですダメですダメですダメですダメですダメですダメですダメですダメです"
dict3_mini2 = "ああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ"
dict3_mini3 = "はああああああああああああああああああああああああああああああああああああああｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱｱ"

dict3 = [dict3_mini1,dict3_mini2,dict3_mini3]


#-------投票

tohyo_list = ["https://media.discordapp.net/attachments/545881286976339970/545930214618955776/makasenasai02.gif",
"https://media.discordapp.net/attachments/545881286976339970/545930204879519744/makasenasai01.gif",
"https://media.discordapp.net/attachments/545881286976339970/545935116166365184/makasenasai05.gif",
"https://media.discordapp.net/attachments/545881286976339970/545935103671402497/makasenasai04.gif"]

title_setup_01 = False
title_setup_02 = False
title_setup_03 = False
title_setup_04 = False

tohyo_setup_01 = False
tohyo_setup_02 = False
tohyo_setup_03 = False

time_setup_01 = False

Choices = {}

rank_number = 0

@client.event
async def on_message(message):
    if message.content.startswith("!初期化"):
        return

    #画像シリーズ
    if message.content.startswith("二足歩行") or message.content.startswith("歩行不可"):
        if client.user != message.author: 
            filepath = "C:\Program1\Source\Dl64cH6UcAE.png"
            await client.send_file(message.channel,filepath)
    if message.content.startswith("ブス") or message.content.startswith("どっちかっていうと"):
        if client.user != message.author: 
            filepath2 = "C:\Program1\Source\Busu.jpg"
            await client.send_file(message.channel,filepath2)

    #てめえなんだ？シリーズ
    if message.content.startswith("てめぇなんだ？") or message.content.startswith("てめえなんだ？"):
        if client.user != message.author: 
            dict.append(message.author)
            last_count = str(dict.count(message.author))
            send = message.author.name + "は" + last_count + "回てめぇなんだ？を使いました"
            await client.send_message(message.channel, send)
            if int(last_count) >= 3 and int(last_count) <= 6:
                butigire_send = "何回目だよ。ブチギレるぞ"
                await client.send_message(message.channel, butigire_send)
            elif int(last_count) >= 7:
                butigire_send2 = "おめぇここでぇじょうぶか？"
                await client.send_message(message.channel, butigire_send2)
            else:
                butigire_send3 = "約束が違うぜ"
                await client.send_message(message.channel, butigire_send3)

    #ダメですシリーズ
    if message.content.startswith("ダメです"):
        if client.user != message.author: 
            dame = random.choices(dict2,k=1)
            send2 = str(dame).replace("['","").replace("']","")
            await client.send_message(message.channel, send2)

    #俺も行くかシリーズ
    if  message.content.startswith("俺も行くか") or message.content.startswith("さっ") or message.content.startswith("俺もいくか"):
        if client.user != message.author: 
            dame2 = random.choices(dict3,k=1)
            send3 = str(dame2).replace("['","").replace("']","")
            await client.send_message(message.channel, send3 * 5)
            
    #投票システム
    if message.content.startswith("!投票"):
        if client.user != message.author:
            send_tohyo_01 = "投票ね、お姉ちゃんに任せなさ～い！"
            tohyo_list_random = random.choices(tohyo_list,k=1)
            send_tohyo_01_p = str(tohyo_list_random).replace("['","").replace("']","")
            await client.send_message(message.channel, send_tohyo_01)
            await client.send_message(message.channel, send_tohyo_01_p)
            send_tohyo_02 = "何を投票したいの？ まずは [タイトル:〇〇] 形式でタイトルを入力してね！"
            sleep(1)
            await client.send_message(message.channel, send_tohyo_02)
            #ローカル関数として処理される為、グローバル宣言を忘れないこと
            global title_setup_01
            title_setup_01 = True
    if message.content.startswith("タイトル:"):
        if client.user != message.author:
            if title_setup_01 == True:
                title = message.content.replace("タイトル:","")
                send_tohyo_03 = "じゃあこれから「" + title + "」について投票するよ！"
                await client.send_message(message.channel, send_tohyo_03)
                sleep(1)
                send_tohyo_04 = "選択肢は「3つ」作ってね"
                await client.send_message(message.channel, send_tohyo_04)
                sleep(1)
                send_tohyo_05 = "--------------------------------------------------------"
                await client.send_message(message.channel, send_tohyo_05)
                send_tohyo_06 = "まず一つめ！ [選択肢1:] 形式で入力してね！"
                await client.send_message(message.channel, send_tohyo_06)
                title_setup_01 = False
                global title_setup_02
                title_setup_02 = True
    if message.content.startswith("選択肢1:"):
        if client.user != message.author:
            if title_setup_02 == True:
                global Choice01
                Choice01 = message.content.replace("選択肢1:","")
                send_tohyo_07 = "一つめの選択肢は「" + Choice01 + "」だね！"
                await client.send_message(message.channel, send_tohyo_07)
                sleep(1)
                send_tohyo_08 = "じゃあ二つめ！ 同じ形式で入力してね！（選択肢2:～）"
                await client.send_message(message.channel, send_tohyo_08)
                title_setup_02 = False
                global title_setup_03
                title_setup_03 = True
                Choices[Choice01] = 1
    if message.content.startswith("選択肢2:"):
        if client.user != message.author:
            if title_setup_03 == True:
                global Choice02
                Choice02 = message.content.replace("選択肢2:","")
                send_tohyo_09 = "二つめの選択肢は「" + Choice02 + "」だね！"
                await client.send_message(message.channel, send_tohyo_09)
                sleep(1)
                send_tohyo_10 = "最後の三つめだよ！"
                await client.send_message(message.channel, send_tohyo_10)
                title_setup_03 = False
                global title_setup_04
                title_setup_04 = True
                Choices[Choice02] = 1
    if message.content.startswith("選択肢3:"):
        if client.user != message.author:
            if title_setup_04 == True:
                global Choice03
                Choice03 = message.content.replace("選択肢3:","")
                send_tohyo_11 = "最後の選択肢は「" + Choice03 + "」だね！"
                await client.send_message(message.channel, send_tohyo_11)
                Choices[Choice03] = 1
                sleep(1)
                send_tohyo_10 = "--------------------------------------------------------"
                await client.send_message(message.channel, send_tohyo_10)
                title_setup_04 = False
                for Choices_name in Choices:
                    global rank_number
                    rank_number += 1
                    send_tohyo_12 = str(rank_number) + ":  " + Choices_name
                    await client.send_message(message.channel, send_tohyo_12)
                rank_number = 0
                send_tohyo_13 = "--------------------------------------------------------"
                await client.send_message(message.channel, send_tohyo_13)
                #全処理後にChoicesを初期化すること（投票機能を使用する度に辞書が肥大化するため）
                send_tohyo_14 = "これから投票を開始するよ！"
                await client.send_message(message.channel, send_tohyo_14)
                send_tohyo_15 = "投票の仕方だよ！ \n\n ★" + Choice01 + "　→　[投票1] ★  \n ★" + Choice02 + "　→　[投票2]★ \n ★" + Choice03 + "　→　[投票3]★ \n\n と入力してね！ \n \n 投票はこれから15秒後に締め切られるから注意してね！"
                await client.send_message(message.channel, send_tohyo_15)
                global tohyo_setup_01
                tohyo_setup_01 = True
                global time_setup_01
                time_setup_01 = True
    #投票開始
    if message.content.startswith("投票1"):
            if client.user != message.author:
                if tohyo_setup_01 == True:
                    Choices[Choice01] += 1 
                    send_tohyo_16 = "選択肢1の" + Choice01 + "に1投票"
                    print(send_tohyo_16)

    if message.content.startswith("投票2"):
            if client.user != message.author:
                if tohyo_setup_01 == True:
                    Choices[Choice02] += 1 
                    send_tohyo_17 = "選択肢2の" + Choice02 + "に1投票"
                    print(send_tohyo_17)    

    if message.content.startswith("投票3"):
            if client.user != message.author:
                if tohyo_setup_01 == True:
                    Choices[Choice03] += 1 
                    send_tohyo_18 = "選択肢3の" + Choice03 + "に1投票"
                    print(send_tohyo_18)   

    if time_setup_01 == True:
        time_setup_01 = False
        sleep(5)
        await client.send_message(message.channel, "5秒経過！")
        sleep(5)
        await client.send_message(message.channel, "残り5秒！！")
        sleep(5)
        Choices[Choice01] -= 1
        Choices[Choice02] -= 1
        Choices[Choice03] -= 1
        send_tohyo_19 = "--------------------------------------------------------"
        await client.send_message(message.channel, send_tohyo_19)
        send_tohyo_20 = "結果が出たよ！！！ \n\n★" + Choice01 + "の投票数:　" + str(Choices[Choice01]) + "★" + "\n" + "★" + Choice02 + "の投票数:　" + str(Choices[Choice02]) + "★" + "\n" + "★" + Choice03 + "の投票数:　" + str(Choices[Choice03]) + "★"
        await client.send_message(message.channel, send_tohyo_20)
        await client.send_message(message.channel, send_tohyo_19)
        max_Choices = max(Choices, key=Choices.get)
        send_tohyo_21 = "一番投票が多かったのは「" + max_Choices + "」だよ！！"
        await client.send_message(message.channel, send_tohyo_21)
        await client.send_message(message.channel, send_tohyo_19)
        sleep(1)
        await client.send_message(message.channel, "また遊んでね")
        await client.send_message(message.channel, "https://media.discordapp.net/attachments/546162748225093681/546562465610203137/makasenasai06.gif")
        Choices.clear()
        return


offline = "offline"
idle = "idle"
dnd = "dnd"

dict4 = []

def dict_count2(output2):
    output2 = len(dict4)
    return output2

@client.event
async def on_member_update(before, after):
    if before.status != after.status:
        after_update = str(after.status)
        if after_update == offline or  after_update == idle or after_update == dnd:
            #もしoffline等を日本語に訳したい時は、if関数を入れて文字列を代入すること
            if after_update == offline:
                after_update = "オフラインを隠す"
            if after_update == idle or after_update == dnd:
                after_update = "退席"
            dict4.append(after.display_name)
            last_count2 = str(dict4.count(after.display_name))
            update_01 = after.display_name + "が" + last_count2 + "回逃亡（" + after_update + "）しました"
            await client.send_message(server_channel, update_01)
            if int(last_count2) >= 3 and int(last_count2) <= 4:
                butigire2_send = "全てを逃亡で解決しようとした男"
                await client.send_message(server_channel, butigire2_send)
            elif int(last_count2) == 2:
                butigire2_send2 = "僅かでも都合が悪いと即逃亡"
                await client.send_message(server_channel, butigire2_send2)
            elif int(last_count2) >= 5 and int(last_count2) <= 6:
                butigire2_send3 = "いや多すぎだろが"
                await client.send_message(server_channel, butigire2_send3)
            elif int(last_count2) >= 7:
                butigire2_send4 = "？？？？ｗ、PCぶっ壊れてますよ"
                await client.send_message(server_channel, butigire2_send4)
            else:
                butigire2_send5 = "脱北が出てるぜ"
                await client.send_message(server_channel, butigire2_send5)


client.run('NTQ2MTYyODg5Njk5MDk4NjM3.D0k3xA.AsPFs53E3hfFVPqTkN3Ax79NyNU')
