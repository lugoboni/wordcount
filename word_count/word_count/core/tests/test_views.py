from django.test import TestCase, Client
from django.conf import settings
from django.test import RequestFactory
from django.urls import reverse


from ..views import WordCountFormView, COUNT_RESULT_MESSAGE


class TestWordCountFormView(TestCase):

    def setUp(self):
        self.client = Client()
        self.bag_of_ten_words = "uno dos tes cuatro cinco sies siete ocho nueve diez"

    def test_get_success_url(self):
      
        resp = self.client.generic(
            'GET', reverse("core:word-count"))

        self.assertEqual(resp.status_code, 200)

    def test_post_form(self):
        resp = self.client.post(reverse("core:word-count"), {'words': self.bag_of_ten_words}, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(COUNT_RESULT_MESSAGE.format(10), str(resp.content))


