from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from users.models import Payment, User
from rest_framework.relations import SlugRelatedField


class PaymentSerializer(serializers.ModelSerializer):
    # SlugRelatedField для вывода почты юзера, а не его id
    user = SlugRelatedField(slug_field='email', queryset=User.objects.all())

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
        fields = ("id", "email", "phone", "city", "avatar", "payment_list", "password")


# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#
#         # Добавление пользовательских полей в токен
#         token['username'] = user.username
#         token['email'] = user.email
#
#         return token
