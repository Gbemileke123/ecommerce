from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100)


class State(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.RESTRICT)


class Address(models.Model):
    street = models.CharField(max_length=255)
    lga = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.RESTRICT)


class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.ForeignKey(Address, on_delete=models.RESTRICT)


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.RESTRICT)
    job_title = models.CharField(max_length=255)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.RESTRICT)


class ProductImage(models.Model):
    name = models.CharField(max_length=255)
    image = models.URLField(max_length=500)


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey("Category", on_delete=models.CASCADE, null=True, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=50, decimal_places=2)
    description = models.CharField(max_length=255)
    product_image = models.ForeignKey(ProductImage, on_delete=models.RESTRICT)
    category = models.ManyToManyField(Category, blank=True)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    shipping_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    order_status = models.BooleanField(default=False)
    product = models.ManyToManyField(Product, blank=True)
    order_ref = models.UUIDField(auto_created=True)


class Payment(models.Model):
    amount = models.DecimalField(max_digits=50, decimal_places=2)
    reference_number = models.CharField(max_length=10, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    order = models.ForeignKey(Order, on_delete=models.RESTRICT)
    verified = models.BooleanField(default=False)


class Feedback(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    message = models.TextField(max_length=1000)
