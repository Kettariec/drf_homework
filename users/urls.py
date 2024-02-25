from django.urls import path
from users.apps import UsersConfig
from users.views import PaymentListView, UserDetailView, UserListView


app_name = UsersConfig.name


urlpatterns = [
    path('', UserListView.as_view()),
    path('<int:pk>/', UserDetailView.as_view()),
    path('payments/', PaymentListView.as_view()),
]
