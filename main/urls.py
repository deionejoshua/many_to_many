from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('authors', views.authors),
    path('create_authors', views.create_authors),
    path('authors/<int:Author_id>', views.writer),
    path('create_books', views.create_books),
    path('books', views.books),
    path('books/<int:Book_id>', views.book_type),
    path('manytomany', views.manytomany),
    path('second_manytomany', views.second_manytomany)
    
    

]