import random
from hydrogram.types import InlineKeyboardButton
# ButtonStyle import karne ki zaroorat nahi hai
import config
from Oneforall import app

# Premium Stickers IDs
STICKERS = [6312260233171312151, 5433824103134530018, 5431445213233261748]

def btn(text, style=None, **kwargs):
    premium_id = random.choice(STICKERS)
    return InlineKeyboardButton(
        text=text,
        icon_custom_emoji_id=premium_id,
        style=style, # Yahan direct number (1-4) jayega
        **kwargs
    )

def start_panel(_):
    return [[
        btn(_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true", style=2), # 2 = Green
        btn(_["S_B_2"], url=config.SUPPORT_CHAT, style=1), # 1 = Blue
    ]]

def private_panel(_):
    return [
        [btn(_["S_B_3"], url=f"https://t.me/{app.username}?startgroup=true", style=2)],
        [
            btn("ᴇʀᴇɴ ʏᴇᴀɢᴇʀ", url="https://t.me/toxication_infinity", style=1),
            btn(_["S_B_2"], url=config.SUPPORT_CHAT, style=1), 
        ],
        [btn(_["S_B_4"], callback_data="settings_back_helper", style=3)], # 3 = Orange
        [
            btn(_["S_B_6"], url=config.SUPPORT_CHANNEL, style=4), # 4 = Red
            btn(_["S_B_5"], url="https://t.me/docker_git_bit", style=1)
        ],
    ]
