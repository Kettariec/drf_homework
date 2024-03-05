from users.models import Payment
from rest_framework import filters, viewsets, status
from users.serializers import PaymentSerializer, UserSerializer
from rest_framework.generics import ListAPIView
from users.models import User
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsOwner
from rest_framework.response import Response


class PaymentListView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['date']
    search_fields = ['course__name', 'lesson__name', 'type']
    permission_classes = [IsAuthenticated, IsOwner]


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        password = serializer.data['password']
        user = User.objects.get(pk=serializer.data['id'])
        if user:
            user.set_password(password)
            user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        user = User.objects.get(pk=kwargs.get('pk'))
        user.set_password(request.data.get('password'))
        request.data['password'] = user.password
        serializer = self.serializer_class(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
