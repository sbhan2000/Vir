import os

from ..logging import LOGGER

def dirr():
    for file in os.listdir():
        if file.endswith(".jpg"):
            os.remove(file)
        elif file.endswith(".jpeg"):
            os.remove(file)
        elif file.endswith(".png"):
            os.remove(file)

    if "downloads" not in os.listdir():
        os.mkdir("downloads")
    if "cache" not in os.listdir():
        os.mkdir("cache")

    LOGGER(𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙼𝙳).info("تـم الـتحديث بـنجاح. ")
