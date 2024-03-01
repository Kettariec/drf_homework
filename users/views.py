from users.models import Payment
from rest_framework import filters
from users.serializers import (PaymentSerializer,
                               UserSerializer, UserDetailSerializer)
from rest_framework.generics import (ListAPIView, RetrieveAPIView,
                                     DestroyAPIView, UpdateAPIView,
                                     CreateAPIView)
from users.models import User
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsOwner


class PaymentListView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['date']
    search_fields = ['course__name', 'lesson__name', 'type']
    permission_classes = [IsAuthenticated, IsOwner]


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwner]
