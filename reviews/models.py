from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Review(models.Model):
    product = models.ForeignKey(Product, related_name="reviews", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Rating de 1 a 5
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('product', 'user')  # Usuário pode deixar apenas 1 review por produto
        ordering = ['-created_at']

    def __str__(self):
        return f'Review for {self.product.name} by {self.user.username}'
