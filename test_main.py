from flask_httpauth import HTTPBasicAuth
import requests, unittest

BASE = "http://127.0.0.1:5000/messages/"
USER_DATA = ['user', 'secretpassword']


class ApiTest(unittest.TestCase):
    # get requests
    def test_get_request(self): 
        # get all messages correctly
        result = requests.get(BASE)
        self.assertEqual(result.status_code,200)

        # get all messages using a specific id 
        result = requests.get(BASE+"1/")
        self.assertEqual(result.status_code,404)
    

    # post requests
    def test_post_request(self):
        # create a new message with correct auth data and content
        result = requests.post(BASE, {"content": "test post request"}, auth=(USER_DATA[0], USER_DATA[1]))
        self.assertEqual(result.status_code,201)

        # create a new message without auth data
        result = requests.post(BASE, {"content": "test post request"})
        self.assertEqual(result.status_code,401)

        # create a new message with blank content
        result = requests.post(BASE, {"content": ""}, auth=(USER_DATA[0], USER_DATA[1]))
        self.assertEqual(result.status_code,404)



    # delete requests
    def test_delete_request(self):
        # delete a message with correct id
        result = requests.delete(BASE+"13",  auth=(USER_DATA[0], USER_DATA[1]))
        self.assertEqual(result.status_code, 204)

        # delete a message with id that doesn't exists
        result = requests.delete(BASE+"7",  auth=(USER_DATA[0], USER_DATA[1]))
        self.assertEqual(result.status_code, 404)


    # patch requests
    def test_patch_request(self):
        # update a message with correct id and content
        result = requests.patch(BASE+"11", {"content": "test patch request"}, auth=(USER_DATA[0], USER_DATA[1]))
        self.assertEqual(result.status_code, 200)

        # update a message without content
        result = requests.patch(BASE+"8", auth=(USER_DATA[0], USER_DATA[1]))
        self.assertEqual(result.status_code, 400)

        # update a message with message that doesn't exists
        result = requests.patch(BASE+"5", auth=(USER_DATA[0], USER_DATA[1]))
        self.assertEqual(result.status_code, 400)

        # update a message with blank content
        result = requests.patch(BASE+"6", {"content": "test patch request"}, auth=(USER_DATA[0], USER_DATA[1]))
        self.assertEqual(result.status_code, 404)

