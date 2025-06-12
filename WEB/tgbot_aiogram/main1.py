import logging
from config import BOT_TOKEN
from telegram import ForceReply, Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import datetime

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)  # логгирование
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update,
                context: ContextTypes.DEFAULT_TYPE) -> None:  # update и context передаются всегда, это обработчик старт
    """Send a message when the command /start is issued."""
    markup = await keyb(context, update)
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",  # user.mention_html - никнейм пользователя
        reply_markup=markup,
    )  # forcereply - заставляет пользователя отвечать на сообщение hi user


async def keyb(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["/start", "/help"], ["/time", "/date"]]
    markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=False)
    return markup


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(f"Я получил сообщение {update.message.text}")


async def time_now(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(f"Время сейчас {datetime.datetime.now().strftime("%H:%M:%S")}")


async def date_now(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(f"Сегодняшняя дата {datetime.date.today()}")


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(BOT_TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    # add_handler - обработчик комманд слева - комманда, справа - функция которая за нее отвечает
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("time", time_now))
    application.add_handler(CommandHandler("date", date_now))
    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,
                                           echo))  # командные задачи выполнять не нужно, за это отвечает add_handler

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
