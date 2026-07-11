from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_settings_keyboard() -> InlineKeyboardMarkup:
	"""Создает инлайн-клавиатуру для меню настроек."""
	keyboard = InlineKeyboardMarkup(inline_keyboard=[
		[InlineKeyboardButton(text="Изменить ник", callback_data="change_nick")],
		[InlineKeyboardButton(text="Выбрать профессию", callback_data="change_prof")],
		[InlineKeyboardButton(text="Сменить расу", callback_data="change_race")]
	])
	return keyboard
