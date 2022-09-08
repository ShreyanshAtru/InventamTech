from django.contrib import admin
from customer.models import User, Restaurant
# Register your models here.

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['Shop', 'price']

admin.site.register(User)
admin.site.register(Restaurant, RestaurantAdmin)