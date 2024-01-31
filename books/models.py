from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# TODO: Set delete modes

class Publisher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='publisher')
    name = models.CharField(max_length=100)
    founded_date = models.DateField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='author')
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateField()
    genre = models.CharField(max_length=50)
    isbn = models.CharField(max_length=13, unique=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title
    
class Sale(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book')
    amount = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.book} ({self.amount} pcs.)'