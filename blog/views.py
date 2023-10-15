from django.shortcuts import render, get_object_or_404
from .models import Book, Author
def books_list(request):
    books = Book.objects.order_by('name') 
    return render(request, 'blog/books_list.html', {'books': books})

def book_detail(request):  
    books = []
    
    book_id = request.GET.get('pk') 
    if book_id != None:
        print("Book ID:",book_id)
        books = Book.objects.filter(pk=book_id)
        # return render(request, 'blog/book_detail.html', {'books': books})
        
    find_name = request.GET.get('find_name')    
    if find_name != None:
        print("find name:",find_name)
        books = Book.objects.filter(name=find_name)
        # books = get_object_or_404(Book, name=find_name)
    
    find_author = request.GET.get('find_author')    
    if find_author != None:
        print("find author:",find_author)
        authors = Author.objects.filter(lastName=find_author)
        authors = authors.union(Author.objects.filter(middleName=find_author))
        authors = authors.union(Author.objects.filter(firstName=find_author))
        for author in authors: 
            books = Book.objects.filter(author=author)
    
    if len(books)<1:
        # Сделать 404 страницу
        pass
    return render(request, 'blog/book_detail.html', {'books': books})
