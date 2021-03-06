from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription
from django.shortcuts import resolve_url as r


class SubscriptionsNewGet(TestCase):

    def setUp(self):
        self.response = self.client.get(r('subscriptions:new'))

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


class SubscriptionsNewPost(TestCase):

    def setUp(self):
        data = {'name': 'Nilo Alexandre', 'cpf': '12345678901', 'email': 'nilo@alexandre.com', 'phone': '19-98541-1256'}
        self.resp = self.client.post(r('subscriptions:new'), data=data)

    def tearDown(self):
        pass

    def test_post(self):
        """Valid POST should redirect to /inscricao/"""
        subscription = self.resp.context['subscription']
        self.assertRedirects(self.resp, r('subscriptions:detail', subscription.uid))

    def test_save_subscription(self):
        self.assertTrue(Subscription.objects.exists())


class SubscriptionsNewPostInvalid(TestCase):
    def setUp(self):
        self.resp = self.client.post(r('subscriptions:new'), data={})

    def tearDown(self):
        pass

    def test_post(self):
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

    def test_dont_save_subscription(self):
        self.assertFalse(Subscription.objects.exists())
