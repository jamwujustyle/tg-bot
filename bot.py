"""
Telegram бот: Пифагор Учитель 📐
Бот для изучения обратной теоремы Пифагора
Handle: @pythagoras_teacher_bot (или ваш собственный)
"""

import logging
from telegram import (
    Update,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
    ContextTypes,
)

# Настройка логирования
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Вопросы теста
QUESTIONS = [
    {
        "question": "1️⃣ Является ли треугольник со сторонами 6, 8 и 10 прямоугольным?",
        "answer": "да",
        "explanations": {
            "да": "✅ Верно! 6² + 8² = 36 + 64 = 100 = 10².",
            "нет": "❌ Неверно. Треугольник является прямоугольным, так как 6² + 8² = 10².",
        },
    },
    {
        "question": "2️⃣ Является ли треугольник со сторонами 7, 24 и 25 прямоугольным?",
        "answer": "да",
        "explanations": {
            "да": "✅ Отлично! 7² + 24² = 49 + 576 = 625 = 25².",
            "нет": "❌ Неверно. Треугольник является прямоугольным, так как 7² + 24² = 25².",
        },
    },
    {
        "question": "3️⃣ Является ли треугольник со сторонами 5, 5 и 7 прямоугольным?",
        "answer": "нет",
        "explanations": {
            "да": "❌ Ошибка. Треугольник не является прямоугольным, так как 5² + 5² ≠ 7².",
            "нет": "✅ Правильно! 5² + 5² = 50, а 7² = 49. Они не равны.",
        },
    },
    {
        "question": "4️⃣ Является ли треугольник со сторонами 8, 15 и 17 прямоугольным?",
        "answer": "да",
        "explanations": {
            "да": "✅ Молодец! 8² + 15² = 64 + 225 = 289 = 17².",
            "нет": "❌ Неправильно. Этот треугольник является прямоугольным: 8² + 15² = 17².",
        },
    },
    {
        "question": "5️⃣ Является ли треугольник со сторонами 3, 4 и 6 прямоугольным?",
        "answer": "нет",
        "explanations": {
            "да": "❌ Неверно. Треугольник не является прямоугольным, так как 3² + 4² ≠ 6².",
            "нет": "✅ Верно! 3² + 4² = 25, а 6² = 36. Поскольку 25 ≠ 36, треугольник не является прямоугольным.",
        },
    },
]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Начало работы с ботом"""
    keyboard = [["🚀 Начать тест"], ["ℹ️ О боте", "📊 Статистика"], ["❓ Помощь"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    welcome_text = (
        "👋 Привет! Я бот-учитель по теме «Обратная теорема Пифагора».\n\n"
        "📚 Я помогу тебе проверить знания о прямоугольных треугольниках!\n\n"
        "🎯 Отвечай 'да' или 'нет' на вопросы о треугольниках.\n\n"
        "Выбери действие:"
    )

    await update.message.reply_text(welcome_text, reply_markup=reply_markup)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Показать помощь"""
    help_text = (
        "📖 <b>Справка по боту</b>\n\n"
        "<b>Команды:</b>\n"
        "/start - Начать работу с ботом\n"
        "/help - Показать эту справку\n"
        "/cancel - Отменить текущий тест\n"
        "/stats - Показать статистику\n"
        "/about - О боте\n\n"
        "<b>Как пользоваться:</b>\n"
        "1. Нажми '🚀 Начать тест'\n"
        "2. Отвечай на вопросы кнопками 'да' или 'нет'\n"
        "3. Получай объяснения после каждого ответа\n"
        "4. В конце смотри свои результаты\n\n"
        "<b>Теорема Пифагора:</b>\n"
        "Треугольник является прямоугольным, если квадрат самой длинной стороны равен "
        "сумме квадратов двух других сторон: a² + b² = c²"
    )

    keyboard = [["🚀 Начать тест"], ["ℹ️ О боте", "📊 Статистика"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        help_text, reply_markup=reply_markup, parse_mode="HTML"
    )


async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """О боте"""
    about_text = (
        "ℹ️ <b>О боте</b>\n\n"
        "📐 <b>Пифагор Учитель</b>\n"
        "Образовательный бот для изучения обратной теоремы Пифагора\n\n"
        "👨‍💻 Версия: 1.0\n"
        "📅 Создан: 2025\n\n"
        "📚 <b>Обратная теорема Пифагора:</b>\n"
        "Если в треугольнике квадрат одной стороны равен сумме квадратов двух других сторон, "
        "то этот треугольник прямоугольный.\n\n"
        "🎓 Формула: a² + b² = c²\n"
        "где c - гипотенуза (самая длинная сторона)"
    )

    keyboard = [["🚀 Начать тест"], ["❓ Помощь", "📊 Статистика"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        about_text, reply_markup=reply_markup, parse_mode="HTML"
    )


async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Показать статистику"""
    if "total_tests" not in context.user_data:
        context.user_data["total_tests"] = 0
        context.user_data["total_correct"] = 0
        context.user_data["total_questions"] = 0

    total_tests = context.user_data.get("total_tests", 0)
    total_correct = context.user_data.get("total_correct", 0)
    total_questions = context.user_data.get("total_questions", 0)

    if total_tests == 0:
        stats_text = (
            "📊 <b>Твоя статистика</b>\n\n"
            "У тебя пока нет завершенных тестов.\n"
            "Пройди первый тест, чтобы увидеть статистику!"
        )
    else:
        accuracy = (total_correct / total_questions * 100) if total_questions > 0 else 0
        avg_score = total_correct / total_tests if total_tests > 0 else 0

        stats_text = (
            f"📊 <b>Твоя статистика</b>\n\n"
            f"🎯 Пройдено тестов: {total_tests}\n"
            f"✅ Правильных ответов: {total_correct} из {total_questions}\n"
            f"📈 Точность: {accuracy:.1f}%\n"
            f"⭐ Средний балл: {avg_score:.1f} из {len(QUESTIONS)}\n\n"
        )

        if accuracy >= 80:
            stats_text += "🏆 Отличный результат!"
        elif accuracy >= 60:
            stats_text += "👍 Хороший результат!"
        else:
            stats_text += "💪 Продолжай практиковаться!"

    keyboard = [
        ["🚀 Начать тест"],
        ["🔄 Сбросить статистику"],
        ["ℹ️ О боте", "❓ Помощь"],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        stats_text, reply_markup=reply_markup, parse_mode="HTML"
    )


async def reset_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Сбросить статистику"""
    keyboard = [
        [InlineKeyboardButton("✅ Да, сбросить", callback_data="reset_confirm")],
        [InlineKeyboardButton("❌ Отмена", callback_data="reset_cancel")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "⚠️ Ты уверен, что хочешь сбросить всю статистику?", reply_markup=reply_markup
    )


async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка inline кнопок"""
    query = update.callback_query
    await query.answer()

    if query.data == "reset_confirm":
        context.user_data["total_tests"] = 0
        context.user_data["total_correct"] = 0
        context.user_data["total_questions"] = 0

        keyboard = [["🚀 Начать тест"], ["ℹ️ О боте", "📊 Статистика"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

        await query.edit_message_text(
            "✅ Статистика успешно сброшена!",
        )
        await query.message.reply_text("Начни новый тест!", reply_markup=reply_markup)

    elif query.data == "reset_cancel":
        await query.edit_message_text("❌ Сброс статистики отменен.")


async def cancel_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Отменить текущий тест"""
    if "current_question" in context.user_data and context.user_data.get(
        "test_in_progress", False
    ):
        context.user_data["test_in_progress"] = False
        context.user_data["current_question"] = 0
        context.user_data["correct_answers"] = 0

        keyboard = [["🚀 Начать тест"], ["ℹ️ О боте", "📊 Статистика"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

        await update.message.reply_text(
            "❌ Тест отменен. Твой прогресс не сохранен.", reply_markup=reply_markup
        )
    else:
        await update.message.reply_text("У тебя нет активного теста.")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка сообщений пользователя"""
    text = update.message.text.lower().strip()

    # Инициализация данных пользователя
    if "current_question" not in context.user_data:
        context.user_data["current_question"] = 0
        context.user_data["correct_answers"] = 0
        context.user_data["test_in_progress"] = False

    # Обработка команд меню
    if text == "ℹ️ о боте" or text == "о боте":
        await about_command(update, context)
        return

    if text == "📊 статистика" or text == "статистика":
        await stats_command(update, context)
        return

    if text == "❓ помощь" or text == "помощь":
        await help_command(update, context)
        return

    if text == "🔄 сбросить статистику":
        await reset_stats(update, context)
        return

    if text == "❌ отменить тест":
        await cancel_command(update, context)
        return

    # Начало теста
    if text == "🚀 начать тест" or text == "начать тест":
        context.user_data["current_question"] = 0
        context.user_data["correct_answers"] = 0
        context.user_data["test_in_progress"] = True
        await send_question(update, context)
        return

    # Обработка ответа (только если тест активен)
    if text in ["да", "нет"] and context.user_data.get("test_in_progress", False):
        await process_answer(update, context)
        return

    # Переход к следующему вопросу или завершение теста
    if text == "➡️ следующий вопрос" or text == "✅ завершить тест":
        context.user_data["current_question"] += 1
        if context.user_data["current_question"] < len(QUESTIONS):
            await send_question(update, context)
        else:
            await show_results(update, context)
        return

    # Повтор теста
    if text == "🔄 пройти заново":
        context.user_data["current_question"] = 0
        context.user_data["correct_answers"] = 0
        context.user_data["test_in_progress"] = True
        await send_question(update, context)
        return

    # Если команда не распознана
    keyboard = [["🚀 Начать тест"], ["ℹ️ О боте", "📊 Статистика"], ["❓ Помощь"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "❓ Команда не распознана. Выбери действие из меню:", reply_markup=reply_markup
    )


async def send_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Отправка вопроса"""
    try:
        question_index = context.user_data["current_question"]
        question_data = QUESTIONS[question_index]

        keyboard = [["да", "нет"], ["❌ Отменить тест"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

        progress = f"Вопрос {question_index + 1} из {len(QUESTIONS)}\n\n"

        await update.message.reply_text(
            progress + question_data["question"],
            reply_markup=reply_markup,
            read_timeout=30,
            write_timeout=30,
        )
    except Exception as e:
        logger.error(f"Error sending question: {e}")
        await update.message.reply_text("Произошла ошибка. Попробуйте еще раз.")


async def process_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка ответа пользователя"""
    user_answer = update.message.text.lower().strip()

    question_index = context.user_data["current_question"]
    question_data = QUESTIONS[question_index]
    correct_answer = question_data["answer"]

    # Проверка ответа
    is_correct = user_answer == correct_answer
    if is_correct:
        context.user_data["correct_answers"] += 1

    # Отправка объяснения
    explanation = question_data["explanations"][user_answer]
    keyboard = [["➡️ Следующий вопрос"]]
    reply_markup = ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=True
    )

    await update.message.reply_text(explanation, reply_markup=reply_markup)


async def show_results(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Показать результаты теста"""
    correct = context.user_data["correct_answers"]
    total = len(QUESTIONS)

    # Обновление статистики
    if "total_tests" not in context.user_data:
        context.user_data["total_tests"] = 0
        context.user_data["total_correct"] = 0
        context.user_data["total_questions"] = 0

    context.user_data["total_tests"] += 1
    context.user_data["total_correct"] += correct
    context.user_data["total_questions"] += total
    context.user_data["test_in_progress"] = False

    # Эмодзи в зависимости от результата
    if correct == total:
        emoji = "🏆"
        message = "Отличная работа! Ты знаешь теорему Пифагора на 100%!"
    elif correct >= total * 0.8:
        emoji = "⭐"
        message = "Очень хорошо! Небольшие ошибки, но результат отличный!"
    elif correct >= total * 0.6:
        emoji = "👍"
        message = "Хороший результат! Продолжай в том же духе!"
    else:
        emoji = "📖"
        message = "Продолжай учиться! Повтори материал и попробуй снова."

    percentage = (correct / total) * 100

    keyboard = [["🔄 Пройти заново"], ["📊 Статистика", "ℹ️ О боте"], ["❓ Помощь"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    results_text = (
        f"{emoji} <b>Тест завершён!</b>\n\n"
        f"✅ Правильных ответов: {correct} из {total}\n"
        f"📊 Процент: {percentage:.0f}%\n\n"
        f"{message}"
    )

    await update.message.reply_text(
        results_text, reply_markup=reply_markup, parse_mode="HTML"
    )


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка ошибок"""
    logger.error(f"Update {update} caused error {context.error}")


def main():
    """Запуск бота"""
    # Вставьте ваш токен бота здесь
    TOKEN = "8247123854:AAHEGNy8hPPbTwk2JYR5WJx1EPE4UQObH6M"

    # Создание приложения с увеличенными таймаутами
    from telegram.request import HTTPXRequest

    request = HTTPXRequest(
        connection_pool_size=8,
        connect_timeout=30.0,
        read_timeout=30.0,
        write_timeout=30.0,
    )

    application = Application.builder().token(TOKEN).request(request).build()

    # Регистрация обработчиков команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about_command))
    application.add_handler(CommandHandler("stats", stats_command))
    application.add_handler(CommandHandler("cancel", cancel_command))

    # Обработчик callback кнопок
    application.add_handler(CallbackQueryHandler(button_callback))

    # Обработчик текстовых сообщений
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    # Обработчик ошибок
    application.add_error_handler(error_handler)

    # Запуск бота
    logger.info("Бот запущен...")
    print("🚀 Бот 'Пифагор Учитель' запущен и готов к работе!")
    print("📱 Доступные команды:")
    print("   /start - Начать работу")
    print("   /help - Помощь")
    print("   /about - О боте")
    print("   /stats - Статистика")
    print("   /cancel - Отменить тест")
    print("\nДля остановки бота нажмите Ctrl+C")

    application.run_polling(
        allowed_updates=Update.ALL_TYPES, drop_pending_updates=True, timeout=30
    )


if __name__ == "__main__":
    main()
