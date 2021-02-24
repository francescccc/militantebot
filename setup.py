import pyrebase

config = {
    "apiKey": "AIzaSyD1s2TKUXZcUVTpOtqfqTQm8AAbV2R7HdE",
    "authDomain": "tweet-bb608.firebaseapp.com",
    "projectId": "tweet-bb608",
    "storageBucket": "tweet-bb608.appspot.com",
    "messagingSenderId": "271208042340",
    "appId": "1:271208042340:web:f89694e1c054976c5bf471",
    "measurementId": "G-PF3FJ5R1NE",
    "databaseURL": "https://tweet-bb608-default-rtdb.firebaseio.com",
    "serviceAccount": "serviceAccountCredentials.json",
}


firebase = pyrebase.initialize_app(config)
db = firebase.database()



data = {"id1":"1364622339074359308"}
users = db.update(data)