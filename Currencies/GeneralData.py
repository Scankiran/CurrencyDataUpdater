import requests
from  Models.CurrencyBase import CurrencyBase
from Models.CurrencyDetail import CurrencyDetailModel

from bs4 import BeautifulSoup
import json

def summary_general_currency_data_scrapy():
    rs = requests.get("https://kur.doviz.com")
    bs = BeautifulSoup(rs.content,'html.parser')
    objects = []
    table = bs.find_all('div',attrs={'class':'market-data'})[0]

    cells = table.find_all('div',attrs={'class':'item'})

    for cell in cells:
        up = cell.find_all('span')
        name = up[0].get_text()
        value = up[1].get_text()

        down = cell.find('div')
        type = down.get_attribute_list('class')

        object = CurrencyBase(name,value,type[1])
        objects.append(object)

    return objects





def general_currency_data_scrapy():
    rs = requests.get("https://kur.doviz.com")
    bs = BeautifulSoup(rs.content,'html.parser')

    tables = bs.find_all('table',attrs={'id':'currencies'})

    currencyTable = tables[0]

    table = currencyTable.find('tbody')

    lines = table.find_all('tr')
    objects = []
    for line in lines:

        cells = line.find_all('td')
        if len(cells) < 7:
            continue

        name = line.get_attribute_list('data-table-subpage-key')[0]
        ob = CurrencyDetailModel(name,cells[1].get_text(),cells[2].get_text(),cells[3].get_text(),cells[4].get_text(),cells[5].get_attribute_list('class')[1].split('-')[1])
        objects.append(ob)

    return objects

def run(sendDetailed):
    objects = summary_general_currency_data_scrapy()
    allObjects = general_currency_data_scrapy()
    summary = list()
    all = list()

    for ob in objects:
        ls = {}
        ls['name'] = ob.name
        ls['value'] = ob.value
        ls['type'] = ob.type
        summary.append(ls)

    for ob in allObjects:
        ls = {}
        ls['name'] = ob.name
        ls['buy'] = ob.buy
        ls['sell'] = ob.sell
        ls['min'] = ob.min
        ls['max'] = ob.max
        ls['type'] = ob.type
        all.append(ls)

    if sendDetailed:
        return json.dumps(all, ensure_ascii=False)
    else:
        return json.dumps(summary, ensure_ascii=False)

