import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from dotenv import load_dotenv

# Загружаем переменные из файла .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Функция обработки команды /start
def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Открыть магазин", web_app=WebAppInfo(url="https://your-webapp-url.com"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Добро пожаловать в наш магазин!', reply_markup=reply_markup)

# Обработка нажатий кнопок
def button(update: Update, context):
    query = update.callback_query
    query.answer()

    # Обработка различных запросов
    if query.data == 'menu':
        query.edit_message_text(text="Выберите категорию:")

# Основная функция для запуска бота
def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Обработчик команды /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
