from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product', 'user', 'rating', 'title', 'created_at', 'updated_at')
    list_filter = ('rating', 'created_at', 'updated_at')
    search_fields = ('product__name', 'user__username', 'title', 'body')


admin.site.register(Review, ReviewAdmin)
