from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

app_name = 'ecommerce'

urlpatterns = [
    path('cart/', views.view_cart, name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_item_id>/',
         views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('products/<int:product_id>/',
         views.product_detail, name='product_detail'),
    path('products/<int:product_id>/add_review/',
         views.add_review, name='add_review'),
    path('wishlist/', views.view_wishlist, name='wishlist'),
    path('wishlist/add/<int:product_id>/',
         views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:product_id>/',
         views.remove_from_wishlist, name='remove_from_wishlist'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('order/history/', views.order_history, name='order_history'),
    path('order/history/<int:order_id>/',
         views.order_detail_history, name='order_detail_history'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/address/', views.manage_addresses, name='manage_addresses'),
    path('profile/address/add/', views.add_address, name='add_address'),
    path('profile/address/edit/<int:address_id>/',
         views.edit_address, name='edit_address'),
    path('profile/address/delete/<int:address_id>/',
         views.delete_address, name='delete_address'),
    path('profile/payment/', views.manage_payment_methods,
         name='manage_payment_methods'),
    path('profile/payment/add/', views.add_payment_method,
         name='add_payment_method'),
    path('profile/payment/edit/<int:payment_id>/',
         views.edit_payment_method, name='edit_payment_method'),
    path('profile/payment/delete/<int:payment_id>/',
         views.delete_payment_method, name='delete_payment_method'),
]

# Additional URLs for static files (optional)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
