import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputFile
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
sb = KeyboardButton("Student book audios")
wb = KeyboardButton("Workbook audios")

student = ReplyKeyboardMarkup()
s1 = KeyboardButton("Unit 1")
s2 = KeyboardButton("Unit 2")
s3 = KeyboardButton("Unit 3")
s4 = KeyboardButton("Unit 4")
s5 = KeyboardButton("Unit 5")
s6 = KeyboardButton("Unit 6")
s7 = KeyboardButton("Unit 7")
s8 = KeyboardButton("Unit 8")
s9 = KeyboardButton("Unit 9")
s10 = KeyboardButton("Unit 10")
back = KeyboardButton("🔙Back")
student.add(s1, s2, s3, s4, s5, s6, s7, s8, s9, s10)
student.add(back)

workbook = ReplyKeyboardMarkup()
wb1 = KeyboardButton("Workbook Unit 1")
wb2 = KeyboardButton("Workbook Unit 2")
wb3 = KeyboardButton("Workbook Unit 3")
wb4 = KeyboardButton("Workbook Unit 4")
wb5 = KeyboardButton("Workbook Unit 5")
wb6 = KeyboardButton("Workbook Unit 6")
wb7 = KeyboardButton("Workbook Unit 7")
wb8 = KeyboardButton("Workbook Unit 8")
wb9 = KeyboardButton("Workbook Unit 9")
wb10 = KeyboardButton("Workbook Unit 10")
back = KeyboardButton("🔙Back")
workbook.add(wb1, wb2, wb3, wb4, wb5, wb6, wb7, wb8, wb9, wb10)
workbook.add(back)

menu = ReplyKeyboardMarkup()
menu.add(sb)
menu.add(wb)

API_TOKEN = '7398712364:AAFfkokKUFobK_S2SMLkAdPoy09Y_BXu2vA'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(f"Hello, {message.from_user.full_name}👋. Welcome to the bot."
                        f"\nChoose one of them 👇.", reply_markup=menu)
    print(message.from_user.username)

