import os
import random
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid
from pyrogram.errors import UserNotParticipant
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto, InputTextMessageContent
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid, UserNotParticipant, UserBannedInChannel
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultPhoto, ReplyKeyboardMarkup)
from db.db import udB
import pymongo

acc = client["ACC"]
db = client["bot"]
userdb = db["user"]

#Client
Client = Client(
    "Memehub Bot",
    bot_token= "5011377446:AAHavxAS4fO42B41mNVcKVoQL8z6D6_LUdU",
    api_id= 8838171,
    api_hash= "0587408d4f7d9301f5295840b0f3b494",
)


force_subchannel = "Memehubtgsl"

START_STRING ="""
Hi {}, Welcome to  MemeHub Telegram ð±ð° Official Bot.
 Bot By [â¤á´µá´¬á´¹Ç¤Îà¸£haÎ® á´·Ê³â±Ë¢Ê°áµáµâ¢ ãð±ð°ã](https://t.me/Imgishan)
"""
BACK_BUTTONS = InlineKeyboardMarkup([[
                 InlineKeyboardButton(text="ð» Êá´á´á´á´ ð»",callback_data="bak")            
                 ]]
                  ) 

START_BUTTON = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('ð Owner ð', user_id="@N_Abeysinghe_2001")
                 ],
                 [
                 InlineKeyboardButton(text="ð´ Êá´Êá´ ð´",callback_data="hlp")
                 ],
                 [
                 InlineKeyboardButton("â sÊá´Êá´ â", switch_inline_query="share")
                 ]]
                  )
                  
FORCESUB_BUTTONS = InlineKeyboardMarkup([[
                 InlineKeyboardButton('Join Here - MemeHub Telegram ð±ð°', url=f"https://t.me/+78jdOfCNSdFhMDM1")
                 ],
                 [
                 InlineKeyboardButton('ð Êá´á´Êá´ Êá´É¢s ð', user_id=f"@Imgishan")
                 ],
                 [
                 InlineKeyboardButton(text="â»ï¸ Reload â»ï¸",callback_data="ref")
                 ]]
                  )
    
HELP_STRING = "Meme Tiye nam dapam Mekataðð. Adminlata Msg Daanna One Nam ekat Mekata dapam ðð"

CLOSE_BUTTON = InlineKeyboardMarkup([[
                 InlineKeyboardButton("ð®ððððð", callback_data="cloc")
                 ]]
                 )

FORCESUB_TEXT = "**â Access Denied â**\n\nMemehub eke nathuva Mokatada yako Botva Start Kare kkkðð\nâ»ï¸Join and Try Again.â»ï¸"
                  
WELCOME_TEXT = "Hello.. <b>{}</b>\n<code>Type your query here..\nI'll respond to your query as earliest</code> ð\n\nÑÏÏ ÏÎ±Ð¸Ð¸Î± ÑÏ ÐºÐ¸ÏÏ Î±Ð²ÏÏÑ Ð¼Ñð? ÑÑÎ±â Ð²ÑâÏÏ\n\nÎ±Ð²ÏÏÑ @Gishankrishka:-\n â¢Ð¼Ñ Ð¸Î±Ð¼Ñ:- Gishan Krishka \n â¢Ð¼Ñ Î±gÑ:- ÏÐ¸ÐºÐ¸ÏÏÐ¸ð\n â¢Â¢ÏÐ¼ÏÏÑÑÑ âÎ±Ð¸gÏÎ±gÑ:- ÏÑÐ² âÑÎ½ÑâÏÏÐ¼ÑÐ¸Ñ(âÑÎ±ÑÐ¸Î¹Ð¸g), ÏÑÑÐ½ÏÐ¸ Ð¼ÏÑÑ ÑÏÏÐ¸ð\nâ¢Â¢Ð½ÑÂ¢Ðº [About à¼â£ï¸â¢ï¸â£IrÃÎ®âmà¸Åâ â¢ï¸â£ï¸à¼](https://t.me/Gishankrishka_Info_bot) fÏÑ Ð¼ÏÑÑ\n\nPlz Don't Send Stickers ð¥²\nReason :- [This](https://t.me/ultchat/19589)"
USER_DETAILS = "<b>FROM:</b>\nName: {} {}\nId: {}\nUname: @{}\nScam: {}\nRestricted: {}\nStatus: {}\nDc Id: {}"
PM_TXT_ATT = "<b>Message from:</b> {}\n<b>Name:</b> {}\n\n{}"
PM_MED_ATT = "<b>Photo from:</b> {} \n<b>Name:</b> {}"

