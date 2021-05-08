from django.contrib import admin
from api.models import Product, Category, Cart, User

# Register your models here.
admin.site.register(Product),
admin.site.register(Category),
admin.site.register(Cart),
admin.site.register(User)
