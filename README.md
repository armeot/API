# API for Daftcode Intership Interview
Web API created with Python 3.9.5 using FLask, RESTful and SQLAlchemy.  
It allows to create, see, edit and delete short messages.

## Launch
API is deployed at: https://armeot-api.herokuapp.com/

## How to use
To begin with import HTTPBasicAith and requests.
```
from flask_httpauth import HTTPBasicAuth
import requests
```

#### GET - returns a list of messages  
route: /message/
```
requests.get("https://armeot-api.herokuapp.com/messages/")
```

#### POST - allows to creates a new message  
route: /message/  
After specifying the route, provide the content of the message and infomation needed for authentication (username and password).
```
USER_DATA = ['username', 'password']
requests.post("https://armeot-api.herokuapp.com/messages/"
              ,{"content": "Content of the message."}
              ,auth=(USER_DATA[0], USER_DATA[1]))
```

#### PATCH - allows to edits a content message
route: /message/{id}
```
USER_DATA = ['username', 'password']
requests.patch("https://armeot-api.herokuapp.com/messages/1"
              ,{"content": "New content of the message."}
              ,auth=(USER_DATA[0], USER_DATA[1]))
```

#### DELETE - allows to deletes a message
route: /message/{id}
```
USER_DATA = ['username', 'password']
requests.delete("https://armeot-api.herokuapp.com/messages/1"
              ,auth=(USER_DATA[0], USER_DATA[1]))
```
