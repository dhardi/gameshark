from django.contrib import admin
from .models import Testimonial


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'rating', 'order', 'created_at')
    search_fields = ('user__username', 'text')
    list_filter = ('rating', 'created_at')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)


admin.site.register(Testimonial, TestimonialAdmin)
