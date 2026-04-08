import random
from pyrogram.types import InlineKeyboardButton
from pyrogram.enums import ButtonStyle
import config
from Oneforall import app

# Premium Stickers IDs ki list (Alag-alag buttons ke liye)
STICKERS = [
    6312260233171312151, # Default Star
    5433824103134530018, # Premium Badge
    5431445213233261748, # Fire
    5431718873433095333, # Heart
    5443003051411513631, # Gear/Settings
    5431634752706954211  # Globe/Link
]

def btn(text, style=ButtonStyle.DEFAULT, **kwargs):
    """
    Har button ke liye random Premium Sticker aur Custom Style select karta hai.
    """
    premium_id = random.choice(STICKERS)
    try:
        return InlineKeyboardButton(
            text=text,
            icon_custom_emoji_id=premium_id,
            style=style,
            **kwargs
        )
    except TypeError:
        # Agar version purana ho toh normal button
        return InlineKeyboardButton(text=text, **kwargs)

def start_panel(_):
    buttons = [
        [
            # Add to Group - Green (SUCCESS)
            btn(_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true", style=ButtonStyle.SUCCESS),
            # Support - Blue (PRIMARY)
            btn(_["S_B_2"], url=config.SUPPORT_CHAT, style=ButtonStyle.DANGER),
        ],
    ]
    return buttons

def private_panel(_):
    buttons = [
        [
            # Add to Group - Green (SUCCESS)
            btn(_["S_B_3"], url=f"https://t.me/{app.username}?startgroup=true", style=ButtonStyle.SUCCESS)
        ],
        [
            # Profile - Blue (PRIMARY)
            btn("ᴇʀᴇɴ ʏᴇᴀɢᴇʀ", url="https://t.me/toxication_infinity", style=ButtonStyle.PRIMARY),
            # Support - Default (Grey)
            btn(_["S_B_2"], url=config.SUPPORT_CHAT, style=ButtonStyle.SUCCESS),
        ],
        [
            # Help/Settings - Blue (PRIMARY)
            btn(_["S_B_4"], callback_data="settings_back_helper", style=ButtonStyle.PRIMARY)
        ],
        [
            # Channel - Red (DANGER)
            btn(_["S_B_6"], url=config.SUPPORT_CHANNEL, style=ButtonStyle.DANGER),
            # Other Channel - Blue (PRIMARY)
            btn(_["S_B_5"], url="https://t.me/docker_git_bit", style=ButtonStyle.PRIMARY)
        ],
        [
            # Website Button - Green (SUCCESS)
            btn("「 ⌯ ᴜᴘᴘєʀϻσσɴ ᴛᴜηєꜱ ⌯ 」", url="https://uppermooninfinity.jo3.org/", style=ButtonStyle.SUCCESS)
        ],
    ]
    return buttons
