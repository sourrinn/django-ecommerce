from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Product, Category, Cart, CartItem, Address, Payment, Review, Wishlist, Coupon, Shipping, Order


class EcommerceTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.category = Category.objects.create(name='Electronics')
        self.product = Product.objects.create(
            name='Laptop', price=1000, category=self.category)

    def test_add_to_cart(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(
            reverse('ecommerce:add_to_cart', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.user.cart.items.count(), 1)

    def test_remove_from_cart(self):
        self.client.login(username='testuser', password='testpassword')
        cart_item = CartItem.objects.create(
            cart=self.user.cart, product=self.product)
        response = self.client.get(
            reverse('ecommerce:remove_from_cart', args=[cart_item.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.user.cart.items.count(), 0)

    def test_product_detail(self):
        response = self.client.get(
            reverse('ecommerce:product_detail', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)

    def test_add_review(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('ecommerce:add_review', args=[self.product.id]), {
            'rating': 5,
            'comment': 'Great laptop!'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.product.reviews.count(), 1)

    def test_add_to_wishlist(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(
            reverse('ecommerce:add_to_wishlist', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.user.wishlist.products.count(), 1)

    def test_remove_from_wishlist(self):
        self.client.login(username='testuser', password='testpassword')
        wishlist = Wishlist.objects.create(user=self.user)
        wishlist.products.add(self.product)
        response = self.client.get(
            reverse('ecommerce:remove_from_wishlist', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.user.wishlist.products.count(), 0)

    def test_order_detail(self):
        self.client.login(username='testuser', password='testpassword')
        order = Order.objects.create(
            customer=self.user, total_price=100, order_date='2023-06-13 12:00:00')
        response = self.client.get(
            reverse('ecommerce:order_detail', args=[order.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, order.customer.username)

    def test_view_cart(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('ecommerce:cart'))
        self.assertEqual(response.status_code, 200)

    def test_checkout(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('ecommerce:checkout'))
        self.assertEqual(response.status_code, 200)

    def test_view_wishlist(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('ecommerce:wishlist'))
        self.assertEqual(response.status_code, 200)

    def test_order_history(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('ecommerce:order_history'))
        self.assertEqual(response.status_code, 200)

    def test_order_detail_history(self):
        self.client.login(username='testuser', password='testpassword')
        order = Order.objects.create(
            customer=self.user, total_price=100, order_date='2023-06-13 12:00:00')
        response = self.client.get(
            reverse('ecommerce:order_detail_history', args=[order.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, order.customer.username)

    # Add more test cases as needed
