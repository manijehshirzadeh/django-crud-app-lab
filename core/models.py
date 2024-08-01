from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    pages = models.IntegerField()

    def __str__(self):
        return self.name
    
    # Define a method to get the URL for this particular cat instance
    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this book's details
        return reverse('book-detail', kwargs={'book_id': self.id})