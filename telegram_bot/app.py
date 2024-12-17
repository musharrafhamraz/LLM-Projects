import os
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from commands import start_command, help_command, custom_command
from handler import handle_message, error
from constants import TELEGRAM_API_KEY

load_dotenv()

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TELEGRAM_API_KEY).build()

    # Register command handlers
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Register message handlers
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Register error handlers
    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=3)
