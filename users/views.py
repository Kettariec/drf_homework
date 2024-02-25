from users.models import Payment
from rest_framework import filters
from users.serializers import PaymentSerializer
from rest_framework.generics import ListAPIView


class PaymentListView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['date']
    search_fields = ['course__name', 'lesson__name', 'type']
