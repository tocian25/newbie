from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.books_list, name='books_list'),
    path('book/', views.book_detail, name='book_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)