# Create your models here.
import uuid
from decimal import Decimal  # Import Decimal here

from django.db import models
from django.db.models import Sum

from products.models import Product


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    
    # Added fields for Stripe and webhook functionality
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)  # New subtotal field
    original_bag = models.TextField(null=False, blank=False, default='')  # Store the original shopping bag
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')  # Stripe Payment ID

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID.
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update totals each time a line item is added,
        accounting for delivery costs.
        """
        # Calculate subtotal as the sum of line item totals
        self.subtotal = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or Decimal(0)
        self.order_total = self.subtotal  # Assuming order total is the same as subtotal here
        # Calculate delivery cost as 10% of the order total
        self.delivery_cost = self.order_total * Decimal(0.10)
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=2, null=True, blank=True)  # XS, S, M, L, XL
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'


