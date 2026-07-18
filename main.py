import os
import asyncio
import json
from aiohttp import web
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

# خواندن توکن از تنظیمات محیطی (Environment Variable)
# دقت کنید: نباید توکن را اینجا دستی بنویسید!
API_TOKEN = os.getenv('8654381552:AAHwgCU5l99fOsKnSK4ZksetjoKVhXOwSLs')

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# وب‌سرور ساده برای اینکه Render ارور پورت ندهد
async def handle(request):
    return web.Response(text="Bot is running!")

async def start_web_server():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    # استفاده از پورت 10000 که Render می‌پسندد
    site = web.TCPSite(runner, '0.0.0.0', 10000)
    await site.start()

# دستور استارت
@dp.message(Command("start"))
async def start(message: types.Message):
    web_app = types.WebAppInfo(url="https://efn82dri-sys.github.io/ArchitectureBot/")
    kb = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="فرم پذیرش معماران", web_app=web_app)]
    ])
    await message.answer("سلام! برای عضویت در خانواده معماران، فرم زیر را پر کنید:", reply_markup=kb)

# دریافت داده‌ها از وب‌اپ
@dp.message(F.web_app_data)
async def handle_data(message: types.Message):
    data = json.loads(message.web_app_data.data)
    print(f"اطلاعات جدید: {data}")
    await message.answer("ثبت‌نام شما با موفقیت انجام شد!")

async def main():
    # شروع وب‌سرور و ربات به صورت همزمان
    await start_web_server()
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
