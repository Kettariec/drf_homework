from django.contrib import admin
from users.models import User, Payment


@admin.register(User)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'city',)
    list_filter = ('email',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'paid_course', 'sum', 'type',)
    list_filter = ('user', 'date', 'type',)
