from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:id>/', views.product_detail),
    path('cart/', views.cart),
    path('add-to-cart/<int:id>/', views.add_to_cart),
    path('remove/<int:id>/', views.remove_from_cart),
    path('increase/<int:id>/', views.increase_quantity),
    path('decrease/<int:id>/', views.decrease_quantity),

    path('register/', views.register),
    path('login/', views.user_login),
    path('logout/', views.user_logout),

    path('profile/', views.profile),
    path('order/', views.place_order),
]
