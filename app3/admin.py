from django.contrib import admin

# Register your models here.
from .models import Category, Sub_Category, Products, Contact, Order, Brand
# from .models import Product

admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Products)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(Brand)

