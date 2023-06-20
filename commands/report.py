import commands.apitelebot as bot
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
client = bot.get_client()
@client.message_handler(regexp="Report: ")
def mengontol(message):
    reportbody = message.text[8:]
    client.reply_to(message, f"Thanks For sending report:)\nYour Report: {reportbody}")
    msg = MIMEMultipart()
    message = reportbody
    # setup the parameters of the message
    password = "Your 1ST EMAIL PASS"
    msg['From'] = "your 1st email"
    msg['To'] = "Your 2nd email"
    msg['Subject'] = "Report Bug!"
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    
    #create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
    
    server.starttls()
    
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()

    