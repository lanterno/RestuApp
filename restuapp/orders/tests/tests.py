from rest_framework.test import APITestCase

from restuapp.customers.tests.factories import CustomerFactory
from .factories import OrderFactory


class OrdersAPITestCases(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.john = CustomerFactory()
        cls.aria = CustomerFactory()
        cls.john_orders = OrderFactory.create_batch(5)
        cls.aria_orders = OrderFactory.create_batch(3)

    def setUp(self):
        pass

    def test_create_new_order(self):
        pass

    def test_update_existing_order(self):
        pass

    def cancel_an_order(self):
        pass
