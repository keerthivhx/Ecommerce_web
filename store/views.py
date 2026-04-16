def increase_quantity(request, id):
    item = Cart.objects.get(id=id, user=request.user)
    item.quantity += 1
    item.save()
    return redirect('/cart/')


def decrease_quantity(request, id):
    item = Cart.objects.get(id=id, user=request.user)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect('/cart/')