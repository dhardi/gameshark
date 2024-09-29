# urls.py do app testimonial

from django.urls import path
from . import views

urlpatterns = [
    path('', views.testimonial_list, name='testimonial_list'),
    path('add/<str:order_number>/', views.add_testimonial, name='add_testimonial'),  # Exige order_number
    path('delete/<int:id>/', views.delete_testimonial, name='delete_testimonial'),
    path('edit/<int:testimonial_id>/', views.edit_testimonial, name='edit_testimonial'),
]
