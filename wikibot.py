from aiogram import Bot, Dispatcher, types, executor
import wikipedia
wikipedia.set_lang("uz")


bot = Bot("6602375626:AAHNRtONPDJg6bGpsBOsXSwt2I8AOSoFe1U")

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer("salom sizga nima yordam berishimiz mumkin")
    
@dp.message_handler(content_types=['text'])
async def text_handler(message: types.Message):
    text = message.text
    mid = await message.answer("⌛️")
    try:
        await message.answer(wikipedia.summary(text))
    except:
        await message.answer("malumot topilmadi")
    await mid.delete()
    
executor.start_polling(dp)