from django.db import models
from django.contrib.auth.models import User


class Quote(models.Model):
    quote_author = models.ForeignKey(User, on_delete=models.CASCADE)
    quote_body = models.CharField(max_length=255)
    context = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.quote_body
    class Meta:
        verbose_name_plural = "Quotes"
