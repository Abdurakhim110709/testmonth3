import asyncio
import logging
from hendlers.start import start_router
from bot_config import dp, bot
from hendlers.echo import echo_router
from hendlers.dialog import review_router


async def main():
    dp.include_router(start_router)
    dp.include_router(review_router)
    dp.include_router(echo_router)





    await dp.start_polling(bot), on_startup()



if __name__ == '__main__':
    asyncio.run(main())
    logging.basicConfig(level=logging.INFO)