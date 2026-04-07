import random
from pyrogram.types import InlineKeyboardButton
# Hum enum ko safely import karenge
try:
    from pyrogram.enums import ButtonStyle
except ImportError:
    ButtonStyle = None

import config
from Oneforall import app

# Premium Stickers IDs
STICKERS = [
    6312260233171312151, 5433824103134530018, 5431445213233261748, 
    5431718873433095333, 5443003051411513631, 5431634752706954211
]

def btn(text, style_type="default", **kwargs):
    """
    Style names: 'primary', 'success', 'warning', 'danger'
    """
    premium_id = random.choice(STICKERS)
    
    # Style mapping (Agar Enum fail ho toh integers use honge)
    styles = {
        "primary": getattr(ButtonStyle, "PRIMARY", 1),
        "success": getattr(ButtonStyle, "SUCCESS", 2),
        "warning": getattr(ButtonStyle, "WARNING", 3),
        "danger": getattr(ButtonStyle, "DANGER", 4),
        "default": getattr(ButtonStyle, "DEFAULT", 0)
    }
    
    chosen_style = styles.get(style_type, 0)

    try:
        # Latest Pyrogram version with Premium Icons
        return InlineKeyboardButton(
            text=text,
            icon_custom_emoji_id=premium_id,
            style=chosen_style,
            **kwargs
        )
    except Exception:
        # Agar icon_custom_emoji_id support nahi hai (Old version)
        try:
            return InlineKeyboardButton(text=text, style=chosen_style, **kwargs)
        except Exception:
            # Sabse basic button (No Style, No Icon) - Zero Crash chance
            return InlineKeyboardButton(text=text, **kwargs)

def start_panel(_):
    return [
        [
            btn(_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true", style_type="success"),
            btn(_["S_B_2"], url=config.SUPPORT_CHAT, style_type="primary"),
        ],
    ]

def private_panel(_):
    return [
        [btn(_["S_B_3"], url=f"https://t.me/{app.username}?startgroup=true", style_type="success")],
        [
            btn("ᴇʀᴇɴ ʏᴇᴀɢᴇʀ", url="https://t.me/toxication_infinity", style_type="primary"),
            btn(_["S_B_2"], url=config.SUPPORT_CHAT, style_type="primary"), 
        ],
        [btn(_["S_B_4"], callback_data="settings_back_helper", style_type="warning")],
        [
            btn(_["S_B_6"], url=config.SUPPORT_CHANNEL, style_type="danger"),
            btn(_["S_B_5"], url="https://t.me/docker_git_bit", style_type="primary")
        ],
        [btn("「 ⌯ ᴜᴘᴘєʀϻσσɴ ᴛᴜηєꜱ ⌯ 」", url="https://uppermooninfinity.jo3.org/", style_type="success")],
    ]
