import commands.apitelebot as bot
client = bot.get_client()

@client.message_handler(commands=["desimal"])
def desimal(message):
    strangka = message.text[9:] #Split/Mengambil bilangan setelah /desimal
    try:
        convert = int(strangka)
        biner = bin(convert)
        hexa = hex(convert)
        octa = oct(convert)
        client.reply_to(message, f"Bilangan dalam Desimal: {convert}\nBilangan dalam Biner: {biner}\nBilangan dalam Hexa: {hexa}\nBilangan dalam Octa: {octa}")
    except ValueError:
        client.reply_to(message, "Mana bisa gitu goblok!")

@client.message_handler(commands=["biner"])
def binary(message):
    strangka = message.text[7:] #Split/Mengambil bilangan setelah /biner
    try:
        convert = int(strangka,2)
        hexa = hex(convert)
        octa = oct(convert)
        client.reply_to(message, f"Bilangan dalam Biner: {strangka}\nBilangan dalam Desimal: {convert}\nBilangan dalam Hexa: {hexa}\nBilangan dalam Octa: {octa}")
    except ValueError:
        client.reply_to(message, "Mana bisa gitu goblok!")

@client.message_handler(commands=["hexa"])
def hexangka(message):
    strangka = message.text[6:] #Split/Mengambil bilangan setelah /hexa
    try:
        convert = int(strangka,16)
        biner = bin(convert)
        octa = oct(convert)
        client.reply_to(message, f"Bilangan dalam Hexa: {strangka}\nBilangan dalam Desimal: {convert}\nBilangan dalam Biner: {biner}\nBilangan dalam Octa: {octa}")
    except ValueError:
        client.reply_to(message, "Mana bisa gitu goblok!")

@client.message_handler(commands=["octa"])
def octangka(message):
    strangka = message.text[6:] #Split/Mengambil bilangan setelah /octa
    try:
        convert = int(strangka,8)
        biner = bin(convert)
        hexa = hex(convert)
        client.reply_to(message, f"Bilangan dalam Octa: {strangka}\nBilangan dalam Desimal: {convert}\nBilangan dalam Biner: {biner}\nBilangan dalam Hexa: {hexa}")
    except ValueError:
        client.reply_to(message, "Mana bisa gitu goblok!")