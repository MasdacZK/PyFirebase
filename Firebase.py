import firebase_admin
from firebase_admin import db

cred_obj = firebase_admin.credentials.Certificate('C:/Users/Daniel Roldan/Desktop/sistemas-distribuidos-bd807-firebase-adminsdk-w29l9-04bedf2332.json')
default_app = firebase_admin.initialize_app(cred_obj, {'databaseURL':'https://sistemas-distribuidos-bd807-default-rtdb.firebaseio.com/'})

ref =db.reference('/Nombres')
ref.push({'Nombre':'Mauricio','Apellido':'Rodriguez','Edad':'23'})

ref = db.reference('Nombres')
nombre = {'Nombre':'Daniel','Apellido':'Roldan','Edad':'26'}
nombre_ref=ref.push(nombre)

ref=db.reference('/Nombres')
producto_ref= ref.child('-NGYXDfspv_mH87TdSOV')
producto_ref.update({'Edad':'24'})