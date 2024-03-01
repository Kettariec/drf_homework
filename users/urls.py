from django.urls import path
from users.apps import UsersConfig
from users.views import (PaymentListView, UserDetailView,
                         UserListView, UserCreateView,
                         UserDeleteView, UserUpdateView)
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)


app_name = UsersConfig.name


urlpatterns = [
    path('', UserListView.as_view()),
    path('<int:pk>/', UserDetailView.as_view()),
    path('create/', UserCreateView.as_view()),
    path('<int:pk>/update/', UserUpdateView.as_view()),
    path('<int:pk>/delete/', UserDeleteView.as_view()),

    path('payments/', PaymentListView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
