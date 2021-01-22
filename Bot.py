from aiogram import Bot, Dispatcher, executor, types, asyncio, exceptions
import os
import datetime
import re
import yadisk

path = os.path.dirname(os.path.abspath(__file__)) + "//"
os.chdir(path)
y = yadisk.YaDisk(token="AgAAAAA__BuSAAbRSsDZZ-SDy0k1kkH-KTpZJaE")
token = '1565891278:AAFYvbj4dDy5UCZesONpdd5W4DJR6xpSIIk'
bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(content_types=['photo'])
async def PhotoCheck(message: types.Message):
    time = datetime.datetime.now()
    time = re.sub("[$|@|&|,|!|#|$|%|^|&|*|(|)|:|<|>|?|,|.|/|]",".",str(time))
    await message.photo[-1].download("{}.{}".format(message.chat.username, time) + '.png')
    await message.answer("Фото скачано, начинаю загрузку в облако...")
    name = "{}.{}.png".format(message.chat.username, time)
    folder = "/Photos/{}".format(name)
    y.upload(name, "/Photos/{}".format(name))
    y.publish("/Photos/{}".format(name))
    folder = y.get_meta(folder)
    os.remove(name)
    await message.answer("Ссылка на облако -", folder["public_url"])

@dp.message_handler(content_types=['document'])
async def DocumentCheck(message: types.Message):
    DocumentDict = message.document
    DocumentDict = DocumentDict['file_name']
    name = DocumentDict
    try:
        time = datetime.datetime.now()
        time = re.sub("[$|@|&|,|!|#|$|%|^|&|*|(|)|:|<|>|?|,|.|/|]",".",str(time))
        await message.document.download(DocumentDict)
        await message.answer("Файл скачан, начинаю загрузку в облако...")
        folder = "/Documents/{}".format(name)
        try:
            y.upload(name, "/Documents/{}".format(name))
        except:
            pass
        y.publish("/Documents/{}".format(name))
        folder = y.get_meta(folder)
        y.publish("/Documents/{}".format(name))
        url = folder["public_url"]
        print(y.exists("/Documents/{}".format(name)))
        await message.answer(url)
    except yadisk.exceptions.PathExistsError:
        folder = "/Documents/{}".format(name)
        folder = y.get_meta(folder)
        url = folder["public_url"]
        await message.answer("Файл уже существует -", url)
    finally:
        os.remove(name)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)