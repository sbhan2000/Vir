import asyncio
import importlib
from sys import argv
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from VIPMUSIC import LOGGER, app, userbot
from VIPMUSIC.core.call import VIP
from VIPMUSIC.misc import sudo
from VIPMUSIC.plugins import ALL_MODULES
from VIPMUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS
from VIPMUSIC import telethn

async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙼𝙳).error("كود جلسة الحساب المساعد غير مدعوم ...")
        
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            if user_id not in BANNED_USERS:
                BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("VIPMUSIC.plugins" + all_module)
    LOGGER("VIPMUSIC.plugins").info("تم تحميل الاضافات ...✓")
    await userbot.start()
    await VIP.start()
    await VIP.decorators()
    LOGGER("𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙼𝙳").info(
            "خطأ .. قم بفتح المكالمة في مجموعة السجل الخاصه بك\n\nجارِ ايقاف بوت الميوزك . . ."
    )
    await idle()
    if len(argv) not in (1, 3, 4):
        await telethn.disconnect()
    else:
        await telethn.run_until_disconnected()
                
    await app.stop()
    await userbot.stop()
    LOGGER("𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙼𝙳").info("جارِ ايقاف بوت الميوزك . . .") 
    

if __name__ == "__main__":
    telethn.start(bot_token=config.BOT_TOKEN)
    asyncio.get_event_loop().run_until_complete(init())
