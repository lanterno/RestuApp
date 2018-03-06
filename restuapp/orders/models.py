from django.db import models


class Order(models.Model):
    SIZES = (
        (0, '30 cm'),
        (1, '50 cm'),
    )
    customer = models.ForeignKey('customers.Customer', related_name='orders', on_delete=models.PROTECT)
    size = models.PositiveSmallIntegerField()
