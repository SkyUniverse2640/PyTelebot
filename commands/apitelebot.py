import telebot, json

def get_fn()->json: #Membuka file data.json 
    return json.loads(open("commands/dbjson/data.json").read())
fn = get_fn()


client = telebot.TeleBot(fn["token"]) #Membuat token api

def get_client()->client: #Client = New Client
    return client