OWNER_STICKER = ["CAADAgADtA8AAhUWiEuTU2os6PSW-AI",
                "CAADAgADCwMAAm2wQgN_tBzazKZEJQI",
                "CAADAgADtwEAAladvQr3FVtdLiA1jgI", 
                "CAADBQADSwQAAnxrOFaYSIaXhBE_YAI"              
         ]
ADMIN_STICKER = ["CAADAgADzhMAAhDzcElTIbO4ZQ8stAI",
                "CAADBQADxwQAAgcbUFea8nhgWIiuGwI",
                "CAADBQADPAUAAtzIoFWtMe3LazkiKQI", 
                "CAADBQADDgQAAkKxWVZAvhW5fKSifwI"              
         ] 
DEV_STICKER = ["CAADAgADaRsAAsOUWUpHrmf5mZp3EgI",
                "CAADAgADbAIAAladvQoqGV6cxNDenwI",
                "CAADAgADgQEAAiteUwteCmw-bAABeLQC", 
                "CAADBQADZgMAAvIEcFVMnMXcAqRX7gI",
                "CAADAgADFwADlp-MDlZMBDUhRlElAg"                
         ]  


REPLY_BUTTONS=ReplyKeyboardMarkup(
      [
            ["ð¤´ OWNER ð¤´"],
            ["ð» Bot Devs ð»", "ð®ââï¸ MemeHub Admins ð®ââï¸"],
            ["NEXT ð"]
           
        ],
        resize_keyboard=True  # Make the keyboard smaller
    )

@Client.on_message(filters.private & filters.regex(pattern="ð¤´ OWNER ð¤´"))   
async def startprivate(bot, message):
     await bot.send_sticker(message.chat.id, random.choice(OWNER_STICKER),reply_markup=InlineKeyboardMarkup([[              
                 InlineKeyboardButton('Nirmal Abeysinghe', user_id="N_Abeysinghe_2001")
                 ]]
                  )
     )
@Client.on_message(filters.private & filters.regex(pattern="ð» Bot Devs ð»"))   
async def startprivate(bot, message):
     await bot.send_sticker(message.chat.id, random.choice(DEV_STICKER),reply_markup=InlineKeyboardMarkup([[              
                 InlineKeyboardButton('à¼â£ï¸â¢ï¸â£IrÃÎ®âmà¸Åâ â¢ï¸â£ï¸à¼ ', user_id="ImGishan")
                 ],
                 [
                 InlineKeyboardButton('unknown boyâð°ð»ð¿ð·ð° ä¹ â¢', user_id="UnknownB_o_y")
                 ]]
                  )
     )

