from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
import asyncio
import json

# توکن خود را اینجا قرار دهید
API_TOKEN = '8654381552:AAHwgCU5l99fOsKnSK4ZksetjoKVhXOwSLs'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# دستور استارت
@dp.message(Command("start"))
async def start(message: types.Message):
    # دکمه‌ای که وب‌اپ را باز می‌کند
    web_app = types.WebAppInfo(url="https://efn82dri-sys.github.io/ArchitectureBot/")
    kb = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="فرم پذیرش معماران", web_app=web_app)]
    ])
    await message.answer("سلام! برای عضویت در خانواده معماران، فرم زیر را پر کنید:", reply_markup=kb)

# دریافت داده‌ها از وب‌اپ
@dp.message(F.web_app_data)
async def handle_data(message: types.Message):
    data = json.loads(message.web_app_data.data)
    # در اینجا می‌توانید داده‌ها را در دیتابیس یا فایل ذخیره کنید
    print(f"اطلاعات جدید: {data}")
    await message.answer("ثبت‌نام شما با موفقیت انجام شد!")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
