import aiosqlite

DB_NAME = "bot_database.db"

async def init_db():
	"""Создание таблицы users, если она не существует."""
	async with aiosqlite.connect(DB_NAME) as db:
		await db.execute('''
			CREATE TABLE IF NOT EXISTS users (
				user_id INTEGER PRIMARY KEY,
				nickname TEXT DEFAULT 'Не указано',
				race TEXT DEFAULT 'Не указана',
				profession TEXT DEFAULT 'Не указана',
				balance INTEGER DEFAULT 0,
				experience INTEGER DEFAULT 0
			)
		''')
		await db.commit()

async def get_or_create_user(user_id: int) -> tuple:
	"""Получает пользователя из БД. Если его нет - создает с дефолтными значениями."""
	async with aiosqlite.connect(DB_NAME) as db:
		async with db.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)) as cursor:
			row = await cursor.fetchone()
			if row:
				return row

			# Если пользователя нет, создаем его
			await db.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
			await db.commit()

			# Возвращаем только что созданную запись
			async with db.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)) as cursor:
				return await cursor.fetchone()
