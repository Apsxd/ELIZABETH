import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from Elizabeth import dispatcher
from Elizabeth.modules.disable import DisableAbleCommandHandler
 
TR_STRINGS = (
      "Bu dünyada götürülecek hiçbir şey yok ... sadece aşk ve arkadaşlıktan vazgeçilecek😉😉🙃.Bu dünyada götürülecek hiçbir şey yok ... sadece aşk ve arkadaşlıktan vazgeçilecek😉😉🙃",
      "Bazı insanlar en sevilen olduğumuzu düşünse de ...... aşkımızın başkaları için olduğunu anlasınlar, bizi arayın .... çok üzücü ................ sonsuza kadar ...... .... Ep ",
      )
@run_async
def q(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(TR_STRINGS))
    else:
      message.reply_text(random.choice(TR_STRINGS))
 
__help__ = """
- /qt"""
__mod_name__ = "T- Quotes"
 
Q_HANDLER = DisableAbleCommandHandler("qt", qt)
 
dispatcher.add_handler(Q_HANDLER)
