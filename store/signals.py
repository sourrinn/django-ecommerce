from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Product, Order, User, Category, Coupon


@receiver(post_save, sender=Product)
def update_product_stock(sender, instance, created, **kwargs):
    """
    Signal handler to update product stock after a product is saved or updated.
    """
    if not created and instance.stock_changed:
        # Perform actions when an existing product's stock is updated
        # For example, you can update the stock quantity based on changes in the product instance
        pass


@receiver(post_save, sender=Order)
def update_order_total(sender, instance, created, **kwargs):
    """
    Signal handler to update the total price of an order after it is saved or updated.
    """
    if not created and instance.items_changed:
        # Perform actions when an existing order's items are updated
        # For example, you can recalculate the total price based on changes in the order items
        pass


@receiver(pre_delete, sender=Order)
def release_order_products(sender, instance, **kwargs):
    """
    Signal handler to release the products of an order before it is deleted.
    """
    # Perform actions before deleting an order
    # For example, you can release the products by updating their availability or stock
    pass


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    """
    Signal handler to update the user profile after a user is saved or updated.
    """
    if created:
        # Perform actions when a new user is created
        # For example, you can create a user profile
        pass
    else:
        # Perform actions when an existing user is updated
        # For example, you can update the user profile information
        pass


@receiver(post_save, sender=Category)
def update_category_products_count(sender, instance, created, **kwargs):
    """
    Signal handler to update the count of products in a category after a product is saved, updated, or deleted.
    """
    # Perform actions after a product is saved, updated, or deleted
    # For example, you can update the count of products in the category
    pass


@receiver(post_save, sender=Coupon)
def apply_coupon_to_order(sender, instance, created, **kwargs):
    """
    Signal handler to apply a coupon code to an order and recalculate the order total.
    """
    if created:
        # Perform actions when a new coupon is created
        # For example, you can apply the coupon to eligible orders
        pass
    else:
        # Perform actions when an existing coupon is updated
        # For example, you can reapply the coupon to eligible orders
        pass


# Add more signal handlers as needed


# Connect signal handlers
post_save.connect(update_product_stock, sender=Product)
post_save.connect(update_order_total, sender=Order)
pre_delete.connect(release_order_products, sender=Order)
post_save.connect(update_user_profile, sender=User)
post_save.connect(update_category_products_count, sender=Category)
post_save.connect(apply_coupon_to_order, sender=Coupon)
