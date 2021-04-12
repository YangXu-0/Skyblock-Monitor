import requests as rq
from bs4 import BeautifulSoup as bs

pageParams = ['', '?from=Farming+Island', '?from=Savanna+Bow'] # Not dynamic since the wiki is very messy

itemList = []
categories = []

for page in range(len(pageParams)):
    data = rq.get(f'https://hypixel-skyblock.fandom.com/wiki/Category:Items{pageParams[page]}')
    soupedData = bs(data.content, 'html.parser')
    preItems = soupedData.find_all('a')

    for i in range(len(preItems)):
        try:
            if 'Category' in preItems[i]['title']:
                categories.append(preItems[i]['title'])
            elif 'Add new page' not in preItems[i]['title']:
                if preItems[i]['title'] not in itemList:
                    itemList.append(preItems[i]['title'])

        except:
            pass

with open('itemlist.txt', 'w') as file1:
    file1.write(str(itemList))
