# Register your models here.
from django.contrib import admin
from .models import Expense

class LocationExpense(admin.ModelAdmin):
    list_display = ('name', 'price')

admin.site.register(Expense, LocationExpense)  #註冊至Administration(管理員後台)

