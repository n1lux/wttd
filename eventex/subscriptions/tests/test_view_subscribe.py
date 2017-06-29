from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscribeGet(TestCase):

    def setUp(self):
        self.response = self.client.get('/inscricao/')

    def tearDown(self):
        pass

    def test_get(self):
        """Get /inscricao/ must return status code 200 """

        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_html(self):
        """Html must contain input tags"""
        tags = (('<form', 1),
                ('<input', 6),
                ('type="text"', 3),
                ('type="email"', 1),
                ('type="submit"', 1)
        )

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_csrf(self):
        """Html must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have subscription form"""
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)


class SubscribePostValid(TestCase):

    def setUp(self):
        data = {'name': 'Nilo Alexandre', 'cpf': '12345678901', 'email': 'nilo@alexandre.com', 'phone': '19-98541-1256'}
        self.resp = self.client.post('/inscricao/', data=data)

    def tearDown(self):
        pass

    def test_post(self):
        """Valid POST should redirect to /inscricao/"""

        self.assertEqual(302, self.resp.status_code)

class SubscribePostInvalid(TestCase):
    def setUp(self):
        self.resp = self.client.post('/inscricao/', data={})

    def tearDown(self):
        pass

    def test_port(self):
        """Invalid POST should not redirect"""

        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_errors(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

class SubscribeSuccessMessage(TestCase):

    def test_message(self):
        data = {'name': 'Nilo Alexandre', 'cpf': '12345678901', 'email': 'nilo@alexandre.com', 'phone': '19-98541-1256'}
        resp = self.client.post('/inscricao/', data=data, follow=True)
        self.assertContains(resp, 'Inscrição Realizada com Sucesso!')
