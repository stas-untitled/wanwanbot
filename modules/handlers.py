from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import ChatTypeFilter

from modules.database import get_or_create_user
from modules.keyboards import get_settings_keyboard

router = Router()

@router.message(F.text.lower() == "инфо")
async def cmd_info(message: Message):
	"""Обработка команды 'инфо' (работает везде)."""
	# user_id, nickname, race, profession, balance, experience
	user = await get_or_create_user(message.from_user.id)

	# Строго по списку, как ты просил
	text = (
		f"Ник: {user[1]}\n"
		f"Раса: {user[2]}\n"
		f"Профессия: {user[3]}\n"
		f"Баланс: {user[4]}\n"
		f"Опыт: {user[5]}"
	)
	await message.answer(text)

@router.message(F.text.lower() == "настройки", ChatTypeFilter(chat_types=["private"]))
async def cmd_settings(message: Message):
	"""Обработка команды 'настройки' (работает ТОЛЬКО в личных сообщениях)."""
	user = await get_or_create_user(message.from_user.id)

	text = (
		f"Ваши текущие значения:\n"
		f"Ник: {user[1]}\n"
		f"Раса: {user[2]}\n"
		f"Профессия: {user[3]}\n\n"
		f"Выберите, что хотите изменить:"
	)

	await message.answer(text, reply_markup=get_settings_keyboard())

# --- Заглушки для инлайн-кнопок (чтобы бот не выдавал ошибку при нажатии) ---
@router.callback_query(F.data == "change_nick")
async def process_change_nick(callback: CallbackQuery):
	await callback.message.edit_text("⚙️ Функция изменения ника будет реализована в следующем шаге.")
	await callback.answer()

@router.callback_query(F.data == "change_prof")
async def process_change_prof(callback: CallbackQuery):
	await callback.message.edit_text("⚙️ Функция выбора профессии будет реализована в следующем шаге.")
	await callback.answer()

@router.callback_query(F.data == "change_race")
async def process_change_race(callback: CallbackQuery):
	await callback.message.edit_text("⚙️ Функция смены расы будет реализована в следующем шаге.")
	await callback.answer()
