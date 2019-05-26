from django.http import HttpResponse
from django.test import Client, SimpleTestCase


# Create your tests here.
class GetTest(SimpleTestCase):

    def test_home(self):
        client = Client()
        client.get('/')
        self.assertEqual(HttpResponse.status_code, 200)

    def test_about(self):
        client = Client()
        client.get('/about')
        self.assertEqual(HttpResponse.status_code, 200)

    def test_clinic(self):
        client = Client()
        client.get('/clinic')
        self.assertEqual(HttpResponse.status_code, 200)

    def test_agreement(self):
        client = Client()
        client.get('/agreement')
        self.assertEqual(HttpResponse.status_code, 200)
