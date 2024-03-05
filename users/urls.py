from django.urls import path
from users.apps import UsersConfig
from users.views import PaymentListView
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from rest_framework import routers
from users.views import UserViewSet

app_name = UsersConfig.name


urlpatterns = [
    path('payments/', PaymentListView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

router = routers.SimpleRouter()
router.register('user', UserViewSet)
urlpatterns += router.urls
