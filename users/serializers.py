from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from users.models import Payment, User


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "phone", "city", "avatar",)


class UserDetailSerializer(serializers.ModelSerializer):
    payment_list = SerializerMethodField()

    def get_payment_list(self, user):
        return PaymentSerializer(Payment.objects.filter(user=user), many=True).data

    class Meta:
        model = User
        fields = ("id", "email", "phone", "city", "avatar", "payment_list",)
