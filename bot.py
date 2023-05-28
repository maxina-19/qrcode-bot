import logging
from aiogram import Bot, Dispatcher, executor, types

import qrcode
import os

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "6043834139:AAETK-COlxvalQs9J6XM0Nz7s6PfFlJR1Zs"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_bot_handler(message: types.Message):
    await message.answer("Assalomu Alaykum.\n\nBu bot orgali siz QR kod yasay olasiz!")

@dp.message_handler(content_types=['text'])
async def generate_qrcode_handler(message: types.Message):
    img = qrcode.make(message.text)
    filename = "qr_result.png"
    img.save(filename)
    await message.answer_photo(types.InputFile(filename), caption="✅ Tayyor")
    os.remove(filename)
    #os.unlink(filename) remove == unlink

if __name__ == '__main__':
    executor.start_polling(dp)