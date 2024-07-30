from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

class Book:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

# Create a list of Book instances
books = [
    Book('Lolo', 'tabby', 'Kinda rude.', 3),
    Book('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
    Book('Fancy', 'bombay', 'Happy fluff ball.', 4),
    Book('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]

# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

def about(request):
    # Send a simple HTML response
    return render(request, 'about.html')

def book_index(request):
    # Render the books/index.html template with the books data
    return render(request, 'books/index.html', {'books': books})