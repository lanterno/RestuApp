import factory

from factory.django import DjangoModelFactory as Factory

from ..models import Customer


class CustomerFactory(Factory):

    class Meta:
        model = Customer
    name = factory.Faker('name')
    address = factory.Faker('address')
    phone = factory.Faker('phone_number')
