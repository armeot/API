from flask_httpauth import HTTPBasicAuth
import requests, unittest

BASE = "http://127.0.0.1:5000/messages/"
USER_DATA = ['user', 'secretpassword']

class ApiTest(unittest.TestCase):
    # get all the messages
    def test_get_request(self): 
        result = requests.get(BASE)
        self.assertEqual(result.status_code,200)
    

    def test_post_request(self):
        # create a new message with correct auth data and content
        result = requests.post(BASE, {"content": "test put request"}, auth=(USER_DATA[0], USER_DATA[1]))
        self.assertEqual(result.status_code,201)

        # create a new message without auth data
        result = requests.post(BASE, {"content": "test put request"})
        self.assertEqual(result.status_code,401)

        # create a new message with blank content
        result = requests.post(BASE, {"content": ""}, auth=(USER_DATA[0], USER_DATA[1]))
        self.assertEqual(result.status_code,404)


    def test_delete_request(self):
        # delete a message with correct id
        result = requests.delete(BASE+"1",  auth=(USER_DATA[0], USER_DATA[1]))
        self.assertEqual(result.status_code, 204)

        # delete a message with id that doesn't exists
        result = requests.delete(BASE+"7",  auth=(USER_DATA[0], USER_DATA[1]))
        self.assertEqual(result.status_code, 404)


    # def test_patch_request(self):
    #     result = requests.patch(BASE+"7",  auth=(USER_DATA[0], USER_DATA[1]))
    #     self.assertEqual(result.status_code, 204)
