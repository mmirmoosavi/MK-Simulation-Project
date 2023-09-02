from django.urls import path, include

from rest_framework import routers
from .views import UserViewSet, LogoutView

router = routers.DefaultRouter()

router.register("users", UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include('rest_framework.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
]
