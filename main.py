from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import ReplyKeyboardMarkup
import time
import json
from datetime import datetime

reply_keyboard1 = [['/about_us'], ['/catalog']]
markup1 = ReplyKeyboardMarkup(reply_keyboard1, one_time_keyboard=True)

reply_keyboard2 = [['/history'], ['/creator']]
markup2 = ReplyKeyboardMarkup(reply_keyboard2, one_time_keyboard=True)


def writing_to_json(update, context):
    user = update.effective_user
    print(f'[<==] Пользователь: {user["last_name"]} {user["first_name"]}\n      ID: {user["id"]}\n      '
          f'Запрос: {update.message.text}')
    must_delete1 = update.message.reply_text(f"[*] Выполняю запрос: {update.message.text}")
    time.sleep(1)
    must_delete2 = update.message.reply_text("[*] Успешно")
    time.sleep(1)
    context.bot.deleteMessage(message_id=must_delete2.message_id,
                              chat_id=update.message.chat_id)
    context.bot.deleteMessage(message_id=must_delete1.message_id,
                              chat_id=update.message.chat_id)

    with open('query_database.json', encoding="utf8") as f:
        data = json.load(f)

    if str(user["id"]) not in data:
        data[str(user["id"])] = {}
        data[str(user["id"])]["description"] = {}
        data[str(user["id"])]["description"]["first_name"] = user["first_name"]
        data[str(user["id"])]["description"]["last_name"] = user["last_name"]
        if user["username"]:
            data[str(user["id"])]["description"]["username"] = user["username"]
        else:
            data[str(user["id"])]["description"]["username"] = None
    d = len(data[str(user["id"])])
    datenow = str(datetime.now())[:-7].split(' ')[0]
    timenow = str(datetime.now())[:-7].split(' ')[1]
    data[str(user["id"])][f"Запись {d}"] = {"дата": datenow, "время": timenow, "запрос": update.message.text}

    with open('query_database.json', 'w', encoding="utf8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


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
    writing_to_json(update, context)
    update.message.reply_markdown_v2(
        fr'Приветствую вас, {user.mention_markdown_v2()}\!',)
    text = 'Я являюсь многофункциональным чат ботом известной организации «[Faro Automated Solutions](https://' \
           'cs14.pikabu.ru/post_img/big/2022/03/08/11/1646763866139681635.jpg)»'
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаю Вам изучить мои возможности: \nВыполните запрос: /help")
    print('[==>] Ответ: Успешно')
    print()


def help(update, context):
    writing_to_json(update, context)
    update.message.reply_text('''Пожалуйста, выберете раздел, интересующий Вас:''')
    update.message.reply_text("О нашей компании - /about_us \n\nАссортимент - /catalog")
    print('[==>] Ответ: Успешно')
    print()


def about_us(update, context):
    writing_to_json(update, context)
    update.message.reply_text('''Пожалуйста, выберете раздел, интересующий Вас:''')
    update.message.reply_text("Назад - /help \n\nИстория компании - /history \n\nОснователь компании - /creator")
    print('[==>] Ответ: Успешно')
    print()


def history(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["about_us"]["history"]
    update.message.reply_text(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /about_us \n\nМои возможности - /help "
                              "\n\nЗаказать бота - /order_bot")
    print('[==>] Ответ: Успешно')
    print()


def creator(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["about_us"]["creator"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /about_us \n\nМои возможности - /help "
                              "\n\nЗаказать бота - /order_bot")
    print('[==>] Ответ: Успешно')
    print()


def catalog(update, context):
    writing_to_json(update, context)
    update.message.reply_text("Пожалуйста, выберете класс нужного бота:")
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["description"]
    update.message.reply_text(text)
    print('[==>] Ответ: Успешно')
    print()


def minerbot(update, context):
    writing_to_json(update, context)
    update.message.reply_text("Пожалуйста, выберете вид нужного бота:")
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["description"]
    update.message.reply_text(text)
    print('[==>] Ответ: Успешно')
    print()


def terraforming(update, context):
    writing_to_json(update, context)
    update.message.reply_text("Пожалуйста, выберете нужного бота:")
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["terraforming"]["description"]
    update.message.reply_text(text)
    print('[==>] Ответ: Успешно')
    print()


def runner(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["terraforming"]["runner"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /terraforming \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def bison(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["terraforming"]["bison"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /terraforming \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def combhorn(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["terraforming"]["combhorn"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /terraforming \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def archedforehead(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["terraforming"]["archedforehead"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /terraforming \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def chewinggum(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["terraforming"]["chewinggum"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /terraforming \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def stonegnawer(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["terraforming"]["stonegnawer"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /terraforming \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def ribbonhorn(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["terraforming"]["ribbonhorn"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /terraforming \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def cleaver(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["terraforming"]["cleaver"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /terraforming \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def ploughhorog(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["terraforming"]["ploughhorog"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /terraforming \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def purifiers(update, context):
    writing_to_json(update, context)
    update.message.reply_text("Пожалуйста, выберете нужного бота:")
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["purifiers"]["description"]
    update.message.reply_text(text)
    print('[==>] Ответ: Успешно')
    print()


def breakwater(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["purifiers"]["breakwater"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /purifiers \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def spearhead(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["purifiers"]["spearhead"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /purifiers \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def clicktooth(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["purifiers"]["clicktooth"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /purifiers \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def processors(update, context):
    writing_to_json(update, context)
    update.message.reply_text("Пожалуйста, выберете нужного бота:")
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["processors"]["description"]
    update.message.reply_text(text)
    print('[==>] Ответ: Успешно')
    print()


def thekite(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["processors"]["thekite"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /processors \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def trashbin(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["processors"]["trashbin"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /processors \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def scavenger(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["processors"]["scavenger"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /processors \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def poisonouslash(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["processors"]["poisonouslash"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /processors \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def overseers(update, context):
    writing_to_json(update, context)
    update.message.reply_text("Пожалуйста, выберете нужного бота:")
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["overseers"]["description"]
    update.message.reply_text(text)
    print('[==>] Ответ: Успешно')
    print()


def wedgedigger(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["overseers"]["wedgedigger"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /overseers \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def lightwing(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["overseers"]["lightwing"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /overseers \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def scoffer(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["minerbot"]["overseers"]["scoffer"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /overseers \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def transporterbot(update, context):
    writing_to_json(update, context)
    update.message.reply_text("Пожалуйста, выберете нужного бота:")
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["transporterbot"]["description"]
    update.message.reply_text(text)
    print('[==>] Ответ: Успешно')
    print()


def hippopotamus(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["transporterbot"]["hippopotamus"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /transporterbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def armorroll(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["transporterbot"]["armorroll"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /transporterbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def watersprinkler(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["transporterbot"]["watersprinkler"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /transporterbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def freezerwineskin(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["transporterbot"]["freezerwineskin"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /transporterbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def firewineskin(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["transporterbot"]["firewineskin"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /transporterbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def scarab(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["transporterbot"]["scarab"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /transporterbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def scoutbot(update, context):
    writing_to_json(update, context)
    update.message.reply_text("Пожалуйста, выберете нужного бота:")
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["scoutbot"]["description"]
    update.message.reply_text(text)
    print('[==>] Ответ: Успешно')
    print()


def longlegged(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["scoutbot"]["longlegged"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /scoutbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def holedigger(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["scoutbot"]["holedigger"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /scoutbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def scour(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["scoutbot"]["scour"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /scoutbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def redeyescour(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["scoutbot"]["redeyescour"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /scoutbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def cloudcutter(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["scoutbot"]["cloudcutter"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /scoutbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def signalbot(update, context):
    writing_to_json(update, context)
    update.message.reply_text("Пожалуйста, выберете нужного бота:")
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["signalbot"]["description"]
    update.message.reply_text(text)
    print('[==>] Ответ: Успешно')
    print()


def longnecked(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["signalbot"]["longnecked"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /signalbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def combatbot(update, context):
    writing_to_json(update, context)
    update.message.reply_text("Пожалуйста, выберете нужного бота:")
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["combatbot"]["description"]
    update.message.reply_text(text)
    print('[==>] Ответ: Успешно')
    print()


def armoredtooth(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["combatbot"]["armoredtooth"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /combatbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def stormypetrel(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["combatbot"]["stormypetrel"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /combatbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def thunderyawn(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["combatbot"]["thunderyawn"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /combatbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def beater(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["combatbot"]["beater"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /combatbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def giant(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["combatbot"]["giant"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /combatbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def icefang(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["combatbot"]["icefang"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /combatbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def likhodey(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["combatbot"]["likhodey"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /combatbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def stalker(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["combatbot"]["stalker"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /combatbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def firewolf(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["combatbot"]["firewolf"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /combatbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def firefang(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["combatbot"]["firefang"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /combatbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def sawtooth(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["combatbot"]["sawtooth"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /combatbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def fighterbot(update, context):
    writing_to_json(update, context)
    update.message.reply_text("Пожалуйста, выберете нужного бота:")
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["fighterbot"]["description"]
    update.message.reply_text(text)
    print('[==>] Ответ: Успешно')
    print()


def invader(update, context):
    writing_to_json(update, context)
    with open('base.json', encoding="utf8") as f:
        data = json.load(f)
        text = data["catalog"]["fighterbot"]["invader"]
    update.message.reply_markdown_v2(text)
    update.message.reply_text("Предлагаемые действия: \n\nНазад - /fighterbot \n\nЗаказать - /bue")
    print('[==>] Ответ: Успешно')
    print()


def fighter(update, context):
    writing_to_json(update, context)
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
