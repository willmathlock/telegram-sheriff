from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from threading import Timer

from conf.settings import BASE_API_URL, TELEGRAM_TOKEN

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
        #animation = 'https://pa1.narvii.com/7136/475c22b4cb2315dcdf910c54e3a8d38d2bb93cfbr1-220-166_hq.gif'
        animation = open(arq, 'rb')
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
    t = Timer(0.5, 
        mandaGif(bot, update, 'machista')
    )
    t.start()
    

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
        MessageHandler(Filters.command, unknown)
    )
    

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()