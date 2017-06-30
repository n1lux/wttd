from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(name='Nilo Alexandre', cpf='12345678901', email='nilo@teste.com', phone='19-984215632')
        self.obj.save()

    def tearDown(self):
        pass

    def test_create(self):
        self.assertTrue(Subscription.objects.all())

    def test_created_at(self):
        """Subscritption must have an auto created at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Nilo Alexandre', str(self.obj))