from django.contrib import admin
from .models import Wishlist

class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created_at')  # Mostra esses campos no admin
    search_fields = ('user__username', 'product__name')  # Adiciona barra de busca
    list_filter = ('created_at',)  # Permite filtrar por data de criação

admin.site.register(Wishlist, WishlistAdmin)
