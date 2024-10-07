from django.contrib import admin
from .models import Wishlist


class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created_at')
    search_fields = ('user__username', 'product__name')
    list_filter = ('created_at',)


admin.site.register(Wishlist, WishlistAdmin)
