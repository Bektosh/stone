from aiogram import Bot, Dispatcher
import asyncio
import logging
from handlers import router
from config import token

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=token)
dp = Dispatcher()


async def start():
    dp.include_router(router)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())