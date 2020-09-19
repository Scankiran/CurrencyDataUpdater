# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from Currencies import Euro,Gbp,Usd,GeneralData
import time
import datetime

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# def addDataSample():
#
#     # Use a service account
#     cred = credentials.Certificate('/Users/saidcankiran/Documents/currencyapi-56147-firebase-adminsdk-737nm-fb12f06859.json')
#     firebase_admin.initialize_app(cred)
#
#     db = firestore.client()
#
#     doc_ref = db.collection('users').document('alovelace')
#     doc_ref.set({
#         'fi2rst': 'Ad2a',
#         'l22ast': 'Love2lace',
#         'b2orn': 1815
#     })


# Press the green button in the gutter to run the script.


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


if __name__ == '__main__':
    print_hi('PyCharm')
    count = 0

    for i in range(0,10):
        writeDataToFirebase('euro','last', Euro.run())
        writeDataToFirebase('usd','last', Usd.run())
        writeDataToFirebase('gbp','last', Gbp.run())
        writeDataToFirebase('general','summary',GeneralData.run(False))
        writeDataToFirebase('general','all', GeneralData.run(True))
        print("runoldu")
        time.sleep(10)







