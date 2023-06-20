from bs4.element import NavigableString, Stylesheet
import commands.apitelebot as bot
client = bot.get_client()
from requests import get
from bs4 import BeautifulSoup as BS

@client.message_handler(commands=["covid19"])
def covid(message):
    try:
        take = BS(get('https://covid19.go.id').content, 'html.parser')
        dapat = take.find('div', class_='col-md-3 text-color-black p-4', style='background-color: rgb(234, 104, 82);').text
        client.reply_to(message, f"DATA REALTIME INFORMASI COVID19 {dapat}")
    except:
        print("Unknown Error!")