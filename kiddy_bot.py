import logging
from aiogram import Bot, Dispatcher, executor, types

# የገባልህ ትክክለኛ ቶከን
API_TOKEN = '8873571450:AAHATMTf2iaSj2VJEkmYMZ47Gs5We4TGg_w'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("ሰላም! እኔ የአንተ ቦት ነኝ። እየሰራሁ ነው!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
