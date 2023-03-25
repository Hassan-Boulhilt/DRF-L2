from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Ebook(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    description = models.TextField()
    publication_date = models.DateField()
    
    def str(self):
        return self.title
    
class Review(models.Model):
    review = models.TextField(blank=True,null=True)
    review_author = models.CharField(max_length=120, blank=True,null=True)
    ebook = models.ForeignKey(Ebook, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def str(self):
        return str(self.rating)