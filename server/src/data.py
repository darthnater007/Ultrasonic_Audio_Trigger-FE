
from firebase_admin import credentials, firestore, initialize_app

def initialize_firestore():
    cred = credentials.Certificate("key.json")
    initialize_app(cred)
    return firestore.client()

def read_current_phrase(firestore_client):
    phrase_ref = firestore_client.collection(u'U_A_T').document(u'current_phrase')
    return phrase_ref.get().to_dict()

def update_phrase(firestore_client, new_phrase):
    data = {u'phrase': new_phrase,}
    try:
        firestore_client.collection(u'U_A_T').document(u'current_phrase').update(data)
        return("Success")
    except Exception as e:
        return("An error has occured: \n" + str(e))

