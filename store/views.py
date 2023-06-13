from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Cart, CartItem, Address, Payment, Review, Wishlist, Coupon, Shipping, Order
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(
        cart=cart, product=product)

    if item_created:
        cart_item.quantity = 1
    else:
        cart_item.quantity += 1

    cart_item.save()
    messages.success(request, 'Product added to cart.')
    return redirect('cart')


@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(
        CartItem, id=cart_item_id, cart__user=request.user)
    cart_item.delete()
    messages.success(request, 'Product removed from cart.')
    return redirect('cart')


@login_required
def view_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    context = {
        'cart': cart
    }
    return render(request, 'cart.html', context)


@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    shipping_address = cart.user.addresses.first()
    billing_address = cart.user.billing_addresses.first()

    if request.method == 'POST':
        shipping_address_id = request.POST.get('shipping_address')
        billing_address_id = request.POST.get('billing_address')
        payment_method = request.POST.get('payment_method')
        coupon_code = request.POST.get('coupon_code')

        shipping_address = get_object_or_404(
            Address, id=shipping_address_id, user=request.user)
        billing_address = get_object_or_404(
            Address, id=billing_address_id, user=request.user)

        coupon = get_object_or_404(
            Coupon, code=coupon_code) if coupon_code else None

        order = Order.objects.create(
            customer=request.user,
            total_price=cart.total_price,
            shipping_address=shipping_address,
            billing_address=billing_address,
            payment_method=payment_method,
            coupon=coupon,
            shipping_method=None,
            is_completed=False
        )

        order.items.set(cart.items.all())

        cart.delete()
        messages.success(request, 'Order placed successfully.')
        return redirect('order_detail', order.id)

    addresses = Address.objects.filter(user=request.user)
    context = {
        'cart': cart,
        'addresses': addresses,
        'shipping_address': shipping_address,
        'billing_address': billing_address,
        'payment_methods': Payment.METHOD_CHOICES,
        'coupons': Coupon.objects.all()
    }
    return render(request, 'checkout.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = product.reviews.all()
    context = {
        'product': product,
        'reviews': reviews
    }
    return render(request, 'product_detail.html', context)


@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        review = Review.objects.create(
            user=request.user,
            product=product,
            rating=rating,
            comment=comment
        )

        messages.success(request, 'Review added successfully.')
        return redirect('product_detail', product.id)

    context = {
        'product': product
    }
    return render(request, 'add_review.html', context)


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist, _ = Wishlist.objects.get_or_create(user=request.user)
    wishlist.products.add(product)
    messages.success(request, 'Product added to wishlist.')
    return redirect('wishlist')


@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist = get_object_or_404(Wishlist, user=request.user)
    wishlist.products.remove(product)
    messages.success(request, 'Product removed from wishlist.')
    return redirect('wishlist')


@login_required
def view_wishlist(request):
    wishlist = get_object_or_404(Wishlist, user=request.user)
    context = {
        'wishlist': wishlist
    }
    return render(request, 'wishlist.html', context)


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, customer=request.user)
    context = {
        'order': order
    }
    return render(request, 'order_detail.html', context)
