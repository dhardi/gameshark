from django.contrib import admin
from .models import Testimonial

# Customização da administração do Testimonial
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'rating', 'order', 'created_at')  # Campos a serem exibidos na lista
    search_fields = ('user__username', 'text')  # Campos pelos quais é possível buscar
    list_filter = ('rating', 'created_at')  # Filtros laterais
    ordering = ('-created_at',)  # Ordena por data de criação (mais recente primeiro)
    readonly_fields = ('created_at',)  # Campos apenas para leitura

# Registrar o modelo no admin
admin.site.register(Testimonial, TestimonialAdmin)
