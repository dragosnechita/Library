from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_librarian = models.BooleanField(default=False)

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    loaned = models.CharField(max_length=200, default='available')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return redirect('view_book', kwargs={'pk': self.pk})

    def borrow_book(self):
        # to be implemented
        pass

