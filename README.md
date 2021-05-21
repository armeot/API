# API for Daftcode Intership Interview
Web API created with Python 3.9.5 using FLask, RESTful and SQLAlchemy.  
It allows to create, see, edit and delete short messages.

## Launch
### a. Locally
To begin with install all of the requirements.  
Open a console and go to the project folder. Type:
```
pip3 install -r requirements.txt
```
To launch the project. Type:
```
python3 main.py
```
No you can acces it at:  http://127.0.0.1:5000/  
### b. Globally
API is deployed at: https://armeot-api.herokuapp.com/

## How to use
First import HTTPBasicAuth and requests.
```
from flask_httpauth import HTTPBasicAuth
import requests
```

#### GET - returns a list of messages  
Local rote: http://127.0.0.1:5000/message/  
Global route: https://armeot-api.herokuapp.com/message/
```
requests.get("https://armeot-api.herokuapp.com/messages/")
```
As a result api will return a data in json format.

#### POST - allows to creates a new message  
Local rote: http://127.0.0.1:5000/message/  
Global route: https://armeot-api.herokuapp.com/message/  
  
After specifying the route, provide the content of the message and infomation needed for authentication (username and password).
```
USER_DATA = ['username', 'password']
requests.post("https://armeot-api.herokuapp.com/messages/"
              ,{"content": "Content of the message."}
              ,auth=(USER_DATA[0], USER_DATA[1]))
```

#### PATCH - allows to edits a content message
Local rote: http://127.0.0.1:5000/message/{id}  
Global route: https://armeot-api.herokuapp.com/message/{id}  
  
After specifying the route and choosing an id, provide the new content of the message and infomation needed for authentication (username and password).
```
USER_DATA = ['username', 'password']
requests.patch("https://armeot-api.herokuapp.com/messages/1"
              ,{"content": "New content of the message."}
              ,auth=(USER_DATA[0], USER_DATA[1]))
```

#### DELETE - allows to deletes a message
Local rote: http://127.0.0.1:5000/message/{id}  
Global route: https://armeot-api.herokuapp.com/message/{id}  
  
After specifying the route and choosing an id, provide the infomation needed for authentication (username and password).
```
USER_DATA = ['username', 'password']
requests.delete("https://armeot-api.herokuapp.com/messages/1"
              ,auth=(USER_DATA[0], USER_DATA[1]))
```
