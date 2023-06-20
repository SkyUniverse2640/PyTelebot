import commands.apitelebot as bot
client = bot.get_client()

@client.message_handler(commands=["celcius"])
def celcius(message):
    strangka = message.text[9:] # membuang /konvert
    try:
        convert = int(strangka)
        c = convert #celcius
        r = (4/5)*convert #reamur
        f = ((9/5)* convert)+ 32 #fahrenheit
        k = convert + 273.15 #kelvin
        client.reply_to(message, "suhu dalam celcius: " + str(c) + "\nsuhu dalam reamur: "+ str(r) + "\nsuhu dalam fahrenheit: "+ str(f) + "\nsuhu dalam kelvin: "+ str(k)) #Send message kepada pengguna
    except ValueError:
        client.reply_to(message, "Mana bisa gitu goblok!")
    
'''@client.message_handler(commands=["reamur"])
def celcius(message):
    strangka = message.text.split() #Mengambil input angka
    bot.deletestr(strangka) # membuang /konvert
    floatangka = list(float(xyz)for xyz in strangka)#membuat list string berubah menjadi float
    convert = np.asarray(floatangka) #Menkonvert float menjadi string kembali
    r = convert #celcius
    c = (4/5)*convert #reamur
    f = ((9/5)* convert)+ 32 #fahrenheit
    k = convert + 273.15 #kelvin
    client.reply_to(message, "suhu dalam reamur: " + str(r) + "\nsuhu dalam celcius: "+ str(c) + "\nsuhu dalam fahrenheit: "+ str(f) + "\nsuhu dalam kelvin: "+ str(k)) #Send message kepada pengguna
    return

@client.message_handler(commands=["celcius"])
def celcius(message):
    strangka = message.text.split() #Mengambil input angka
    bot.deletestr(strangka) # membuang /konvert
    floatangka = list(float(xyz)for xyz in strangka)#membuat list string berubah menjadi float
    convert = np.asarray(floatangka) #Menkonvert float menjadi string kembali
    c = convert #celcius
    r = (4/5)*convert #reamur
    f = ((9/5)* convert)+ 32 #fahrenheit
    k = convert + 273.15 #kelvin
    client.reply_to(message, "suhu dalam celcius: " + str(c) + "\nsuhu dalam reamur: "+ str(r) + "\nsuhu dalam fahrenheit: "+ str(f) + "\nsuhu dalam kelvin: "+ str(k)) #Send message kepada pengguna
    return
@client.message_handler(commands=["celcius"])
def celcius(message):
    strangka = message.text.split() #Mengambil input angka
    bot.deletestr(strangka) # membuang /konvert
    floatangka = list(float(xyz)for xyz in strangka)#membuat list string berubah menjadi float
    convert = np.asarray(floatangka) #Menkonvert float menjadi string kembali
    c = convert #celcius
    r = (4/5)*convert #reamur
    f = ((9/5)* convert)+ 32 #fahrenheit
    k = convert + 273.15 #kelvin
    client.reply_to(message, "suhu dalam celcius: " + str(c) + "\nsuhu dalam reamur: "+ str(r) + "\nsuhu dalam fahrenheit: "+ str(f) + "\nsuhu dalam kelvin: "+ str(k)) #Send message kepada pengguna
    return'''