@Client.on_message(filters.private & filters.regex(pattern="ð®ââï¸ MemeHub Admins ð®ââï¸"))   
async def startprivate(bot, message):
     await bot.send_sticker(message.chat.id, random.choice(ADMIN_STICKER),reply_markup=InlineKeyboardMarkup([[
                 InlineKeyboardButton('Nirmal Abeysinghe', user_id="N_Abeysinghe_2001")
                 ],
                 [                 
                 InlineKeyboardButton('à¼â£ï¸â¢ï¸â£IrÃÎ®âmà¸Åâ â¢ï¸â£ï¸à¼ ', user_id="ImGishan")
                 ],
                 [                 
                 InlineKeyboardButton('unknown boyâð°ð»ð¿ð·ð° ä¹ â¢', user_id="UnknownB_o_y")
                 ],
                 [                 
                 InlineKeyboardButton('Navidu Nimsara', user_id="Navidu_Nimsara")
                 ],
                 [                 
                 InlineKeyboardButton('DarkLucifer ä¹ â¢', user_id="Dark_Iucifer")
                 ],
                 [                 
                 InlineKeyboardButton('ð*â©.ððð¥ð¨.â©*ð', user_id="hiru_malsh_2002")
                 ],
                 [
                 InlineKeyboardButton('ðððð¼ ðððð¼ áaÍ¦Ì¥jÍ¦Ì¥aÍ¦Ì¥pÌaÌÆà°ê«êª', user_id="hora_pusa")
                 ],
                 [                 
                 InlineKeyboardButton('ââ á¢ á¼ á© á á á_ _á° á á¢ á¼ á á© á á© â¥âââ', user_id="XXXTENTACION_LOVER")
                 ],
                 [                 
                 InlineKeyboardButton('Sahiru Keshan', user_id="Sahiru_2007")
                 ],
                 [                 
                 InlineKeyboardButton('ðð§.ððð©ððð£', user_id="Sathan_OP")
                 ],
                 [
                 InlineKeyboardButton('âï¸ K.Malith Punsara âï¸', user_id="kmp32913291")
                 ],
                 [                 
                 InlineKeyboardButton(' à¶à·à¶±à·à¶±à· à¶à¶±à·à¶± à¶ à·à·à· à¶à·à¶½à·à¶½', user_id="Chamath198")
                 ],
                 [                 
                 InlineKeyboardButton('Å¦Ä§ÈºÉáµ¾ê ÉÉnáµ¾ÉÈº', user_id="ImTharuk")
                 ],
                 [                 
                 InlineKeyboardButton('ðáááðð¾ï¸ð»ðµ', user_id="w_wolflk2")
                 ],
                 [
                 InlineKeyboardButton('ðððð£ðªð¡ðâ¹â¹â¹ ', user_id="Th4nula999")
                 ],
                 [                 
                 InlineKeyboardButton('â ï¸ðð³.ððµð³ð°ð®ð¦â ï¸', user_id="Dr_Strome")
                 ],
                 [                 
                 InlineKeyboardButton('Pasindu Maleesha', user_id="PASINDU_M_WICK")
                 ],
                 [                 
                 InlineKeyboardButton('ixAAr ModderÏâ ', user_id="Mr_ixAAr")
                 ],
                 [
                 InlineKeyboardButton('ððð©ð', user_id="sthisara")
                 ],
                 [
                 InlineKeyboardButton('Inush Deeptha', user_id="SL10Inush")
                 ],
                 [                 
                 InlineKeyboardButton('ð³ð°ï¸ððº ä¸åçªã©å°ºå|', user_id="IamDarkSam2")
                 ],
                 [                 
                 InlineKeyboardButton('á´Êá´á´á´á´ Éªá´á´É´á´Êá´ Öð±ð°', user_id="G_c_c_123")
                 ],
                 [                 
                 InlineKeyboardButton('ð² ð·âª â¢âDaRká°á´á©á¼á´á°', user_id="Brotherz90")
                 ],
                 [
                 InlineKeyboardButton('#ððð¥ð©_ðð Kaveesha Nethmal', user_id="jason_spqr_roman_Kr")
                 ],
                 [                 
                 InlineKeyboardButton('à¶à¶à·à¶½', user_id="akiyush")
                 ],
                 [                 
                 InlineKeyboardButton('â¬à·´ðððð â  ððððà·´â¬', url="tg://user?id=1390045267")
                 ],
                 [                 
                 InlineKeyboardButton(' ð©ð¶ð»ð¶ððµ ðð®ðð®ð»ððµð®', url="tg://user?id=1100376280")
                 ],
                 [
                 InlineKeyboardButton('ð«ð¢ðð¿ð¶ððð«', user_id="animepissa")
                 ],
                 [                 
                 InlineKeyboardButton('ð¥ðâ ï¸ðð« ðððð¼â ï¸ðð¥', user_id="ORGA0302")
                 ],
                 [                 
                 InlineKeyboardButton('Mr.á´á´á´ ÉªÊÊð', user_id="lucifer_the_devill")
                 ],
                 [                 
                 InlineKeyboardButton('Â« Alok Weerasinghe Â»', user_id="Alokweerasinghe")
                 ],
                 [
                 InlineKeyboardButton('Sathish Kalhara', user_id="Sathish_Kalhara")
                 ],
                 [                 
                 InlineKeyboardButton('á´±á´¹á´¾ ÆÆ Æ²ÆÆ¬ ÆÆ¦ÆÆÆ²Ô¼Æ', user_id="LordVladtheImpalerTransylvania")
                 ]]
                  )
     )
    
