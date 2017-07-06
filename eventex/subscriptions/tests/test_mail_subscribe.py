from django.test import TestCase
from django.core import mail
from django.shortcuts import resolve_url as r


class TestMailSubscribe(TestCase):
    def setUp(self):
        data = {'name': 'Nilo Alexandre', 'cpf': '12345678901', 'email': 'nilo@alexandre.com', 'phone': '19-98541-1256'}
        self.client.post(r('subscriptions:new'), data=data)
        self.email = mail.outbox[0]

    def tearDown(self):
        pass

    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_subscription_email_subject(self):
        expect = "Confirmação de Inscrição"

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'nilo@alexandre.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):

        contents = ('Nilo Alexandre', '12345678901', 'nilo@alexandre.com', '19-98541-1256')

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
