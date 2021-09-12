from django.contrib import admin
from app.models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "amount", "order_details")

admin.site.register(Order, OrderAdmin)
