from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
)
DEPART = (
    ('IT', 'IT'),
    ('FAD', 'FAD'),
    ('SECURITY', 'SECURITY'),
)


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)
    purchase_date = models.DateTimeField(auto_now=True)
    purchase_cost = models.PositiveIntegerField(null=True)
    location = models.CharField(max_length=100, choices=DEPART, null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    department = models.CharField(max_length=60, choices=DEPART, null=True)
    description = models.TextField(max_length=5000, null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.customer}-{self.name}'
