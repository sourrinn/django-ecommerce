from django import forms
from .models import Product, Review, Order, OrderItem, Customer, Address, Payment, Wishlist, Coupon, Shipping


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1)


class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(choices=[(i, str(i)) for i in range(1, 6)])
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'products', 'total_price', 'order_date']
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'products': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'total_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'order_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'quantity']
        widgets = {
            'order': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
        widgets = {
            # Add appropriate widgets for address fields
        }


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
        widgets = {
            # Add appropriate widgets for payment fields
        }


class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = '__all__'
        widgets = {
            # Add appropriate widgets for wishlist fields
        }


class CouponForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = '__all__'
        widgets = {
            # Add appropriate widgets for coupon fields
        }


class ShippingForm(forms.ModelForm):
    class Meta:
        model = Shipping
        fields = '__all__'
        widgets = {
            # Add appropriate widgets for shipping fields
        }


# Add more form classes as needed
