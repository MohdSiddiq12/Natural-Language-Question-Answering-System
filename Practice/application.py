import pyrebase

config = {
  "apiKey": "AIzaSyBjo2V2n3Tu3WzYP0CBQEMl9fDcyl2SQA8",
  "authDomain": "testing-58ac9.firebaseapp.com",
  "projectId": "testing-58ac9",
  "storageBucket": "testing-58ac9.appspot.com",
  "messagingSenderId": "96371435136",
  "appId": "1:96371435136:web:597bc6873d37ad3f80a865",
  "measurementId": "G-THMPKPSH3Q"
}

firebase = firebase.initialize_app(config)

db = firebase.database()

db.child("names").push({"name":"siddiq"})