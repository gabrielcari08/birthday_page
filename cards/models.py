from django.db import models
from django.contrib.auth.models import User


class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to='cards/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Card {self.pk} - {self.user.username}"
