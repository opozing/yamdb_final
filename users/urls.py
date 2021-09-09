from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import ConfirmUser, CreateUser, UsersViewSet

router = DefaultRouter()
router.register(prefix='users', viewset=UsersViewSet, basename='users')

auth_patterns = [
    path('email/', CreateUser.as_view(), name='user-registration'),
    path('token/', ConfirmUser.as_view(), name='confirm-user'),
]

urlpatterns = [
    path('v1/auth/', include(auth_patterns)),
    path('v1/', include(router.urls)),
]
