from aiogram import F, Bot, Dispatcher, types
from handlers import start, faq, about_dev, main_menu, learning, training
from config_reader import config
import asyncio
import logging


bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()

dp.include_routers(
    start.router,
    faq.router,
    about_dev.router,
    main_menu.router,
    learning.router,
    training.router
)

logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.INFO, filename='bot.log',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

async def main():
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())