@dp.message_handler()
async def send_student(message: types.Message):
    if message.text == "Student book audios":
        await message.answer("Student book audios 🎧", reply_markup=student)
    elif message.text == "Unit 1":
        await bot.send_message(message.from_user.id, "Sending...")
        await bot.send_audio(message.from_user.id, InputFile("Unit 1/Track 01.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 1/Track 02.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 1/Track 03.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 1/Track 04.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 1/Track 05.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 1/Track 06.mp3"))
        await bot.send_message(message.from_user.id, "Unit 1 audios sent successful")
    elif message.text == "Unit 2":
        await bot.send_message(message.from_user.id,"Sending...")
        await bot.send_audio(message.from_user.id, InputFile("Unit 2/Track 07.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 2/Track 08.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 2/Track 09.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 2/Track 10.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 2/Track 11.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 2/Track 12.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 2/Track 13.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 2/Track 14.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 2/Track 15.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 2/Track 16.mp3"))
        await bot.send_message(message.from_user.id, "Unit 2 audios sent successful")
    elif message.text == "Unit 3":
        await bot.send_message(message.from_user.id, "Sending...")
        await bot.send_audio(message.from_user.id, InputFile("Unit 3/Track 17.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 3/Track 18.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 3/Track 19.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 3/Track 20.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 3/Track 21.mp3"))
        await bot.send_message(message.from_user.id, "Unit 3 audios sent successful")
    elif message.text == "Unit 4":
        await bot.send_message(message.from_user.id, "Sending...")
        await bot.send_audio(message.from_user.id, InputFile("Unit 4/Track 22.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 4/Track 23.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 4/Track 24.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 4/Track 25.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 4/Track 26.mp3"))
        await bot.send_message(message.from_user.id, "Unit 4 audios sent successful")
    elif message.text == "Unit 5":
        await bot.send_message(message.from_user.id, "Sending...")
        await bot.send_audio(message.from_user.id, InputFile("Unit 5/Track 27.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 5/Track 28.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 5/Track 29.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 5/Track 30.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 5/Track 31.mp3"))
        await bot.send_message(message.from_user.id, "Unit 5 audios sent successful")
    elif message.text == "Unit 6":
        await bot.send_message(message.from_user.id, "Sending...")
        await bot.send_audio(message.from_user.id, InputFile("Unit 6/Track 01.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 6/Track 02.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 6/Track 03.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 6/Track 04.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 6/Track 05.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 6/Track 06.mp3"))
        await bot.send_message(message.from_user.id, "Unit 6 audios sent successful")
    elif message.text == "Unit 7":
        await bot.send_message(message.from_user.id, "Sending...")
        await bot.send_audio(message.from_user.id, InputFile("Unit 7/Track 07.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 7/Track 08.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 7/Track 09.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 7/Track 10.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 7/Track 11.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 7/Track 12.mp3"))
        await bot.send_message(message.from_user.id, "Unit 7 audios sent successful")
    elif message.text == "Unit 8":
        await bot.send_message(message.from_user.id, "Sending...")
        await bot.send_audio(message.from_user.id, InputFile("Unit 8/Track 13.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 8/Track 14.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 8/Track 15.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 8/Track 16.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 8/Track 17.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 8/Track 18.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 8/Track 19.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 8/Track 20.mp3"))
        await bot.send_message(message.from_user.id, "Unit 8 audios sent successful")
    elif message.text == "Unit 9":
        await bot.send_message(message.from_user.id, "Sending...")
        await bot.send_audio(message.from_user.id, InputFile("Unit 9/Track 21.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 9/Track 22.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 9/Track 23.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 9/Track 24.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 9/Track 25.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 9/Track 26.mp3"))
        await bot.send_message(message.from_user.id, "Unit 9 audios sent successful")
    elif message.text == "Unit 10":
        await bot.send_message(message.from_user.id, "Sending...")
        await bot.send_audio(message.from_user.id, InputFile("Unit 10/Track 27.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 10/Track 28.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 10/Track 29.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Unit 10/Track 30.mp3"))
        await bot.send_message(message.from_user.id, "Unit 10 audios sent successful")
    elif message.text == "🔙Back":
        await bot.send_message(message.from_user.id, "Back to main menu", reply_markup=menu)

    elif message.text == "Workbook audios":
        await message.answer("Workbook audios 🎧", reply_markup=workbook)
    elif message.text == "Workbook Unit 1":
        await bot.send_message(message.from_user.id, "Sending...")
        await bot.send_audio(message.from_user.id, InputFile("Workbook 1/Track 01.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Workbook 1/Track 02.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Workbook 1/Track 03.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Workbook 1/Track 04.mp3"))
        await bot.send_message(message.from_user.id, "Workbook Unit 1 Audios sent successful")

    elif message.text == "Workbook Unit 2":
        await bot.send_message(message.from_user.id, "Sending...")
        await bot.send_audio(message.from_user.id, InputFile("Workbook 2/Track 05.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Workbook 2/Track 06.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Workbook 2/Track 07.mp3"))
        await bot.send_message(message.from_user.id, "Workbook Unit 2 Audios sent successful")

    elif message.text == "Workbook Unit 3":
        await bot.send_message(message.from_user.id, "Sending...")
        await bot.send_audio(message.from_user.id, InputFile("Workbook 3/Track 08.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Workbook 3/Track 09.mp3"))
        await bot.send_message(message.from_user.id, "Workbook Unit 3 Audios sent successful")

    elif message.text == "Workbook Unit 4":
        await bot.send_message(message.from_user.id, "Sending...")
        await bot.send_audio(message.from_user.id, InputFile("Workbook 4/Track 10.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Workbook 4/Track 11.mp3"))
        await bot.send_message(message.from_user.id, "Workbook Unit 3 Audios sent successful")

    elif message.text == "Workbook Unit 5":
        await bot.send_message(message.from_user.id, "Sending...")
        await bot.send_audio(message.from_user.id, InputFile("Workbook 5/Track 12.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Workbook 5/Track 13.mp3"))
        await bot.send_message(message.from_user.id, "Workbook Unit 5 Audios sent successful")

    elif message.text == "Workbook Unit 6":
        await bot.send_message(message.from_user.id, "Sending...")
        await bot.send_audio(message.from_user.id, InputFile("Workbook 6/Track 14.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Workbook 6/Track 15.mp3"))
        await bot.send_message(message.from_user.id, "Workbook Unit 6 Audios sent successful")

    elif message.text == "Workbook Unit 7":
        await bot.send_message(message.from_user.id, "Sending...")
        await bot.send_audio(message.from_user.id, InputFile("Workbook 7/Track 16.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Workbook 7/Track 17.mp3"))
        await bot.send_message(message.from_user.id, "Workbook Unit 7 Audios sent successful")

    elif message.text == "Workbook Unit 8":
        await bot.send_message(message.from_user.id, "Sending...")
        await bot.send_audio(message.from_user.id, InputFile("Workbook 8/Track 18.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Workbook 8/Track 19.mp3"))
        await bot.send_message(message.from_user.id, "Workbook Unit 8 Audios sent successful")

    elif message.text == "Workbook Unit 9":
        await bot.send_message(message.from_user.id, "Sending...")
        await bot.send_audio(message.from_user.id, InputFile("Workbook 9/Track 20.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Workbook 9/Track 21.mp3"))
        await bot.send_message(message.from_user.id, "Workbook Unit 9 Audios sent successful")

    elif message.text == "Workbook Unit 10":
        await bot.send_message(message.from_user.id, "Sending...")
        await bot.send_audio(message.from_user.id, InputFile("Workbook 10/Track 22.mp3"))
        await bot.send_audio(message.from_user.id, InputFile("Workbook 10/Track 23.mp3"))
        await bot.send_message(message.from_user.id, "Workbook Unit 10 Audios sent successful")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
