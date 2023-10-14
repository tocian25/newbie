from django.contrib import admin
from .models import Post, Book, Author

admin.site.register(Post)
admin.site.register(Book)
admin.site.register(Author)