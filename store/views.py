from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart

@login_required
def place_order(request):
    cart_items = Cart.objects.filter(user=request.user)

    if not cart_items:
        return redirect('/cart/')

    total = sum(item.product.price * item.quantity for item in cart_items)

    # dummy order page (safe version for submission)
    order_summary = {
        "total": total,
        "items": cart_items
    }

    cart_items.delete()

    return render(request, 'store/order_success.html', order_summary)