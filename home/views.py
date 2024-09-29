from django.shortcuts import render
from testimonial.models import Testimonial
from products.models import Product, Category  # Certifique-se de que o modelo de Category está importado

def index(request):
    """ A view to return the index page """
    
    # Buscando todas as avaliações
    testimonials = Testimonial.objects.all()
    
    # Buscando a categoria 'Deals'
    deals_category = Category.objects.get(name="deals")  # Substitua "Deals" pelo nome exato da categoria
    hot_deals = Product.objects.filter(category=deals_category)

    context = {
        'testimonials': testimonials,
        'hot_deals': hot_deals,
    }

    return render(request, 'home/index.html', context)
