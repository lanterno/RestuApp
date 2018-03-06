import factory

from factory.django import DjangoModelFactory as Factory

from restuapp.customers.tests.factories import CustomerFactory

from .faker_providers import PizzaOrderFakeProvider
from ..models import Order

factory.Faker.add_provider(PizzaOrderFakeProvider)


class OrderFactory(Factory):

    class Meta:
        model = Order

    customer = factory.SubFactory(CustomerFactory)
    size = factory.Faker('pizza_size')
