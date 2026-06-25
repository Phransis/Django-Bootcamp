from django.contrib import admin

from payments.models import Payment

# Register your models here.

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'timestamp', 'status', 'method')
    list_filter = ('status', 'method', 'timestamp')
    search_fields = ('id',)
    ordering = ('-timestamp',)
admin.site.register(Payment, PaymentAdmin)
