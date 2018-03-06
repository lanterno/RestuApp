import random

from faker.providers import BaseProvider

from ..models import Order


class PizzaOrderFakeProvider(BaseProvider):

    def pizza_size(self):
        return random.choice(Order.SIZES)[0]
