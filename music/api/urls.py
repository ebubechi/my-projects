from django.urls import include,re_path
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]