@Client.on_message(filters.private & filters.regex(pattern="NEXT ð"))   
async def startprivate(bot, message):
     await bot.send_message(message.chat.id, text='NEXT ð',reply_markup=ReplyKeyboardMarkup(
      [
            ["Thama Mukut na"],
            ["BACK ð"]
           
        ],
        resize_keyboard=True  # Make the keyboard smaller
      )
    )

@Client.on_message(filters.private & filters.regex(pattern="BACK ð"))   
async def startprivate(bot, message):
     await bot.send_message(message.chat.id, text='BACK ð',reply_markup=REPLY_BUTTONS)
     
@Client.on_message(filters.command(["start", "start@MemeHubTgSl_Bot"]))
async def startprivate(bot, message):
    USER = InlineKeyboardMarkup([[              
                 InlineKeyboardButton(f'{message.from_user.first_name}', url=f"t.me/{message.from_user.username}")
                 ]]
                  )
    info = await bot.get_users(user_ids=message.from_user.id)
    USER_DETAILS = f"[{message.from_user.mention}](tg://user?id={message.from_user.id}) [`{message.from_user.id}`] Started Ur Bot.\n\n**First Name: `{info.first_name}`**\n**LastName: `{info.last_name}`**\n**Scam: `{info.is_scam}`**\n**Restricted: `{info.is_restricted}`**\n**Status:`{info.status}`**\n**Dc Id: `{info.dc_id}`**"
    await bot.send_message(-1001759991131, text=USER_DETAILS, reply_markup=USER)
    if force_subchannel:
        try:
            user = await bot.get_chat_member(force_subchannel, message.from_user.id)
            if user.status == "kicked out":
                await message.reply_text("Yourt Banned")
                return 
        except UserNotParticipant:
            file_id = "CAADBQADOAcAAn_zKVSDCLfrLpxnhAI"
            await bot.send_sticker(message.chat.id, file_id)
            text = FORCESUB_TEXT
            reply_markup = FORCESUB_BUTTONS
            await message.reply_text(
            text=text,
            reply_markup=reply_markup
            ) 
            return
    file_id = "CAADBQADVwYAAhCWAVRcksqpPVEWHAI"
    await bot.send_sticker(message.chat.id, file_id, reply_markup=REPLY_BUTTONS)
    text = f"Hi {message.from_user.mention}, Welcome to  MemeHub Telegram ð±ð° Official Bot\n\nâå½¡ Êá´á´ ÊÊ å½¡â\n[â¤á´µá´¬á´¹Ç¤Îà¸£haÎ® á´·Ê³â±Ë¢Ê°áµáµâ¢ ãð±ð°ã](https://t.me/Imgishan)\n[unknown boyâð°ð»ð¿ð·ð° ä¹ â¢](t.me/UnknownB_o_y)"
    reply_markup = START_BUTTON  
    await message.reply_text(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
    )
    


@Client.on_message(filters.command(["help", "help@MemeHubTgSl_Bot"]))
async def startprivate(bot, message):
    if force_subchannel:
        try:
            user = await bot.get_chat_member(force_subchannel, message.from_user.id)
            if user.status == "kicked out":
                await message.reply_text("Yourt Banned")
                return 
        except UserNotParticipant:
            file_id = "CAADBQADOAcAAn_zKVSDCLfrLpxnhAI"
            await bot.send_sticker(message.chat.id, file_id)
            text = FORCESUB_TEXT
            reply_markup = FORCESUB_BUTTONS
            await message.reply_text(
            text=text,
            reply_markup=reply_markup
            ) 
            return
    await message.reply_text(
        text=HELP_STRING,
        reply_markup=CLOSE_BUTTON,
        disable_web_page_preview=True
         )

