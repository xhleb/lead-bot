import asyncio
import os 

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("NO BOT_TOKEN in .env")

dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Hello!")

@dp.message()
async def echo(message: Message):
    text = answers(message)
    await message.answer(text)

def answers(message: Message):
    if message.text is None or not message.text.strip():
        return "I only understand text messages."
    else:
        return f"You said: {message.text}"

async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())