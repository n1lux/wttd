from django.test import TestCase

from eventex.subscriptions.models import Subscription


class SubscriptionDatailGet(TestCase):
    def setUp(self):
        self.obj = Subscription.objects.create(
            name="Nilo Alexandre",
            cpf="12345678901",
            email="nilo@mailinator.com",
            phone="21-25632-896645"
        )
        self.resp = self.client.get('/inscricao/{}/'.format(self.obj.uid))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_datail.html')

    def test_context(self):
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        contents = (self.obj.name, self.obj.cpf, self.obj.email, self.obj.phone)

        with self.subTest():
            for content in contents:
                self.assertContains(self.resp, content)


class SubcriptionDetailNotFound(TestCase):
    def test_not_found(self):
        resp = self.client.get('/inscricao/0/')
        self.assertEqual(404, resp.status_code)
