from django.shortcuts import render
from django.contrib import messages
from testimonial.models import Testimonial
from products.models import Product, Category  # Certifique-se de que o modelo de Category está importado

def index(request):
    """ A view to return the index page """
    
    # Buscando todas as avaliações
    testimonials = Testimonial.objects.all()
    
    # Buscando a categoria 'Deals'
    try:
        deals_category = Category.objects.get(name="deals")  # Substitua "Deals" pelo nome exato da categoria
        hot_deals = Product.objects.filter(category=deals_category)
    except Category.DoesNotExist:
        deals_category = None  # Não encontramos a categoria
        hot_deals = []  # Nenhum produto para exibir

        messages.warning(request, "A categoria 'Deals' não foi encontrada.")  # Mensagem para o usuário

    context = {
        'testimonials': testimonials,
        'hot_deals': hot_deals,
        'deals_category': deals_category,  # Pode ser útil para o template
    }

    return render(request, 'home/index.html', context)