@Client.on_message(filters.private & filters.text)
async def pm_text(bot, message):
    if force_subchannel:
        try:
            user = await bot.get_chat_member(force_subchannel, message.from_user.id)
            if user.status == "kicked out":
                await message.reply_text("Yourt Banned")
                return 
        except UserNotParticipant:
            file_id = "CAADBQADOAcAAn_zKVSDCLfrLpxnhAI"
            await bot.send_sticker(message.chat.id, file_id)
            text = FORCESUB_TEXT
            reply_markup = FORCESUB_BUTTONS
            await message.reply_text(
            text=text,
            reply_markup=reply_markup
            ) 
            return
    if message.from_user.id == 1884885842:
        await reply_text(bot, message)
        return
    info = await bot.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    await bot.send_message(
        chat_id=1884885842,
        text=f"**Msg from:</b> {reference_id} **\n**Name:</b> {info.first_name}\n\n{message.text}**"
    )
    await bot.send_message(
        chat_id=-1001759991131,
        text=f"**Msg from:</b> {reference_id} **\n**Name:</b> {message.from_user.mention}\n\n{message.text}**"
    )


@Client.on_message(filters.sticker & filters.private) 
async def pm_media(bot, message):
    if force_subchannel:
        try:
            user = await bot.get_chat_member(force_subchannel, message.from_user.id)
            if user.status == "kicked out":
                await message.reply_text("Yourt Banned")
                return 
        except UserNotParticipant:
            file_id = "CAADBQADOAcAAn_zKVSDCLfrLpxnhAI"
            await bot.send_sticker(message.chat.id, file_id)
            text = FORCESUB_TEXT
            reply_markup = FORCESUB_BUTTONS
            await message.reply_text(
            text=text,
            reply_markup=reply_markup
            ) 
            return
    file_id = "CAADBQADEwUAAmjn4Vez7jrL1Cu2AAEC"
    await bot.send_sticker(message.chat.id, file_id) 

@Client.on_message(filters.media & filters.private)
async def pm_media(bot, message):
    if force_subchannel:
        try:
            user = await bot.get_chat_member(force_subchannel, message.from_user.id)
            if user.status == "kicked out":
                await message.reply_text("Yourt Banned")
                return 
        except UserNotParticipant:
            file_id = "CAADBQADOAcAAn_zKVSDCLfrLpxnhAI"
            await bot.send_sticker(message.chat.id, file_id)
            text = FORCESUB_TEXT
            reply_markup = FORCESUB_BUTTONS
            await message.reply_text(
            text=text,
            reply_markup=reply_markup
            ) 
            return
    if message.from_user.id == 1884885842:
        await replay_media(bot, message)
        return
    info = await bot.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    await message.forward(1884885842)
    
    await bot.send_message(1884885842 ,f"Photo from:</b> {reference_id} **\n**Name:</b> {info.first_name}")
    await message.forward(-1001210985373)
    await message.forward(-1001759991131)
    await bot.send_message(
        chat_id=-1001759991131,
        text=f"**Msg from:</b> {reference_id} **\n**Name:</b> [{message.from_user.first_name}](tg://user?id={message.from_user.id})**\n\n@admin"
    )
    reply_markup = BACK_BUTTONS
    text = "Ur Photo Sent To [MemeHub Telegram ð±ð°](https://t.me/memehubTGSL)"
    await message.reply_text(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
    )
    




@Client.on_message(filters.text)
async def reply_text(bot, message):
    reference_id = True
    if message.reply_to_message is not None:
        file = message.reply_to_message
        try:
            reference_id = file.text.split()[2]
        except Exception:
            pass
        try:
            reference_id = file.caption.split()[2]
        except Exception:
            pass
        await bot.send_message(
            text=message.text,
            chat_id=int(reference_id)
        )    
 



@Client.on_callback_query()  
async def tgm(bot, update):  
    if update.data == "add": 
        await update.answer(
             text="â»ï¸Adding Soon.....",
        )
    elif update.data == "bak":
         await update.message.edit_text(
             text=HELP_STRING,
             reply_markup=CLOSE_BUTTON,
             disable_web_page_preview=True
         )
         await update.answer(
             text="ð» Êá´á´á´á´ ð»",
         )
    elif update.data == "bak":
         await update.message.delete()
         await bot.delete_message(update.chat.id, update.message.id)
    elif update.data == "hlp":
         await update.message.edit_text(
             text=HELP_STRING,
             reply_markup=CLOSE_BUTTON,
             disable_web_page_preview=True
         )
         await update.answer(
             text="ð» Êá´á´Êá´ ð»",
         )
    elif update.data == "cloc":
         await update.message.delete()
    elif update.data == "ref": 
        await update.answer(
             text="â»ï¸Reloading.....â»ï¸",
        )        
         
