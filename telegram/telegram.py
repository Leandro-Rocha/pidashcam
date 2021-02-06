from decouple import config

from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = config('API_TOKEN')
SNAPSHOT_FILE = config('SNAPSHOT_FILE')

bot = Bot(token=API_TOKEN)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands=['snapshot'])
async def send_welcome(message: types.Message):
    await message.answer("Taking snapshot...")
    try:
        await message.answer_photo(types.InputFile(SNAPSHOT_FILE))
    except Exception as e:
        await message.answer("Snapshot unavailable 😪")
        print(str(e))

if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)
