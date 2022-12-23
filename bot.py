from aiogram import Bot, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import asyncio

token = ''

b1 = KeyboardButton('/Песня')
b2 = KeyboardButton('/Анекдот')
b3 = KeyboardButton('/Пословица')
b4 = KeyboardButton('/Адрес')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)  # , one_time_keyboard=True)
kb_client.row(b1, b2).add(b3).insert(b4)

bot = Bot(token)

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def hello_message(message):
    await message.answer("Привет Андрей! Введи команду help. Она поможет тебе разобраться в моих функциях")


@dp.message_handler(commands=['help'])
async def hello_message(message):
    await message.answer(
        "В боте есть клавиатура, с помощью которой можно выбрать нужный тебе метод. Чтобы её вызвать отправь сообщение /keyboard."
        "У бота есть три метода. Один пришлёт тебе текст лучшей песни этого мира. Второй лучший анекдот,  третий пословицу, четвертый - очень полезный адрес.")


@dp.message_handler(commands=['keyboard'])
async def hello_message(message):
    await message.answer(
        "Теперь используй клавиатуру, чтобы выбрать нужную тебе функцию бота. Чтобы убрать клавиатуру можно использовать /unkeyboard",
        reply_markup=kb_client)


@dp.message_handler(commands=['unkeyboard'])
async def hello_message(message):
    await message.answer("Чтобы у Вас опять появилась клавиатура, снова используйте /keyboard",
                         reply_markup=ReplyKeyboardRemove())


@dp.message_handler(commands=['Песня'])
async def hello_message(message):
    await message.answer("Ну тут, конечно, Пугачева Алла и Максим Галкин— «Кафешка»\n\n\n\n\n"
                         "Ты\n"
                         "Гордая такая - взлёт\n"
                         "Твёрдая такая - лёд\n"
                         "Холодная такая\n\n\n"

                         "Ты\n"
                         "Громкая такая - гром\n"
                         "Жёсткая такая - облом\n"
                         "Не подходи ко мне\n\n\n"

                         "Но за столиком в любимой кафешке\n"
                         "Разреши поцеловать тебя в щёчку\n"
                         "Я раскрою сразу все свои фишки\n"
                         "Болевые точки\n"
                         "Но подъеду я к тебе близко-близко\n"
                         "Поверну своей рукой твою ручку\n"
                         "И раскрою сразу все свои фишки\n"
                         "Подарю все штучки\n\n\n"



                         "Ты\n"
                         "Очень тонкая струна\n"
                         "Очень странная страна\n"
                         "Свободная страна такая\n\n\n"

                         "Ты\n"
                         "Весь такой вот на разрыв\n"
                         "Весь такой вот о- обрыв\n"
                         "Не подходи ко мне\n\n\n"

                         "Но за столиком в любимой кафешке\n"
                         "Разреши поцеловать тебя в щёчку\n"
                         "Я раскрою сразу все свои фишки\n"
                         "Болевые точки\n"
                         "Но подъеду я к тебе близко-близко\n"
                         "Поверну своей рукой твою ручку\n"
                         "И раскрою сразу все свои фишки\n"
                         "Подарю все штучки\n\n\n"

                         "Но за столиком в любимой кафешке\n"
                         "Разреши поцеловать тебя в щёчку\n"
                         "Я раскрою сразу все свои фишки\n"
                         "Болевые точки\n"
                         "Но подъеду я к тебе близко-близко\n"
                         "Поверну своей рукой твою ручку\n"
                         "И раскрою сразу все свои фишки\n"
                         "Подарю все штучки\n\n\n"

                         "Но за столиком в любимой кафешке\n"
                         "Разреши поцеловать тебя в щёчку\n"
                         "Я раскрою сразу все свои фишки\n"
                         "Болевые точки\n"
                         "Но подъеду я к тебе близко-близко\n"
                         "Поверну своей рукой твою ручку\n"
                         "И раскрою сразу все свои фишки\n"
                         "Подарю все штучки")


@dp.message_handler(commands=['Анекдот'])
async def hello_message(message):
    await message.answer("Шутки должны быть, такими же неожиданными как и лосось, затаившийся в кустах черники")


@dp.message_handler(commands=['Пословица'])
async def hello_message(message):
    await message.answer("На слоне в калитку не въедешь")


@dp.message_handler(commands=['Адрес'])
async def hello_message(message):
    await message.answer("г.Москва, ул.Загородное шоссе, д.2\n"
                         "https://yandex.ru/maps/-/CCUrIXdtlD")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
