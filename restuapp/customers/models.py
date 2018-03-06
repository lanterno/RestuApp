from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()  # TODO: refactor into a separate model, or an ArrayField to support multiple addresses
    phone = models.CharField(max_length=18, unique=True)

    def __str__(self):
        return self.name
