from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Review
from .forms import ReviewForm
from products.models import Product

@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    # Verifica se o usuário já fez um review deste produto
    existing_review = Review.objects.filter(product=product, user=request.user).first()
    
    if existing_review:
        messages.error(request, "You have already reviewed this product.")
        return redirect('product_detail', product_id=product.id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, "Review added successfully!")
            return redirect('product_detail', product_id=product.id)
    else:
        form = ReviewForm()

    return render(request, 'reviews/add_review.html', {'form': form, 'product': product})

# Editar Review
@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if review.user != request.user:
        return redirect('product_detail', product_id=review.product.id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review has been updated!')
            return redirect('product_detail', product_id=review.product.id)
    else:
        form = ReviewForm(instance=review)
    
    return render(request, 'reviews/edit_review.html', {'form': form, 'review': review})

# Excluir Review
@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    product_id = review.product.id
    if review.user == request.user:
        review.delete()
        messages.success(request, 'Your review has been deleted.')
    
    return redirect('product_detail', product_id=product_id)
