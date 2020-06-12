from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from threading import Timer

from conf.settings import BASE_API_URL, TELEGRAM_TOKEN
from conf.emoji import turtle_emoji
from conf.cotacao import busca_cotacao

def tocaAudio(bot, update, name):
    arq = "conf/audios/" + name + ".mp3"

    bot.send_audio(
        chat_id = update.message.chat_id,
        audio = open(arq, 'rb')
    )

def mandaGif(bot, update, name):
    arq = "conf/img/" + name + ".gif"
    bot.sendAnimation(
        chat_id = update.message.chat_id,
        animation = open(arq, 'rb')
    )

def mandaImg(bot, update, name):
    arq = "conf/img" + name + ".png"
    bot.sendPhoto(
        chat_id = update.message.chat_id,
        photo = open(arq, 'rb')
    )

def bfa(bot, update):
    response_message = "ACABA LOGO BFA!"
    bot.send_message(
        chat_id = update.message.chat_id,
        text = response_message
    )

def unknown(bot, update):
    response_message = "Meow? =^._.^="
    bot.send_message(
        chat_id = update.message.chat_id,
        text = response_message
    )

def amanha(bot, update):
    tocaAudio(bot, update, 'amanha')

def pedra(bot, update):
    tocaAudio(bot, update, 'caralhovamosfazerpedra')

def fodo(bot, update):
    tocaAudio(bot, update, 'fodo')

def olha(bot, update):
    tocaAudio(bot, update, 'olha')

def oralzinho(bot, update):
    tocaAudio(bot, update, 'oralziniho')

def machista(bot, update):
    tocaAudio(bot, update, 'machista')
    mandaGif(bot, update, 'machista')

def milagre(bot, update):
    tocaAudio(bot, update, 'milagre')
    mandaGif(bot, update, 'milagre')

def tururu(bot, update):
    tocaAudio(bot, update, 'tururu')

def cotacao(bot, update):
    bot.send_message(
        chat_id = update.message.chat_id,
        text = busca_cotacao()
    )

def skidaddle(bot, update):
    tocaAudio(bot, update, 'skidaddle')
    mandaGif(bot, update, 'skidaddle')

def tosco(bot, update):
    tocaAudio(bot, update, 'tosco')

def turtle(bot, update):
    tocaAudio(bot, update, 'turtle')
    bot.send_message(
        chat_id = update.message.chat_id,
        text = turtle_emoji()
    )

def main():
    updater = Updater(token=TELEGRAM_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        CommandHandler('amanha', amanha)
    )
    dispatcher.add_handler(
        CommandHandler('pedra', pedra)
    )
    dispatcher.add_handler(
        CommandHandler('cotacao', cotacao)
    )
    dispatcher.add_handler(
        CommandHandler('fodo', fodo)
    )
    dispatcher.add_handler(
        CommandHandler('olha', olha)
    )
    dispatcher.add_handler(
        CommandHandler('oralzinho', oralzinho)
    )
    dispatcher.add_handler(
        CommandHandler('machista', machista)
    )
    dispatcher.add_handler(
        CommandHandler('milagre', milagre)
    )
    dispatcher.add_handler(
        CommandHandler('tururu', tururu)
    )
    dispatcher.add_handler(
        CommandHandler('tosco', tosco)
    )
    dispatcher.add_handler(
        CommandHandler('turtle', turtle)
    )
    dispatcher.add_handler(
        CommandHandler('skidaddle', skidaddle)
    )


    dispatcher.add_handler(
        MessageHandler(Filters.command, unknown)
    )
    

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()