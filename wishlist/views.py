from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Import the messages framework
from products.models import Product
from .models import Wishlist

# View wishlist of the logged-in user
@login_required
def wishlist_view(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist/wishlist.html', {'wishlist': wishlist})

# Add a product to wishlist with success message
@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)
    
    if created:
        messages.success(request, f'{product.name} has been added to your wishlist.')
    else:
        messages.info(request, f'{product.name} is already in your wishlist.')
    
    # Redireciona de volta para a mesma página de onde veio a requisição (HTTP_REFERER)
    return redirect(request.META.get('HTTP_REFERER', 'wishlist:wishlist_view'))


# Remove a product from wishlist with success message
@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.filter(user=request.user, product=product).delete()

    messages.success(request, f'{product.name} has been removed from your wishlist.')  # Success message for removal

    return redirect('wishlist:wishlist_view')
