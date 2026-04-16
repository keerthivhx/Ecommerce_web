from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('register/', views.register),
    path('login/', views.user_login),
    path('logout/', views.user_logout),
    path('remove/<int:id>/', views.remove_from_cart),
    path('increase/<int:id>/', views.increase_quantity),
    path('decrease/<int:id>/', views.decrease_quantity),
]  