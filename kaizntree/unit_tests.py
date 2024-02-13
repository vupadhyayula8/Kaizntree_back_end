from django.test import TestCase, Client
from django.contrib.auth.hashers import make_password
from kaizntree.dbModels import UserDetails, UserItems
import json

class TestViews(TestCase):
    def setUp(self):
        # Set up test data
        self.client = Client()
        self.username = "test_user"
        self.password = "test_password"
        UserDetails(username=self.username, password=make_password(self.password))

    def test_login_success(self):
        data = {
            "username": self.username,
            "password": self.password
        }
        response = self.client.post('/login/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["status"], True)

    def test_login_failure(self):
        data = {
            "username": self.username,
            "password": "wrong_password"
        }
        response = self.client.post('/login/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["status"], False)

    def test_register_success(self):
        data = {
            "username": "new_user",
            "password": "new_password"
        }
        response = self.client.post('/register/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], True)

    def test_register_failure(self):
        data = {
            "username": self.username,
            "password": "new_password"
        }
        response = self.client.post('/register/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], False)

    # ------------------------------------------------------------------------------------------------------------ #
    # ------------------------------------------------------------------------------------------------------------ #
    def test_fetch_items(self):
        data = {
            "username": self.username
        }
        response = self.client.post('/fetch_items/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        # Add more assertions as needed

    def test_add_item(self):
        response = self.client.post('/add_item/')
        self.assertEqual(response.status_code, 200)
        # Add more assertions as needed

    def test_add_category(self):
        response = self.client.post('/add_category/')
        self.assertEqual(response.status_code, 200)
        # Add more assertions as needed
