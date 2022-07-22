# K Opong-Mensah


import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from brcdlib import read_imei

databaseURL = 'https://brcdfb-300dc-default-rtdb.firebaseio.com/'

cred_object = firebase_admin.credentials.Certificate('brcdfb-300dc-firebase-adminsdk-21dpo-4b65e379c5.json')
default_app = firebase_admin.initialize_app(cred_object, {
	'databaseURL':databaseURL
	})

ref = db.reference('Database reference')



from firebase_admin import db

ref = db.reference("/")

for key in ref.get().keys():
    if key == 'pending':
        continue
    file_id = ref.get()[key]['image'].replace('https://drive.google.com/open?id=','')
    email = ref.get()[key]['email']
    imeis = read_imei(file_id)
    

    ref_post = db.reference("/pending/")
    subject = 'codes for '+str(email)
    ref_post.push({'imei':imeis,'subject':subject,'email':email})

    ref.child(key).delete()
