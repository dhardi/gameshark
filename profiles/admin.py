from django.contrib import admin
from django.utils.html import format_html

from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'default_phone_number', 'default_country',
        'profile_picture_tag'
    )
    readonly_fields = ('profile_picture_tag',)

    def profile_picture_tag(self, obj):
        if obj.profile_picture:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px;" />'.format(
                    obj.profile_picture.url
                )
            )
        return "No Image"
    profile_picture_tag.short_description = 'Profile Picture'


# Register your UserProfile model with the custom admin class
admin.site.register(UserProfile, UserProfileAdmin)
