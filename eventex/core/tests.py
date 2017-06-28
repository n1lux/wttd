from django.test import TestCase

# Create your tests here.


class HomeTest(TestCase):

    def setUp(self):
        self.response = self.client.get('/')

    def tearDown(self):
        pass

    def test_get(self):
        """Must be returned status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must be returned template index.html"""
        self.assertTemplateUsed(self.response, 'index.html')

    def test_subscription_link(self):
        self.assertContains(self.response, 'href="/inscricao/"')