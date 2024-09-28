# models.py do app testimonial

from django.db import models
from django.contrib.auth.models import User
from checkout.models import Order  # Importando a Order para relacionamento

class Testimonial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=False, blank=False)  # Relacionamento com Order
    text = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Rating de 1 a 5 estrelas
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Testimonial by {self.user.username} for order {self.order.order_number}"
