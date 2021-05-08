from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500, default='')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500, default='')
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, blank=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price
        }


class Cart(models.Model):
    username = models.CharField(max_length=50)
    address = models.TextField()
    book = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, blank=True)


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=2222)
