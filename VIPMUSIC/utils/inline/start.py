from pyrogram.types import InlineKeyboardButton
from config import SUPPORT_CHANNEL, SUPPORT_CHAT

import config
from VIPMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text=_["S_B_8"], callback_data="settings_back_helper"),
            InlineKeyboardButton(text=_["S_B_2"], callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(text=_["S_B_3"], url=config.SUPPORT_CHANNEL),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            )
        ],
        [
            InlineKeyboardButton(text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"),
            InlineKeyboardButton(text=_["S_B_3"], url=f"{SUPPORT_CHAT}"),
          ], 
        [
            InlineKeyboardButton(text=_["S_B_8"], callback_data="settings_back_helper")
        ],
    ]
    return buttons
