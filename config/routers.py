from rest_framework.routers import SimpleRouter

from restuapp.customers.views import CustomerViewSet

router = SimpleRouter()

router.register(r'customers', CustomerViewSet)
