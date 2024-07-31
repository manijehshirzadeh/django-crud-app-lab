from django.shortcuts import render

from .models import Book


# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

def about(request):
    # Send a simple HTML response
    return render(request, 'about.html')

def book_index(request):
    books = Book.objects.all()
    # Render the books/index.html template with the books data
    return render(request, 'books/index.html', {'books': books})