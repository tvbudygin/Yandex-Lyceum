import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

# Bot token can be obtained via https://t.me/BotFather
from config import BOT_TOKEN

# Клавиатура
reply_keyboard = [[KeyboardButton(text='/address'), KeyboardButton(text='/phone')],
                  [KeyboardButton(text='/site'), KeyboardButton(text='/work_time')],
                  [KeyboardButton(text='/stop')],
                  ]
markup = ReplyKeyboardMarkup(keyboard=reply_keyboard,
                             one_time_keyboard=False,
                             resize_keyboard=True)

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


@dp.message(Command('start'))
async def start(message: Message) -> None:
    await message.reply(f"Привет! Смотри клавиатуру снизу...", reply_markup=markup)


@dp.message(Command('stop'))
async def stop(message: Message) -> None:
    await message.reply(f"Пока! Клавиатура была закрыта.", reply_markup=ReplyKeyboardRemove())


@dp.message(Command('help'))
async def help(message: Message) -> None:
    await message.reply(f"тут нам когданибудь помогут.")


@dp.message(Command('address'))
async def address(message: Message) -> None:
    await message.reply(f"Адрес компании")


@dp.message(Command('phone'))
async def phone(message: Message) -> None:
    await message.reply(f"Телефон: 123-45-67")


@dp.message(Command('site'))
async def site(message: Message) -> None:
    await message.reply(f"Сайт компании")


@dp.message(Command('work_time'))
async def work_time(message: Message) -> None:
    await message.reply(f"Рабочее время: бесконечно")


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender
    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
