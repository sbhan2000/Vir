import socket
import time

import heroku3
from pyrogram import filters

import config
from VIPMUSIC.core.mongo import mongodb

from .logging import LOGGER

SUDOERS = filters.user()

HAPP = None
_boot_ = time.time()


def is_heroku():
    return "heroku" in socket.getfqdn()


XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    str(config.HEROKU_API_KEY),
    "https",
    str(config.HEROKU_APP_NAME),
    "HEAD",
    "master",
]


def dbb():
    global db
    db = {}
    LOGGER(𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙼𝙳).info(f"تم تحديث قاعدة بيانات البوت ...✓")


async def sudo():
    global SUDOERS
    SUDOERS.add(config.OWNER_ID)
    sudoersdb = mongodb.sudoers
    sudoers = await sudoersdb.find_one({"sudo": "sudo"})
    sudoers = [] if not sudoers else sudoers["sudoers"]
    if config.OWNER_ID not in sudoers:
        sudoers.append(config.OWNER_ID)
        await sudoersdb.update_one(
            {"sudo": "sudo"},
            {"$set": {"sudoers": sudoers}},
            upsert=True,
        )
    if sudoers:
        for user_id in sudoers:
            SUDOERS.add(user_id)
    LOGGER(𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙼𝙳).info(f" تم تحميل قائمة مطورين البوت ...✓")


def heroku():
    global HAPP
    if is_heroku:
        if config.HEROKU_API_KEY and config.HEROKU_APP_NAME:
            try:
                Heroku = heroku3.from_key(config.HEROKU_API_KEY)
                HAPP = Heroku.app(config.HEROKU_APP_NAME)
                LOGGER(𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙼𝙳).info(f"تم إضافة فارات البوت ...✓")
            except BaseException:
                LOGGER(𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙼𝙳).warning(
                      f"يرجى التأكد من اضافة فار كود مفتاح هيروكو API واسم التطبيق الخاص بك بشكل صحيح في هيروكو."
                )
