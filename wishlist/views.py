from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Wishlist

# View wishlist of the logged-in user
@login_required
def wishlist_view(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist/wishlist.html', {'wishlist': wishlist})

# Add a product to wishlist
@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)
    
    if created:
        wishlist_item.save()
    return redirect('wishlist:wishlist_view')

# Remove a product from wishlist
@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.filter(user=request.user, product=product).delete()
    return redirect('wishlist:wishlist_view')
