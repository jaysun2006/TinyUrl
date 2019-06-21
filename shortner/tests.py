import json
import shortuuid

from django.test import TestCase
from shortner.models import URL


class URLShortenerTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.uuid = shortuuid.uuid()
        cls.joor_short_url = URL.objects.create(
            tiny_url=cls.uuid,
            source_url="https://jaysun94.me"
        )

    def test_api_can_shorten_url(self):
        params = {
            'url': 'http://www.example.com'
        }
        response = self.client.post(
            '/api/', json.dumps(params), content_type="application/json")
        self.assertEqual(response.status_code, 200)

        result = json.loads(response.content.decode('utf8'))
        self.assertIsInstance(
            result['tiny_url'], type(shortuuid.uuid()))

    def test_api_can_return_urls(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)

        result = json.loads(response.content.decode('utf8'))
        self.assertEqual(len(result['data']), 1)

    def test_api_can_redirect(self):
        response = self.client.get('/{0}/'.format(self.uuid))
        self.assertEqual(response.status_code, 302)