@Client.on_message(filters.user(1884885842) & filters.sticker)
async def replay_media(bot, message):
    reference_id = True
    if message.reply_to_message is not None:
        file = message.reply_to_message
        try:
            reference_id = file.text.split()[2]
        except Exception:
            pass
        try:
            reference_id = file.caption.split()[2]
        except Exception:
            pass
        await bot.copy_message(
            chat_id=int(reference_id),
            from_chat_id=message.chat.id,
            message_id=message.message_id
        )          
         
@Client.on_inline_query()
async def answer(client, inline_query):
    if inline_query.query=='share':
        await inline_query.answer(
            results=[
                InlineQueryResultPhoto(
                    title="Share Karapam",
                    photo_url="https://telegra.ph/file/7966021e7aa2a08112249.jpg",
                    caption="""
ð·ð. ð±ðð¢ð ððð ððððð ð ð ððð ððð ððððððð ðð ð¢ðð ðððð ððððð ðððð ð¢ððð ððððð ðð ððð ððð ððð ðððð ðð.
ð¼ðððððð à¶à¶à· à¶à¶©à·à¶¸à·à¶±à· à¶±à· à¶à·à¶ºà¶½ à¶¯à·à¶à·à¶¸à·à¶¯ à¶à¶±à·à¶±à· ððððð à¶à·à¶©à¶à·à·à·à¶½à· à¶à·à·à¶§ à¶à¶»à¶à¶±à·à¶± à¶¯à·à¶ºà¶à· à¶±à·à¶¯? à¶¸à·à¶±à·à¶± à·à·à·à¶¯à·à¶¸ à¶à¶ºà·à¶à· ððððð/ððððð¢ ðððððð à¶à¶à·à¶à·à¶¸ à¶à·à¶±à·à¶± à¶à¶´à·à¶§ à¶à¶´à· à¶à·à· à¶¯à·à¶±à·à· à¶à¶´à· ððððððð à¶à¶à· à¶ à¶à¶­à¶»à·à¶±à· à·à·à¶¸à¶¯à·à¶¸ ðððð à¶¯à·à¶± à¶à¶ºà¶§ à¶à¶´à· ððððððð à¶à¶à· à¶à¶©à·à¶¸à·à¶±à· à·à·à¶±à·à¶±à¶­à· à¶´à·à·à·à·à¶±à· à¶à¶¯à¶¸ à¶à¶à·à·à¶±à·à¶± à¶à¶´ à·à¶¸à¶ ð¤âï¸ð¤ð¤ð
ð±ðð = @MemehubTgSl_Bot
""",
                    reply_markup=InlineKeyboardMarkup([[              
                 InlineKeyboardButton('ð Owner ð', user_id="@N_Abeysinghe_2001")
                 ],
                 [
                 InlineKeyboardButton('ð Report Bugs ð', user_id="1884885842")
                 ],
                 [
                 InlineKeyboardButton('á´á´á´á´Êá´Ê á´á´ÒÒÉªá´Éªá´Ê Êá´á´á´ ãð±ð°ã', user_id="@MemeHubTgSl_Bot")
                 ],
                 [
                 InlineKeyboardButton("â sÊá´Êá´ â", switch_inline_query="share")
                 ]])
                    
                        
                     
            ),
            ],
            cache_time=1
        )        

@app.on_message(filters.private & filters.command("bcast") & filters.user(1884885842) & filters.reply)
async def broadcast_message(_, message):
    sleep_time = 0.1
    text = message.reply_to_message.text.markdown
    sent = 0
    chats = userdb.find({})
    m = await message.reply_text(
        f"Broadcast in progress"
    )
    for chat in chats:
        try:
            await app.send_message(chat['username'], text=text,disable_web_page_preview=True)
            await asyncio.sleep(sleep_time)
            sent += 1
        except FloodWait as e:
            await asyncio.sleep(int(e.x))
        except Exception:
            pass
    await m.edit(f"**Broadcasted Message In {sent} Chats.**")        

print(f"""
Im Alive
""")
Client.run()










