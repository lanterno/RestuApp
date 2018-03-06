"""
restuapp URL Configuration
"""
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.views.static import serve
from django.views.generic import RedirectView

from restuapp.core.views import SwaggerSchemaView

from .routers import router

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='docs', permanent=False), name='index'),
    path('api/v1/docs/', SwaggerSchemaView.as_view(), name='docs'),
    path('api/v1/', include(router.urls)),
]
