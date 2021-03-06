import requests
import json
from  Models.CurrencyBase import CurrencyBase
from Models.BankModel import BankModel

from bs4 import BeautifulSoup
# Create your views here.



def returnBank():
    rs = requests.get("https://kur.doviz.com/serbest-piyasa/euro")
    bs = BeautifulSoup(rs.content, 'html.parser')

    tables = bs.find_all('table')
    changeRates = list()
    bankValues = list()

    changeTable = tables[0]
    cells = (changeTable.find('tbody')).find_all('td')
    title = ["","Günlük Değişim","Haftalık Değişim","Yıllık Değişim"]
    for i in range(1,4):
        ob = CurrencyBase(title[i], cells[i].get_text(),cells[i].get_attribute_list('class')[0].split('-')[1])
        changeRates.append(ob)

    bankTable = tables[1]

    lines = bankTable.find_all('tr')

    for line in lines:
        cells = line.find_all('td')
        if len(cells) < 1 :
            continue

        ob = BankModel((cells[0].find('a')).get_text(),cells[1].get_text().replace(",","."),cells[2].get_text().replace(",","."))
        bankValues.append(ob)

    bankTable = tables[2]

    lines = bankTable.find_all('tr')

    for line in lines:
        cells = line.find_all('td')
        if len(cells) < 1:
            continue

        ob = BankModel((cells[0].find('a')).get_text(), cells[1].get_text().replace(",","."), cells[2].get_text().replace(",","."))
        bankValues.append(ob)

    currencyName = bs.find('div', {'class': 'kur-title'}).find('span', {'class': 'left'}).get_text()
    currencyValues = bs.find('div', {'class': 'data'}).find_all('span', {'class': 'value'})

    currencyBuy = currencyValues[0].get_text()
    currencySell = currencyValues[0].get_text()

    return changeRates,bankValues,{'name':currencyName,'sell':currencySell.replace(",","."),'buy':currencyBuy.replace(",",".")}


def run():
    changeList, bankList, generalInfo = returnBank()
    changeRates = list()
    bankValues = list()

    for ob in changeList:
        ls = {}
        ls['name'] = ob.name
        ls['value'] = ob.value
        ls['type'] = ob.type
        changeRates.append(ls)

    for ob in bankList:
        ls = {}
        ls['bankName'] = ob.bankName
        ls['buy'] = ob.buy
        ls['sell'] = ob.sell
        bankValues.append(ls)

    return [changeRates,bankValues,generalInfo]







