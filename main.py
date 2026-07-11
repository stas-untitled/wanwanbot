import asyncio
import logging
from os import getenv
from aiogram import Bot, Dispatcher

from modules.database import init_db
from modules.handlers import router as handlers_router

async def main():
	# Настройка логирования
	logging.basicConfig(
		level=logging.INFO,
		format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
	)

	# Инициализация БД при старте
	await init_db()

	bot = Bot(token=getenv(BOT_TOKEN))
	dp = Dispatcher()

	# Подключаем роутер с обработчиками
	dp.include_router(handlers_router)

	logging.info("Бот успешно запущен!")

	# Запуск пулинга
	await dp.start_polling(bot)

if __name__ == "__main__":
	try:
		asyncio.run(main())
	except (KeyboardInterrupt, SystemExit):
		logging.info("Бот остановлен.")
