from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import ReplyKeyboardMarkup
import time
import json

reply_keyboard1 = [['/about_us'], ['/catalog']]
markup1 = ReplyKeyboardMarkup(reply_keyboard1, one_time_keyboard=True)

reply_keyboard2 = [['/history'], ['/creator']]
markup2 = ReplyKeyboardMarkup(reply_keyboard2, one_time_keyboard=True)


def echo(update, context):
    update.message.reply_text('Я получил сообщение ' + update.message.text)


def main():
    updater = Updater("5182532740:AAFDNs0THbKIIom_ASW3fFUK-kjs8kwd-Ko", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(CommandHandler("about_us", about_us))
    dp.add_handler(CommandHandler("history", history))
    dp.add_handler(CommandHandler("creator", creator))
    dp.add_handler(CommandHandler("catalog", catalog))

    dp.add_handler(CommandHandler("minerbot", minerbot))
    dp.add_handler(CommandHandler("terraforming", terraforming))
    dp.add_handler(CommandHandler("runner", runner))
    dp.add_handler(CommandHandler("bison", bison))
    dp.add_handler(CommandHandler("combhorn", combhorn))
    dp.add_handler(CommandHandler("archedforehead", archedforehead))
    dp.add_handler(CommandHandler("chewinggum", chewinggum))
    dp.add_handler(CommandHandler("stonegnawer", stonegnawer))
    dp.add_handler(CommandHandler("cleaver", cleaver))
    dp.add_handler(CommandHandler("ploughhorog", ploughhorog))
    dp.add_handler(CommandHandler("ribbonhorn", ribbonhorn))

    dp.add_handler(CommandHandler("purifiers", purifiers))
    dp.add_handler(CommandHandler("breakwater", breakwater))
    dp.add_handler(CommandHandler("spearhead", spearhead))
    dp.add_handler(CommandHandler("clicktooth", clicktooth))

    dp.add_handler(CommandHandler("processors", processors))
    dp.add_handler(CommandHandler("thekite", thekite))
    dp.add_handler(CommandHandler("poisonouslash",poisonouslash))
    dp.add_handler(CommandHandler("scavenger", scavenger))
    dp.add_handler(CommandHandler("trashbin", trashbin))

    dp.add_handler(CommandHandler("overseers", overseers))
    dp.add_handler(CommandHandler("wedgedigger", wedgedigger))
    dp.add_handler(CommandHandler("lightwing", lightwing))
    dp.add_handler(CommandHandler("scoffer", scoffer))

    dp.add_handler(CommandHandler("transporterbot", transporterbot))
    dp.add_handler(CommandHandler("hippopotamus", hippopotamus))
    dp.add_handler(CommandHandler("armorroll", armorroll))
    dp.add_handler(CommandHandler("watersprinkler", watersprinkler))
    dp.add_handler(CommandHandler("freezerwineskin", freezerwineskin))
    dp.add_handler(CommandHandler("firewineskin", firewineskin))
    dp.add_handler(CommandHandler("scarab", scarab))

    dp.add_handler(CommandHandler("scoutbot", scoutbot))
    dp.add_handler(CommandHandler("longlegged", longlegged))
    dp.add_handler(CommandHandler("holedigger", holedigger))
    dp.add_handler(CommandHandler("scour", scour))
    dp.add_handler(CommandHandler("redeyescour", redeyescour))
    dp.add_handler(CommandHandler("cloudcutter", cloudcutter))

    dp.add_handler(CommandHandler("signalbot", signalbot))
    dp.add_handler(CommandHandler("longnecked", longnecked))

    dp.add_handler(CommandHandler("combatbot", combatbot))
    dp.add_handler(CommandHandler("armoredtooth", armoredtooth))
    dp.add_handler(CommandHandler("thunderyawn", thunderyawn))
    dp.add_handler(CommandHandler("beater", beater))
    dp.add_handler(CommandHandler("giant", giant))
    dp.add_handler(CommandHandler("icefang", icefang))
    dp.add_handler(CommandHandler("likhodey", likhodey))
    dp.add_handler(CommandHandler("stalker", stalker))
    dp.add_handler(CommandHandler("firewolf", firewolf))
    dp.add_handler(CommandHandler("firefang", firefang))
    dp.add_handler(CommandHandler("sawtooth", sawtooth))
    dp.add_handler(CommandHandler("stormypetrel", stormypetrel))

    dp.add_handler(CommandHandler("fighterbot", fighterbot))
    dp.add_handler(CommandHandler("invader", invader))
    dp.add_handler(CommandHandler("fighter", fighter))

    text_handler = MessageHandler(Filters.text & ~Filters.command, echo)
    dp.add_handler(text_handler)
    updater.start_polling()
    updater.idle()


def start(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /start")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    update.message.reply_markdown_v2(
        fr'Приветствую вас, {user.mention_markdown_v2()}\!',)
    text = 'Я являюсь многофункциональным чат ботом известной организации «[Faro Automated Solutions](https://' \
           'cs14.pikabu.ru/post_img/big/2022/03/08/11/1646763866139681635.jpg)»'
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаю Вам изучить мои возможности: \nВыполните запрос: /help")
    print('[==>] Ответ: Успешно')
    print()


def help(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /help")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    update.message.reply_text('''Пожалуйста, выберете раздел, интересующий Вас:''')
    update.message.reply_text("О нашей компании - /about_us \n\nАссортимент - /catalog")
    print('[==>] Ответ: Успешно')
    print()


def about_us(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /about_us")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    update.message.reply_text('''Пожалуйста, выберете раздел, интересующий Вас:''')
    update.message.reply_text("Назад - /help \n\nИстория компании - /history \n\nОснователь компании - /creator")
    print('[==>] Ответ: Успешно')
    print()


def history(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /history")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["about_us"]["history"]
    update.message.reply_text(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /about_us \n\nМои возможности - /help "
                              "\n\nЗаказать бота - /order_bot")
    print('[==>] Ответ: Успешно')
    print()


def creator(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /creator")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["about_us"]["creator"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /about_us \n\nМои возможности - /help "
                              "\n\nЗаказать бота - /order_bot")
    print('[==>] Ответ: Успешно')
    print()


def catalog(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /catalog")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    update.message.reply_text("Пожалуйста, выберете класс нужного бота:")
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["description"]
    update.message.reply_text(text)
    print('[==>] Ответ: Успешно')
    print()


def minerbot(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /minerbot")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    update.message.reply_text("Пожалуйста, выберете вид нужного бота:")
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["description"]
    update.message.reply_text(text)
    print('[==>] Ответ: Успешно')
    print()


def terraforming(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /terraforming")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    update.message.reply_text("Пожалуйста, выберете нужного бота:")
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["terraforming"]["description"]
    update.message.reply_text(text)
    print('[==>] Ответ: Успешно')
    print()


def runner(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /runner")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["terraforming"]["runner"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /terraforming \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def bison(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /bison")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["terraforming"]["bison"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /terraforming \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def combhorn(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /combhorn")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["terraforming"]["combhorn"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /terraforming \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def archedforehead(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /archedforehead")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["terraforming"]["archedforehead"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /terraforming \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def chewinggum(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /chewinggum")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["terraforming"]["chewinggum"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /terraforming \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def stonegnawer(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /stonegnawer")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["terraforming"]["stonegnawer"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /terraforming \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def ribbonhorn(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /ribbonhorn")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["terraforming"]["ribbonhorn"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /terraforming \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def cleaver(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /cleaver")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["terraforming"]["cleaver"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /terraforming \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def ploughhorog(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /ploughhorog")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["terraforming"]["ploughhorog"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /terraforming \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def purifiers(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /purifiers")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    update.message.reply_text("Пожалуйста, выберете нужного бота:")
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["purifiers"]["description"]
    update.message.reply_text(text)
    print('[==>] Ответ: Успешно')
    print()


def breakwater(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /breakwater")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["purifiers"]["breakwater"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /purifiers \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def spearhead(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /spearhead")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["purifiers"]["spearhead"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /purifiers \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def clicktooth(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /clicktooth")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["purifiers"]["clicktooth"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /purifiers \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def processors(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /processors")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    update.message.reply_text("Пожалуйста, выберете нужного бота:")
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["processors"]["description"]
    update.message.reply_text(text)
    print('[==>] Ответ: Успешно')
    print()


def thekite(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /thekite")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["processors"]["thekite"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /processors \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def trashbin(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /trashbin")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["processors"]["trashbin"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /processors \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def scavenger(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /scavenger")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["processors"]["scavenger"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /processors \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def poisonouslash(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /poisonouslash")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["processors"]["poisonouslash"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /processors \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def overseers(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /overseers")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    update.message.reply_text("Пожалуйста, выберете нужного бота:")
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["overseers"]["description"]
    update.message.reply_text(text)
    print('[==>] Ответ: Успешно')
    print()


def wedgedigger(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /wedgedigger")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["overseers"]["wedgedigger"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /overseers \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def lightwing(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /lightwing")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["overseers"]["lightwing"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /overseers \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def scoffer(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /scoffer")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["overseers"]["scoffer"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /overseers \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def transporterbot(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /transporterbot")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    update.message.reply_text("Пожалуйста, выберете нужного бота:")
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["transporterbot"]["description"]
    update.message.reply_text(text)
    print('[==>] Ответ: Успешно')
    print()


def hippopotamus(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /hippopotamus")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["transporterbot"]["hippopotamus"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /transporterbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def armorroll(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /armorroll")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["transporterbot"]["armorroll"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /transporterbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def watersprinkler(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /watersprinkler")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["transporterbot"]["watersprinkler"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /transporterbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def freezerwineskin(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /freezerwineskin")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["transporterbot"]["freezerwineskin"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /transporterbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def firewineskin(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /firewineskin")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["transporterbot"]["firewineskin"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /transporterbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def scarab(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /scarab")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["transporterbot"]["scarab"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /transporterbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def scoutbot(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /scoutbot")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    update.message.reply_text("Пожалуйста, выберете нужного бота:")
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["scoutbot"]["description"]
    update.message.reply_text(text)
    print('[==>] Ответ: Успешно')
    print()


def longlegged(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /longlegged")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["scoutbot"]["longlegged"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /scoutbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def holedigger(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /holedigger")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["scoutbot"]["holedigger"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /scoutbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def scour(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /scour")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["scoutbot"]["scour"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /scoutbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def redeyescour(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /redeyescour")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["scoutbot"]["redeyescour"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /scoutbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def cloudcutter(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /cloudcutter")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["scoutbot"]["cloudcutter"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /scoutbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def signalbot(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /signalbot")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    update.message.reply_text("Пожалуйста, выберете нужного бота:")
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["signalbot"]["description"]
    update.message.reply_text(text)
    print('[==>] Ответ: Успешно')
    print()


def longnecked(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /longnecked")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["signalbot"]["longnecked"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /signalbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def combatbot(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /combatbot")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    update.message.reply_text("Пожалуйста, выберете нужного бота:")
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["combatbot"]["description"]
    update.message.reply_text(text)
    print('[==>] Ответ: Успешно')
    print()


def armoredtooth(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /armoredtooth")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["combatbot"]["armoredtooth"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /combatbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def stormypetrel(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /stormypetrel")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["combatbot"]["stormypetrel"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /combatbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def thunderyawn(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /thunderyawn")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["combatbot"]["thunderyawn"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /combatbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def beater(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /beater")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["combatbot"]["beater"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /combatbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def giant(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /giant")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["combatbot"]["giant"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /combatbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def icefang(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /icefang")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["combatbot"]["icefang"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /combatbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def likhodey(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /likhodey")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["combatbot"]["likhodey"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /combatbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def stalker(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /stalker")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["combatbot"]["stalker"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /combatbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def firewolf(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /firewolf")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["combatbot"]["firewolf"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /combatbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def firefang(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /firefang")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["combatbot"]["firefang"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /combatbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def sawtooth(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /sawtooth")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["combatbot"]["sawtooth"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /combatbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def fighterbot(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /fighterbot")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    update.message.reply_text("Пожалуйста, выберете нужного бота:")
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["fighterbot"]["description"]
    update.message.reply_text(text)
    print('[==>] Ответ: Успешно')
    print()


def invader(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /invader")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["fighterbot"]["invader"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /fighterbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def fighter(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text("[*] Выполняю запрос: /fighter")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["fighterbot"]["fighter"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /fighterbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


if __name__ == '__main__':
    print('[*] Connection is True.')
    print('')
    main()
