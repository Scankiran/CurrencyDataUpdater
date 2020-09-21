# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from Currencies import Euro,Gbp,Usd,GeneralData
import time
import schedule
import datetime
import json



credp = credentials.Certificate(
        '/Users/saidcankiran/Documents/currencyapi-56147-firebase-adminsdk-737nm-fb12f06859.json')
firebase_admin.initialize_app(credp)
db = firestore.client()


def writeDataToFirebase(dataType,type,data):
    current_time = datetime.datetime.now()


    doc_ref = db.collection(dataType).document(type)
    doc_ref.set({
        'last': data,
        'updateTime':current_time
    })
    print(current_time)

def writeDataToFirebasee(dataType,type,data):
    current_time = datetime.datetime.now()


    doc_ref = db.collection(dataType).document(type)
    doc_ref.set({
        'changeRate': json.dumps(data[0],ensure_ascii=False),
        'banks':json.dumps(data[1],ensure_ascii=False),
        'generalInfo':data[2],
        'updateTime':current_time
    })
    print(current_time)




def run():
    for i in range(0,10):
        writeDataToFirebasee('euro','last', Euro.run())
        writeDataToFirebasee('usd','last', Usd.run())
        writeDataToFirebasee('gbp','last', Gbp.run())
        writeDataToFirebase('general','summary',GeneralData.run(False))
        writeDataToFirebase('general','all', GeneralData.run(True))
        print("runoldu")
        time.sleep(60)



      # Press ⌘F8 to toggle the breakpoint.

while True:
    run()
    time.sleep(1)

