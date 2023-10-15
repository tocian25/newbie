from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import AbstractUser, Group
from django.contrib.auth.views import RegistrationView, LoginView
from django.db import models
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, UpdateView, DeleteView


class UserLoginView(LoginView):
    template_name = 'registration/login.html'


class User(AbstractUser):
    Name = models.CharField(max_length=200)
    dateOfBirth = models.DateField()
    groups = models.ManyToManyField(Group, related_name='blog_users')
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='blog_user_set'  # Здесь указывается уникальное имя для обратного доступа
    )


pass


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=2000)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Author(models.Model):
    firstName = models.CharField(max_length=200)
    middleName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    dateOfBirth = models.DateField()
    biography = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.lastName + " " + self.firstName + " " + self.middleName


class Book(models.Model):
    name = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    # author = models.TextField()
    published_date = models.DateField()
    sammari = models.TextField()
    cover = models.ImageField(upload_to='book_cover')

    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'genre']
    success_url = reverse_lazy('book_list')


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'genre']
    success_url = reverse_lazy('book_list')

    def test_func(self):
        book = self.get_object()
        return self.request.user == book.author or self.request.user.is_superuser


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')

    def test_func(self):
        book = self.get_object()
        return self.request.user == book.author or self.request.user.is_superuser


class UserRegistrationView(RegistrationView):
    template_name = 'registration/register.html'
