import config
import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters import Command

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=config.TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def welcome(message: types.Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="В КАТАЛОГ ТОВАРОВ", web_app=WebAppInfo(url='https://opermayki.ru/'))],
        [InlineKeyboardButton(text="О нашем интернет магазине", callback_data='about')],
        [InlineKeyboardButton(text="Наши контакты", callback_data='cont')]
    ])
    await message.answer(
        f"Здравствуйте, <b>{message.from_user.first_name}</b>!\nЭто магазин - Technik.",
        parse_mode='html',
        reply_markup=markup
    )

# Обработчик callback-запросов
@dp.callback_query()
async def cbm(callback: types.CallbackQuery):
    if callback.data == 'cont':
        back_markup = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="В главное меню", callback_data='back_to_main')]
        ])
        await callback.message.answer(
            "<b>Контакты</b>\n \nг. Феодосия\n \n+79781234567\n \nОтвечаем: с 10:00 до 20:00 ежедневно\n \nПочта: technikshop@gmail.com\n \nРежим работы онлайн-магазина: круглосуточно",
            parse_mode='HTML',
            reply_markup=back_markup
        )
    elif callback.data == 'about':
        back_markup = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="В главное меню", callback_data='back_to_main')]
        ])
        await callback.message.answer(
            "Магазин Technik, все товары отличного качества",
            reply_markup=back_markup
        )
    elif callback.data == 'back_to_main':
        markup = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="В КАТАЛОГ ТОВАРОВ", web_app=WebAppInfo(url='https://opermayki.ru/'))],
            [InlineKeyboardButton(text="О нашем интернет магазине", callback_data='about')],
            [InlineKeyboardButton(text="Наши контакты", callback_data='cont')]
        ])
        await callback.message.answer(
            "Вы вернулись в главное меню нашего магазина",
            reply_markup=markup
        )

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
