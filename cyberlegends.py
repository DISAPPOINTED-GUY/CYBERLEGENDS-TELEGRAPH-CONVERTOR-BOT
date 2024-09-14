#    Copyright (c) 2021 Rishisuperyo
#    
#    This program is free software: you can redistribute it and/or modify  
#    it under the terms of the GNU General Public License as published by  
#    the Free Software Foundation, version 3.
# 
#    This program is distributed in the hope that it will be useful, but 
#    WITHOUT ANY WARRANTY; without even the implied warranty of 
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
#    General Public License for more details.
# 
#    License can be found in < https://github.com/RISHISUPERYO-GAMERZ/PROBOT-TELEGRAPH-MAKER/blob/main/License> 

import os
from telegraph import upload_file
import pyrogram
from pyrogram import filters, Client
from pyrogram.types import (
    InlineQueryResultArticle, InputTextMessageContent,
    InlineKeyboardMarkup, InlineKeyboardButton,
    CallbackQuery, InlineQuery)

APP_ID=os.getenv("API_ID")
API_HASH=os.getenv("API_HASH")
BOT_TOKEN=os.getenv("BOT_TOKEN")
Cyberlegends= Client(
   "Cyberlegends.Uploader",
   api_id=APP_ID,
   api_hash=API_HASH,
   bot_token=BOT_TOKEN,
)

@Cyberlegends.on_message(filters.photo)
async def uploadphoto(client, message):
  msg = await message.reply_text("`Wait plz Lemme download the photoðŸ˜Žâš¡`")
  userid = str(message.chat.id)
  img_path = (f"./DOWNLOADS/{userid}.jpg")
  img_path = await client.download_media(message=message, file_name=img_path)
  await msg.edit_text("`I HAVE DOWNLOADED THE PHOTOðŸ¥³ðŸ¥³, sending u âš¡`")
  try:
    tlink = upload_file(img_path)
  except:
    await msg.edit_text("`Something went wrong`") 
  else:
    await msg.edit_text(f"https://telegra.ph{tlink[0]}")     
    os.remove(img_path) 

@Cyberlegends.on_message(filters.animation)
async def uploadgif(client, message):
  if(message.animation.file_size < 5242880):
    msg = await message.reply_text("`WAIT AND EK MANTRA DE RAHA WOH BOL MUJHE:- ð“¢ð“ð“šð“ ð“›ð“ð“šð“ ð“‘ð“žð“žð“œ ð“‘ð“žð“žð“œ`")
    userid = str(message.chat.id)
    gif_path = (f"./DOWNLOADS/{userid}.mp4")
    gif_path = await client.download_media(message=message, file_name=gif_path)
    await msg.edit_text("`SendingðŸ˜Ž Plz wait ðŸ˜‚âš¡`")
    try:
      tlink = upload_file(gif_path)
      await msg.edit_text(f"https://telegra.ph{tlink[0]}")   
      os.remove(gif_path)   
    except Exception as e:
      await msg.edit_text("Error : {e}")
        
     logger.error(f"Failed: {e}")
@Cyberlegends.on_message(filters.video)
async def uploadvid(client, message):
  if(message.video.file_size < 5242880):
    msg = await message.reply_text("`rÍ›uÍ›kÍ›oÍ› zÍ›aÍ›rÍ›aÍ› sÍ›aÍ›bÍ›aÍ›rÍ› kÍ›aÍ›rÍ›oÍ›ðŸ˜‚ðŸ˜‚ðŸ˜‚`")
    userid = str(message.chat.id)
    vid_path = (f"./DOWNLOADS/{userid}.mp4")
    vid_path = await client.download_media(message=message, file_name=vid_path)
    await msg.edit_text("`Lo abh finnally bhej rahaðŸ˜‚`")
    try:
      tlink = upload_file(vid_path)
      await msg.edit_text(f"https://telegra.ph{tlink[0]}")     
      os.remove(vid_path)   
    except:
      await msg.edit_text("Kuch garbar hui hae reallyðŸ˜¶") 
  else:
    await message.reply_text("Size Should Be Less Than 5 mbðŸ˜¶ðŸ˜‘")

@Cyberlegends.on_message(filters.command(["start"]))
async def home(client, message):
  buttons = [[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
    ],
    [
              InlineKeyboardButton('Our Channel', url='https://t.me/Cyberlegends_NETWORK'),
        InlineKeyboardButton('âš¡DÌ¸EÌ¸VÍŽEÍŽLÍ¢OÍ¢PÌ¶EÌ¶RÌ¶âš¡â€Š', url='https://t.me/Cyberlegends_UPDATES')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await Cyberlegends.send_message(
chat_id=message.chat.id,
        text="""<b>Hello this is CYBERLEGENDS TELEGRAPH CONVERTER BOT thanks for using this bot our best RISHISUPERYO Ã— CYBERLEGENDS team made this bot
 ðŸ˜¶ðŸ˜‰,
        
im a telegraph Uploader That Can Upload Photo, Video And Gif
        
Simply send me photo, video or gif to upload to Telegra.ph
        
Made With âš¡ðŸ˜Ž By @CYBERLEGENDS_NETWORK âš¡</b>""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )

@Cyberlegends.on_message(filters.command(["help"]))
async def help(client, message):
  buttons = [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Close', callback_data='close')
    ],
    [
        InlineKeyboardButton('Our Channel', url='https://t.me/Cyberlegends_Network')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await Cyberlegends.send_message(
        chat_id=message.chat.id,
        text="""âš¡âš¡âš¡âš¡âš¡
        
Just AREE BHAI MUJHE PLZ YAAR 5MB KA NICHE ,GIF YA PHOTO YA VID SEND KARNA OKðŸ˜‚ðŸ˜Šâš¡
i'll upload it to telegra.ph and give you the direct link""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )                           
@Cyberlegends.on_callback_query()
async def button(Cyberlegends, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(Cyberlegends, update.message)
      elif "close" in cb_data:
       """
        await update.mess📊 STATS 📊

⚠️ EMPERORS ONLY ⚠️

🚀 Usage 🚀 - /stats

💻Info💻: This command shows statistics of the bot , It can be only used by 👑EMPERORS👑age.delete() 
"""
      elif "home" in cb_data:
        await update.message.delete()
        await home(Cyberlegends, update.message)
Cyberlegends.run()

