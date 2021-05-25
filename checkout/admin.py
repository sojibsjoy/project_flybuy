from django.contrib import admin
from checkout.models import Summary, DeliveryAddress, DeliveryOption, PaymentMethod

# Register your models here.
admin.site.register(Summary)
admin.site.register(DeliveryAddress)
admin.site.register(DeliveryOption)
admin.site.register(PaymentMethod)
