from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from threading import Timer

from conf.settings import BASE_API_URL, TELEGRAM_TOKEN

def tocaAudio(bot, update, file):
    arq = 'conf/audios' + file
    bot.send_audio()

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
    bot.send_audio(
        chat_id = update.message.chat_id,
        audio = open('conf/audios/amanha.mp3', 'rb')
    )

def pedra(bot, update):
    bot.send_audio(
        chat_id = update.message.chat_id,
        audio = open('conf/audios/caralhovamosfazerpedra.mp3', 'rb')
    )

def fodo(bot, update):
    bot.send_audio(
        chat_id = update.message.chat_id,
        audio = open('conf/audios/fodo.mp3', 'rb')
    )

def olha(bot, update):
    bot.send_audio(
        chat_id = update.message.chat_id,
        audio = open('conf/audios/olha.mp3', 'rb')
    )

def oralzinho(bot, update):
    bot.send_audio(
        chat_id = update.message.chat_id,
        audio = open('conf/audios/oralzinho.mp3', 'rb')   
    )

def machista(bot, update):
    bot.send_audio(
        chat_id = update.message.chat_id,
        audio = open('conf/audios/machista.mp3', 'rb'), 
    )
    t = Timer(0.5, 
        bot.sendAnimation(
        chat_id = update.message.chat_id,
        #animation = 'https://pa1.narvii.com/7136/475c22b4cb2315dcdf910c54e3a8d38d2bb93cfbr1-220-166_hq.gif'
        animation = open('conf/img/machista.gif', 'rb')
    ))
    t.start()
    

def main():
    updater = Updater(token=TELEGRAM_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        CommandHandler('start', start)
    )
    dispatcher.add_handler(
        CommandHandler('http', http_cats, pass_args=True)
    )
    dispatcher.add_handler(
        CommandHandler('bfa', bfa)
    )
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