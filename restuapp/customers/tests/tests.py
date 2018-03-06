from django.urls import reverse
from rest_framework.test import APITestCase

from ..models import Customer
from .factories import CustomerFactory


class CustomersAPITestCases(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.customer1 = CustomerFactory()
        CustomerFactory.create_batch(5)

    def setUp(self):
        self.customer1.refresh_from_db()

    def test_lookup_for_customer_by_exact_phone_number(self):
        resp = self.client.get(
            path=reverse('customer-list') + '?phone={}'.format(self.customer1.phone),
        )
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 1)
        self.assertEqual(resp.data[0]['id'], self.customer1.id)

    def test_create_new_customer(self):
        no_of_customers = Customer.objects.count()
        resp = self.client.post(
            path=reverse('customer-list'),
            data={
                'name': 'Jon Targaryen',  # aka. John Snow
                'phone': '+705096839744',
                'address': 'The North/ South of the wall'
            }
        )
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(Customer.objects.count(), no_of_customers + 1)

    def test_update_customer(self):
        resp = self.client.patch(
            path=reverse('customer-detail', kwargs={'pk': self.customer1.id}),
            data={
                'address': 'The Wall!!',
            }
        )
        self.assertEqual(resp.status_code, 200)
        self.customer1.refresh_from_db()
        self.assertEqual(self.customer1.address, 'The Wall!!')

    def test_cant_create_multiple_accounts_with_same_phone_number(self):
        self.client.post(
            path=reverse('customer-list'),
            data={
                'name': 'Jon Targaryen',  # aka. John Snow
                'phone': '+705096839744',
                'address': 'The North/ South of the wall'
            }
        )
        resp = self.client.post(
            path=reverse('customer-list'),
            data={
                'name': 'Aria Stark',
                'phone': '+705096839744',
                'address': 'Everywhere..'
            }
        )
        self.assertEqual(resp.status_code, 400)
        self.assertIn('phone', resp.data.keys())

    def test_can_only_delete_customer_if_he_or_she_has_no_orders(self):
        # TODO: This feature isn't required right now, but to be added in the future.
        pass
