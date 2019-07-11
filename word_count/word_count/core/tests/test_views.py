from django.test import TestCase, Client
from django.conf import settings
from django.test import RequestFactory
from django.urls import reverse


from word_count.core.views import WordCountFormView


class TestWordCountFormView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_get_success_url(self):
      
        resp = self.client.generic(
            'GET', reverse("core:word-count"))

        self.assertEqual(resp.status_code, 200)

    def test_post_form(self):
        resp = self.client.post(reverse("core:word-count"), {'words':"skjaksj"}, follow=True)
        self.assertEqual(resp.status_code, 200)


