from django.contrib import admin

# Register your models here.
from .models import Restaurant,Pizza

admin.site.register(Restaurant)
admin.site.register(Pizza)