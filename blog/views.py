from django.shortcuts import render
from .models import Book
def books_list(request):
    books = Book.objects.order_by('name')
    return render(request, 'blog/post_list.html', {'books': books})