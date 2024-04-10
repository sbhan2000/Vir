from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config

from ..logging import LOGGER


class VIP(Client):
    def __init__(self):
        LOGGER(𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙼𝙳).info(f"تـم تـشغيل الـبوت بـنجاح... ")
        super().__init__(
            name="VIPMUSIC",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=f"<u><b>» {self.mention} 🥤| تـم تـشغيل بـوت :</b><u>\n\n🥤|أيـدي الـبوت : <code>{self.id}</code>\n\n🥤| اسـم الـبوت : {self.name}\n\n🥤| يـوزر الـبوت : @{self.username}",
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙼𝙳).error(
                "قـم بـأضافة البوت الى المجموعه ورفعه مشرف وفتح اتصال"
            )
            
        except Exception as ex:
            LOGGER(𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙼𝙳).error(
                f"لـم يـسطتع الـبوت الـوصول الى الـمجموعه.\n  بسبب : {type(ex).__name__}."
            )
            

        a = await self.get_chat_member(config.LOGGER_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙼𝙳).error(
                "مـن فضلك قـم بـرفع الـبوت مـشرف وفـتح اتـصال. "
            )
            
        LOGGER(𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙼𝙳).info(f"🥤| تـم تـشغيل بـوت {self.name} بـنجاح. ")

    async def stop(self):
        await super().stop()
