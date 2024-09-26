
from django.urls import path
from . import views


urlpatterns = [
    path('', views.testimonial_list, name='testimonial_list'),
    path('add/', views.add_testimonial, name='add_testimonial'),
    path('delete/<int:testimonial_id>/', views.delete_testimonial, name='delete_testimonial'),
]
