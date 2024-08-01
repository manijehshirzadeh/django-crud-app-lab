from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'books/detail.html', {'book': book})

class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    success_url = '/books/'

class BookUpdate(UpdateView):
    model = Book
    # Let's disallow the renaming of a book by excluding the name field!
    fields = ['author', 'description', 'pages']

class BookDelete(DeleteView):
    model = Book
    success_url = '/books/'