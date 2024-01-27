from django.db import models

# Create your models here.
# TODO: Set delete modes

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    founded_date = models.DateField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateField()
    genre = models.CharField(max_length=50)
    isbn = models.CharField(max_length=13)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    bio = models.TextField()
    books = models.ManyToManyField(Book, blank=True)

    def __str__(self):
        return self.name
