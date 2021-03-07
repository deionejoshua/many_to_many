from django.shortcuts import render, redirect
from .models import Author, Book


def index(request):
    return render(request, 'index.html')


def authors(request):
    context = {
        "all_authors" : Author.objects.all(),
        
    }
    return render(request, 'authors.html', context)


def create_authors(request):
    new_author = Author.objects.create (
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        notes = request.POST['notes']
    )
    return redirect('/authors')

def writer(request, Author_id):
    context = {
        "one_author" : Author.objects.get(id = Author_id),
        "all_books" : Book.objects.all()
    }

    return render(request, 'authordet.html', context)


def create_books(request):
    new_book = Book.objects.create(
        title = request.POST['title'],
        description = request.POST['description']
    )

    
    return redirect('/books')

def books(request):
    context = {
        "all_books" : Book.objects.all()
    }

    return render(request, 'index.html', context)

def book_type(request, Book_id):
    context = {
        "one_book" : Book.objects.get(id = Book_id),
        "all_authors" : Author.objects.all()
    }
    return render(request, 'books.html', context)


def manytomany(request):
    book = Book.objects.get(id = request.POST['book_id'])
    author = Author.objects.get(id = request.POST['author'])
    author.Books.add(book)
    
    return redirect(f'books/{book.id}')

def second_manytomany(request):
    book = Book.objects.get(id = request.POST['book_id'])
    author = Author.objects.get(id = request.POST['author_id'])
    author.Books.add(book)

    return redirect(f'authors/{author.id}')