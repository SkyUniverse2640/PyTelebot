######################### Module #########################
import commands.apitelebot as bot
import random
import commands.tempratur
import commands.binary
import commands.report
import commands.scrap
######################### Module #########################


##### Calling Client And FN(FileName) On apitelebot #####
client = bot.get_client()
fn = bot.get_fn()
##### Calling Client And FN(FileName) On apitelebot #####


############ COMMANDS ############
@client.message_handler(commands=["start"])
def mulai(message):
    client.reply_to(message, fn["start"])

@client.message_handler(commands=["help"])
def bantuan(message):
    client.reply_to(message, fn["help"])

@client.message_handler(commands=["howgay"])
def gay(message):
    msg = message.text
    jum = len(msg)
    if jum < 8:
        client.reply_to(message, "Please Input The Username!")
    else:
        target = msg.split(" ")[1] #split jadi ["/howgay", "name"] ambil name
        client.reply_to(message, f"{target} are {random.randint(0, 100)}% gay! ")

@client.message_handler(commands=["kerangajaib"])
def ajaib(message):
    msg = message.text
    jum = len(msg)
    if jum < 13:
        client.reply_to(message, "Please Input The Question!")
    else:
        target = msg.split(" ")[1]
        answer = random.choice(fn["jawab"])
        client.reply_to(message, f"Your Question: {target} \nAnswer: " + answer)

@client.message_handler(commands=["repeat"])
def repeat(message):
    msg = message.text
    jum = len(msg)
    if jum < 8:
        client.reply_to(message, "Hey? Please input the text! and i will repeat it!")
    else:
        if msg[8:jum].lower() in fn["wow"]:
            print(message)
            client.reply_to(message, "Yeah We Know That!")
        else:
            client.reply_to(message, msg[8:jum])

@client.message_handler(commands=["infobot"])
def info(message):
    client.reply_to(message, "===SkyUniverse Bot===\nCreated on: 23 February 2021\nOwner: " + fn["Owner"] + "\nYoutube: https://www.youtube.com/channel/UC97FDydAqWcRUAxdK3qEcsQ\nInstagram: https://www.instagram.com/ini.nanze\n===SkyUniverse Bot===")

@client.message_handler(commands=["reportbug"])
def reporting(message):
    client.send_message(message.chat.id, "To send report bug to developer. You can send message with format:\nReport: <space> <text>\nExample:\n\nReport: Mengkeren:V")

@client.message_handler(commands=["mtkfitur"])
def mtk(message):
    client.send_message(message.chat.id, "Math feature avaible: /celcius <integer>\n/reamur(Under develoment)\n/fahrenheit(under development)\n/kelvin(under development)\n\n\n/biner (biner)\n/desimal (desimal)\n/hexa (hexa)\n/octa (octa)")
############ COMMANDS ############



print("Bot ready!")
client.polling()