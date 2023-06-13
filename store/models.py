from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Description')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    price = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name='Price')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products', verbose_name='Category')

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name='User')
    products = models.ManyToManyField(
        Product, through='CartItem', verbose_name='Products')

    def __str__(self):
        return f"Cart for {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='items', verbose_name='Cart')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='Product')
    quantity = models.PositiveIntegerField(verbose_name='Quantity')

    class Meta:
        verbose_name_plural = 'Cart Items'

    def __str__(self):
        return f"Cart #{self.cart_id} - Item #{self.id}"


class Address(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='addresses', verbose_name='User')
    street = models.CharField(max_length=100, verbose_name='Street')
    city = models.CharField(max_length=100, verbose_name='City')
    state = models.CharField(max_length=100, verbose_name='State')
    country = models.CharField(max_length=100, verbose_name='Country')
    postal_code = models.CharField(max_length=20, verbose_name='Postal Code')

    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"


class Payment(models.Model):
    order = models.ForeignKey(
        'Order', on_delete=models.CASCADE, related_name='payments', verbose_name='Order')
    payment_method = models.CharField(
        max_length=100, verbose_name='Payment Method')
    transaction_id = models.CharField(
        max_length=100, verbose_name='Transaction ID')
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Amount')
    timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name='Timestamp')

    def __str__(self):
        return f"Payment for Order #{self.order.id}"


class Review(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='User')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews', verbose_name='Product')
    rating = models.PositiveIntegerField(verbose_name='Rating')
    comment = models.TextField(verbose_name='Comment')
    timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name='Timestamp')

    def __str__(self):
        return f"Review by {self.user.username} for {self.product.name}"


class Wishlist(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name='User')
    products = models.ManyToManyField(
        Product, related_name='wishlists', verbose_name='Products')
    timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name='Timestamp')

    def __str__(self):
        return f"Wishlist for {self.user.username}"


class Coupon(models.Model):
    code = models.CharField(max_length=50, verbose_name='Code')
    discount_percentage = models.PositiveIntegerField(
        verbose_name='Discount Percentage')
    expiry_date = models.DateField(verbose_name='Expiry Date')

    def __str__(self):
        return self.code


class Shipping(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    price = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name='Price')

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='orders', verbose_name='Customer')
    products = models.ManyToManyField(
        Product, through='OrderItem', verbose_name='Products')
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Total Price')
    order_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Order Date')
    shipping_address = models.ForeignKey(
        Address, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Shipping Address')
    billing_address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True,
                                        blank=True, related_name='billing_orders', verbose_name='Billing Address')
    payment_method = models.CharField(
        max_length=100, verbose_name='Payment Method')
    coupon = models.ForeignKey(
        Coupon, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Coupon')
    shipping_method = models.ForeignKey(
        Shipping, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Shipping Method')
    is_completed = models.BooleanField(
        default=False, verbose_name='Is Completed')

    class Meta:
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"Order #{self.id}"

    def get_absolute_url(self):
        return reverse('order_detail', args=[str(self.id)])
