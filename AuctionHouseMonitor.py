import requests as rq
import numpy as np
import keyboard as key
import time
import yagmail as yg

NAME = # Account name
API_KEY = # API key
UUID = # UUID

with open( ) as file1:  # Wherever it is you stored the scraped list
    listNames = file1.read()[2:-2]

listNames = listNames.split("', '")

while True:
    itemName = input()

    if itemName in listNames:
        print('item found')
        break
    else:
        print('not an item')

while True:
    try:
        price = int(input())
        print('price entered')
        break

    except:
        print('enter an int')

data = rq.get(f"https://api.hypixel.net/Skyblock/auctions?key={API_KEY}&uuid={UUID}").json()
totalPages = int((data['totalPages']))
compiledPrices = []
name = []
loopNum = 0

while True:
    for page in range(totalPages):

        if key.is_pressed('q'):
            exit()

        tempData = rq.get(f"https://api.hypixel.net/Skyblock/auctions?key={API_KEY}&page={page}").json()

        for i in range(len(tempData['auctions'])):
            try:
                if (itemName in tempData['auctions'][i]['item_name']) and (tempData['auctions'][i]['bin']):
                    compiledPrices.append(int(tempData['auctions'][i]['starting_bid']))
                    name.append(tempData['auctions'][i]['auctioneer'])
            except:
                pass

    npCompiled = np.array(compiledPrices)
    metBudget = np.where(npCompiled <= price)[0]

    if len(metBudget) > 0:
        body = ""

        for i in metBudget:
            tempData2 = rq.get(f"https://api.mojang.com/user/profiles/{name[i]}/names").json()

            body += f"{tempData2[-1]['name']} is selling at: {str(npCompiled[i])} coins, "

        try:
            yag = yg.SMTP(user= , password=)  # gmail address (sender) and password
            yag.send(
                to= ,  # gmail address (recipient)
                subject='GO AUCTION HOUSE',
                contents=f'{itemName} available in BIN: {body}.'
            )
            print('success, email sent')
        except:
            print('error email not sent')

    loopNum += 1
    print(loopNum)

    for i in range(180):
        if key.is_pressed('q'):
            exit()

        time.sleep(1)
