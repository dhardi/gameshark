from django.shortcuts import render
from django.contrib import messages
from testimonial.models import Testimonial
from products.models import Product, Category  

def index(request):
    """ A view to return the index page """
    
    
    testimonials = Testimonial.objects.all()
    
    
    try:
        deals_category = Category.objects.get(name="deals")
        hot_deals = Product.objects.filter(category=deals_category)
    except Category.DoesNotExist:
        deals_category = None
        hot_deals = []

        messages.warning(request, "A categoria 'Deals' não foi encontrada.")

    context = {
        'testimonials': testimonials,
        'hot_deals': hot_deals,
        'deals_category': deals_category,  
    }

    return render(request, 'home/index.html', context)
