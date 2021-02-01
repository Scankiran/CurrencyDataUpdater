# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys,os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from Currencies import Euro,Gbp,Usd,GeneralData,Gold
import time
import sched
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





print(sys.getrecursionlimit())
sys.setrecursionlimit(10000)
print(sys.getrecursionlimit())
s = sched.scheduler(time.time,time.sleep)

def run(sc):
    writeDataToFirebasee('euro','last', Euro.run())
    writeDataToFirebasee('usd','last', Usd.run())
    writeDataToFirebasee('gbp','last', Gbp.run())
    writeDataToFirebasee('gold','last',Gold.run())
    writeDataToFirebase('general','summary',GeneralData.run(False))
    writeDataToFirebase('general','all', GeneralData.run(True))

    print("runoldu")
    s.enter(60,1,run,(sc,))
    s.run()

try:
    run(s)
except:
    os.system("python3 main.py")
      # Press ⌘F8 to toggle the breakpoint.
#saidler

