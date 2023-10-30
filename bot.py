from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, Application


async def hello(update: Update, context:ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Xin chao {update.effective_message.text.replace("/hello","")}')

app = Application.builder().token('6817570334:AAGNhnC3AD2VRW-eWjX5BawBiPap9sb5tlw').build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()