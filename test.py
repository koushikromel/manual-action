import pyrebase, time, datetime

firebaseConfig = {
  "apiKey": "AIzaSyCZM1nAgvgC6keSPeO3-ba7xK2gO_4x8RI",
  "authDomain": "manual-action-72984.firebaseapp.com",
  "databaseURL": "https://manual-action-72984-default-rtdb.firebaseio.com",
  "projectId": "manual-action-72984",
  "storageBucket": "manual-action-72984.appspot.com",
  "messagingSenderId": "685097099467",
  "appId": "1:685097099467:web:9ff833ca73adc3fda73b4e",
  "measurementId": "G-M3GTTB9HP4"
}

fb = pyrebase.initialize_app(firebaseConfig)

db = fb.database()

data = db.get().val()


if data["testing"] is not None:
  date = datetime.datetime.now().strftime("%d-%m-%Y, %I:%M:%S %p")
  value = len(data["testing"])+1
  db.child("testing").child(value).set({"time": str(date)})
else:
  db.child("testing").set({"1": "Welcome"})