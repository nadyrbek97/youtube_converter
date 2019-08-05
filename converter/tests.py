from django.test import TestCase, Client
from django.urls import reverse


class HomeTest(TestCase):

    def setUp(self):
        self.test_link = "https://www.youtube.com/watch?v=Mhj15W23IjA"
        self.test_email = "nadyrbek97@gmail.com"
        self.client = Client()
        self.home_url = reverse('home-view')

    def test_post_view(self):

        response = self.client.post(self.home_url, {'link': self.test_link,
                                                    'email': self.test_email})

        self.assertEqual(response.status_code, 200)
