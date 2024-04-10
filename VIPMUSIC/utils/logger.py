from pyrogram.enums import ParseMode

from VIPMUSIC import app
from VIPMUSIC.utils.database import is_on_off
from config import LOGGER_ID


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
<b>{app.mention} بـدء بـتشغيل</b>

<b>🥤| أيـدي الـكروب :</b> <code>{message.chat.id}</code>
<b>🥤| أسـم الـكروب :</b> {message.chat.title}
<b>🥤| يـوزر الكروب :</b> @{message.chat.username}

<b>🥤| أيـدي الـعضو :</b> <code>{message.from_user.id}</code>
<b>🥤| اسـم الـعضو :</b> {message.from_user.mention}
<b>🥤| يـوزر الـعضو :</b> @{message.from_user.username}

<b>🥤| تـم تـشغيل :</b> {message.text.split(None, 1)[1]}
<b>🥤| نـوع التشغيل :</b> {streamtype}"""
        if message.chat.id != LOGGER_ID:
            try:
                await app.send_message(
                    chat_id=LOGGER_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
