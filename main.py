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
Hi {}, Welcome to  MemeHub Telegram 🇱🇰 Official Bot.
 Bot By [◤ᴵᴬᴹǤΐรhaή ᴷʳⁱˢʰᵏᵃ◢ 『🇱🇰』](https://t.me/Imgishan)
"""
BACK_BUTTONS = InlineKeyboardMarkup([[
                 InlineKeyboardButton(text="👻 ʙᴀᴍᴄᴋ 👻",callback_data="bak")            
                 ]]
                  ) 

START_BUTTON = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('🍁 Owner 🍁', user_id="@N_Abeysinghe_2001")
                 ],
                 [
                 InlineKeyboardButton(text="🌴 ʜᴇʟᴘ 🌴",callback_data="hlp")
                 ],
                 [
                 InlineKeyboardButton("➕ sʜᴀʀᴇ ➕", switch_inline_query="share")
                 ]]
                  )
                  
FORCESUB_BUTTONS = InlineKeyboardMarkup([[
                 InlineKeyboardButton('Join Here - MemeHub Telegram 🇱🇰', url=f"https://t.me/+78jdOfCNSdFhMDM1")
                 ],
                 [
                 InlineKeyboardButton('🐞 ʀᴘᴏʀᴛ ʙᴜɢs 🐞', user_id=f"@Imgishan")
                 ],
                 [
                 InlineKeyboardButton(text="♻️ Reload ♻️",callback_data="ref")
                 ]]
                  )
    
HELP_STRING = "Meme Tiye nam dapam Mekata😒😂. Adminlata Msg Daanna One Nam ekat Mekata dapam 😒😂"

CLOSE_BUTTON = InlineKeyboardMarkup([[
                 InlineKeyboardButton("𝕮𝖑𝖔𝖒𝖘𝖊", callback_data="cloc")
                 ]]
                 )

FORCESUB_TEXT = "**❌ Access Denied ❌**\n\nMemehub eke nathuva Mokatada yako Botva Start Kare kkk😒😒\n♻️Join and Try Again.♻️"
                  
WELCOME_TEXT = "Hello.. <b>{}</b>\n<code>Type your query here..\nI'll respond to your query as earliest</code> 😉\n\nуσυ ωαииα тσ киσω αвσυт мє😌? яєα∂ вєℓσω\n\nαвσυт @Gishankrishka:-\n •му иαмє:- Gishan Krishka \n •му αgє:- υикиσωи🌝\n •¢σмρυтєя ℓαиgυαgє:- ωєв ∂єνєℓσρмєит(ℓєαяиιиg), ρутнσи мσяє ѕσσи😁\n•¢нє¢к [About ༒❣️☢️╣IrØή❂mคŇ╠☢️❣️༒](https://t.me/Gishankrishka_Info_bot) fσя мσяє\n\nPlz Don't Send Stickers 🥲\nReason :- [This](https://t.me/ultchat/19589)"
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
            ["🤴 OWNER 🤴"],
            ["💻 Bot Devs 💻", "👮‍♂️ MemeHub Admins 👮‍♂️"],
            ["NEXT 🔜"]
           
        ],
        resize_keyboard=True  # Make the keyboard smaller
    )

@Client.on_message(filters.private & filters.regex(pattern="🤴 OWNER 🤴"))   
async def startprivate(bot, message):
     await bot.send_sticker(message.chat.id, random.choice(OWNER_STICKER),reply_markup=InlineKeyboardMarkup([[              
                 InlineKeyboardButton('Nirmal Abeysinghe', user_id="N_Abeysinghe_2001")
                 ]]
                  )
     )
@Client.on_message(filters.private & filters.regex(pattern="💻 Bot Devs 💻"))   
async def startprivate(bot, message):
     await bot.send_sticker(message.chat.id, random.choice(DEV_STICKER),reply_markup=InlineKeyboardMarkup([[              
                 InlineKeyboardButton('༒❣️☢️╣IrØή❂mคŇ╠☢️❣️༒ ', user_id="ImGishan")
                 ],
                 [
                 InlineKeyboardButton('unknown boy┊𝙰𝙻𝙿𝙷𝙰 么 ™', user_id="UnknownB_o_y")
                 ]]
                  )
     )

@Client.on_message(filters.private & filters.regex(pattern="👮‍♂️ MemeHub Admins 👮‍♂️"))   
async def startprivate(bot, message):
     await bot.send_sticker(message.chat.id, random.choice(ADMIN_STICKER),reply_markup=InlineKeyboardMarkup([[
                 InlineKeyboardButton('Nirmal Abeysinghe', user_id="N_Abeysinghe_2001")
                 ],
                 [                 
                 InlineKeyboardButton('༒❣️☢️╣IrØή❂mคŇ╠☢️❣️༒ ', user_id="ImGishan")
                 ],
                 [                 
                 InlineKeyboardButton('unknown boy┊𝙰𝙻𝙿𝙷𝙰 么 ™', user_id="UnknownB_o_y")
                 ],
                 [                 
                 InlineKeyboardButton('Navidu Nimsara', user_id="Navidu_Nimsara")
                 ],
                 [                 
                 InlineKeyboardButton('DarkLucifer 么 ™', user_id="Dark_Iucifer")
                 ],
                 [                 
                 InlineKeyboardButton('🌀*✩.𝗛𝗜𝗥𝗨.✩*🌀', user_id="hiru_malsh_2002")
                 ],
                 [
                 InlineKeyboardButton('𝙃𝙊𝙍𝘼 𝙋𝙐𝙎𝘼 ᖇḁͦj̥ͦḁͦṗȧƙకꫝꪖ', user_id="hora_pusa")
                 ],
                 [                 
                 InlineKeyboardButton('║♔ Ꭲ ᕼ ᗩ ᖇ ᑌ ᑎ_ _ᗰ Ꮖ Ꭲ ᕼ ᔑ ᗩ ᖇ ᗩ ❥⃟♔║', user_id="XXXTENTACION_LOVER")
                 ],
                 [                 
                 InlineKeyboardButton('Sahiru Keshan', user_id="Sahiru_2007")
                 ],
                 [                 
                 InlineKeyboardButton('𝙈𝙧.𝙎𝙖𝙩𝙝𝙖𝙣', user_id="Sathan_OP")
                 ],
                 [
                 InlineKeyboardButton('⚜️ K.Malith Punsara ⚜️', user_id="kmp32913291")
                 ],
                 [                 
                 InlineKeyboardButton(' ගින්නෙ ඉන්න චීස් කෑල්ල', user_id="Chamath198")
                 ],
                 [                 
                 InlineKeyboardButton('ŦħȺɍᵾꝁ ɌɇnᵾɉȺ', user_id="ImTharuk")
                 ],
                 [                 
                 InlineKeyboardButton('𝐖ᏋᏒᏋ🆆🅾️🅻🅵', user_id="w_wolflk2")
                 ],
                 [
                 InlineKeyboardButton('𝙏𝙝𝙚𝙣𝙪𝙡𝙖⁹⁹⁹ ', user_id="Th4nula999")
                 ],
                 [                 
                 InlineKeyboardButton('☠️𝘋𝘳.𝘚𝘵𝘳𝘰𝘮𝘦☠️', user_id="Dr_Strome")
                 ],
                 [                 
                 InlineKeyboardButton('Pasindu Maleesha', user_id="PASINDU_M_WICK")
                 ],
                 [                 
                 InlineKeyboardButton('ixAAr Modderϟ➊ ', user_id="Mr_ixAAr")
                 ],
                 [
                 InlineKeyboardButton('𝙕𝙚𝙩𝙖', user_id="sthisara")
                 ],
                 [
                 InlineKeyboardButton('Inush Deeptha', user_id="SL10Inush")
                 ],
                 [                 
                 InlineKeyboardButton('🅳🅰️🆁🅺 丂卂爪ㄩ尺卂|', user_id="IamDarkSam2")
                 ],
                 [                 
                 InlineKeyboardButton('ᴄʜᴀᴍᴏᴅ ɪᴍᴀɴᴛʜᴀ ֍🇱🇰', user_id="G_c_c_123")
                 ],
                 [                 
                 InlineKeyboardButton('🇲 🇷✪ ™✓DaRkᗰᗴᎩᕼᗴᗰ', user_id="Brotherz90")
                 ],
                 [
                 InlineKeyboardButton('#𝙇𝙚𝙥𝙩_𝙏𝙂 Kaveesha Nethmal', user_id="jason_spqr_roman_Kr")
                 ],
                 [                 
                 InlineKeyboardButton('අකිල', user_id="akiyush")
                 ],
                 [                 
                 InlineKeyboardButton('☬෴𝐃𝐀𝐑𝐊 ✠ 𝐋𝐎𝐑𝐃෴☬', url="tg://user?id=1390045267")
                 ],
                 [                 
                 InlineKeyboardButton(' 𝗩𝗶𝗻𝗶𝘁𝗵 𝗕𝗮𝘄𝗮𝗻𝘁𝗵𝗮', url="tg://user?id=1100376280")
                 ],
                 [
                 InlineKeyboardButton('💫𝗢𝘁𝗿𝗶𝘅𝘅💫', user_id="animepissa")
                 ],
                 [                 
                 InlineKeyboardButton('🔥🌏♠️𝐌𝐫 𝙊𝙍𝙂𝘼♠️🌏🔥', user_id="ORGA0302")
                 ],
                 [                 
                 InlineKeyboardButton('Mr.ᴅᴇᴠɪʟʟ😈', user_id="lucifer_the_devill")
                 ],
                 [                 
                 InlineKeyboardButton('« Alok Weerasinghe »', user_id="Alokweerasinghe")
                 ],
                 [
                 InlineKeyboardButton('Sathish Kalhara', user_id="Sathish_Kalhara")
                 ],
                 [                 
                 InlineKeyboardButton('ᴱᴹᴾ ƇƠƲƝƬ ƊƦƛƇƲԼƛ', user_id="LordVladtheImpalerTransylvania")
                 ]]
                  )
     )
    
@Client.on_message(filters.private & filters.regex(pattern="NEXT 🔜"))   
async def startprivate(bot, message):
     await bot.send_message(message.chat.id, text='NEXT 🔜',reply_markup=ReplyKeyboardMarkup(
      [
            ["Thama Mukut na"],
            ["BACK 🔙"]
           
        ],
        resize_keyboard=True  # Make the keyboard smaller
      )
    )

@Client.on_message(filters.private & filters.regex(pattern="BACK 🔙"))   
async def startprivate(bot, message):
     await bot.send_message(message.chat.id, text='BACK 🔙',reply_markup=REPLY_BUTTONS)
     
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
    text = f"Hi {message.from_user.mention}, Welcome to  MemeHub Telegram 🇱🇰 Official Bot\n\n★彡 ʙᴏᴛ ʙʏ 彡★\n[◤ᴵᴬᴹǤΐรhaή ᴷʳⁱˢʰᵏᵃ◢ 『🇱🇰』](https://t.me/Imgishan)\n[unknown boy┊𝙰𝙻𝙿𝙷𝙰 么 ™](t.me/UnknownB_o_y)"
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
    text = "Ur Photo Sent To [MemeHub Telegram 🇱🇰](https://t.me/memehubTGSL)"
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
             text="♻️Adding Soon.....",
        )
    elif update.data == "bak":
         await update.message.edit_text(
             text=HELP_STRING,
             reply_markup=CLOSE_BUTTON,
             disable_web_page_preview=True
         )
         await update.answer(
             text="👻 ʙᴀᴍᴄᴋ 👻",
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
             text="👻 ʜᴇᴍʟᴘ 👻",
         )
    elif update.data == "cloc":
         await update.message.delete()
    elif update.data == "ref": 
        await update.answer(
             text="♻️Reloading.....♻️",
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
            message_id=message.message.id
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
𝙷𝚒. 𝙱𝚘𝚢𝚜 𝚊𝚗𝚍 𝚐𝚒𝚛𝚕𝚜 𝚠𝚎 𝚊𝚛𝚎 𝚝𝚑𝚎 𝚖𝚎𝚖𝚎𝚑𝚞𝚋 𝚒𝚏 𝚢𝚘𝚞 𝚑𝚊𝚟𝚎 𝚖𝚎𝚖𝚎𝚜 𝚜𝚎𝚗𝚍 𝚢𝚘𝚞𝚛 𝚖𝚎𝚖𝚎𝚜 𝚝𝚘 𝚘𝚞𝚛 𝚋𝚘𝚝 𝚊𝚗𝚍 𝚑𝚎𝚕𝚙 𝚞𝚜.
𝙼𝚎𝚖𝚎𝚑𝚞𝚋 එකේ ඇඩ්මින් නැ කියල දුකෙම්ද ඉන්නේ 𝚖𝚎𝚖𝚎𝚜 ගොඩගැහිලා ඒවාට කරගන්න දෙයක් නේද? මෙන්න විසදුම ඔයාගේ 𝚖𝚎𝚖𝚎𝚜/𝚏𝚞𝚗𝚗𝚢 𝚟𝚒𝚍𝚎𝚘𝚜 ඔක්කොම එවන්න අපිට අපි ඒවා දානවා අපේ 𝚌𝚑𝚊𝚗𝚗𝚎𝚕 එකේ ඒ අතරින් හැමදාම 𝚖𝚎𝚖𝚜 දාන අයට අපේ 𝚌𝚑𝚊𝚗𝚗𝚎𝚕 එකේ ඇඩ්මින් වෙන්නත් පුළුවන් අදම එක්වන්න අප සමග 🤞✌️🤟🤘👊
𝙱𝚘𝚝 = @MemehubTgSl_Bot
""",
                    reply_markup=InlineKeyboardMarkup([[              
                 InlineKeyboardButton('🍁 Owner 🍁', user_id="@N_Abeysinghe_2001")
                 ],
                 [
                 InlineKeyboardButton('🐞 Report Bugs 🐞', user_id="1884885842")
                 ],
                 [
                 InlineKeyboardButton('ᴍᴇᴍᴇʜᴜʙ ᴏᴍғғɪᴄɪᴀʟ ʙᴏᴍᴛ 『🇱🇰』', user_id="@MemeHubTgSl_Bot")
                 ],
                 [
                 InlineKeyboardButton("➕ sʜᴀʀᴇ ➕", switch_inline_query="share")
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










