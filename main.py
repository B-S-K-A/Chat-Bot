import os
from os import error
import logging
import pyrogram
import time
from decouple import config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

KINGAMDA = Client(
    "king-amda",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_IMG = "https://telegra.ph/file/3ea20a755f67a981eda42.jpg"

START_TEXT = """
𝐊𝐢𝐧𝐠 𝐀𝐦𝐝𝐚 ගෙ 𝐏𝐌 𝐒𝐞𝐜𝐮𝐫𝐢𝐭𝐲 එකෙන් ඔයාට 𝐊𝐢𝐧𝐠 𝐀𝐦𝐝𝐚 ට 𝐌𝐬𝐠 දාන්න දෙන්නෙ නෑ ..

ඒකට විකල්පයක් විදියට තමයි 𝐊𝐢𝐧𝐠 𝐀𝐦𝐝𝐚 𝐁𝐨𝐭 ව හැදුවෙ..

ඔයාලට මේකෙන් 𝐊𝐢𝐧𝐠 𝐀𝐦𝐝𝐚 ව සම්බන්ධ කරගන්න පුලුවන්.

ගොඩ දෙනෙක් අහන ප්‍රශ්න යට බටන් වල තියෙනවා..
ඔයාට ඕන ඒවා තියෙනම් එතනින් ගන්න පුලුවන්.. 
යටම තීන 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐊𝐢𝐧𝐠 𝐀𝐦𝐝𝐚 බටන් එකෙන් ඔයාට 𝐊𝐢𝐧𝐠 𝐀𝐦𝐝𝐚 ව සම්බන්ධ කර ගන්න පුලුවන්.
"""

START_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('King Amda Telegram', callback_data='cbcmdsm'),
        InlineKeyboardButton('King Amda Whatsap',callback_data='infoan_me')
        ],
        [
        InlineKeyboardButton('Our Main Bot(Anki Cozmo)',callback_data='infoan_me'),
        InlineKeyboardButton('GitHub',url='https://github.com/King-Amda')
        ],
        [InlineKeyboardButton('Apply For Anki Cozmo Devs', url='https://forms.gle/zvspqb7Nn2MvWmbu8')
        ]]
)

@KINGAMDA.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_photo(START_IMG)
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        reply_markup=START_BUTTON,
        disable_web_page_preview=True,
        quote=True
        
KINGAMDA.run()        
