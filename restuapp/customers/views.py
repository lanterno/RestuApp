from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, UpdateModelMixin
)

from .serializers import CustomerSerializer
from .models import Customer


class CustomerViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    filter_fields = ('phone', )
