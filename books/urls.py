from django.urls import path
from . import views

urlpatterns = [
    path('publishers', views.Publishers.as_view(), name='publishers'),
    path('publishers/<int:pk>', views.PublisherDetails.as_view(), name='publisher-details'),
    path('tags', views.Tags.as_view(), name='tags'),
    path('tags/<int:pk>', views.TagDetails.as_view(), name='tag-details'),
    path('books', views.Books.as_view(), name='books'),
    path('books/<int:pk>', views.BookDetails.as_view(), name='book-details'),
    path('authors', views.Authors.as_view(), name='authors'),
    path('authors/<int:pk>', views.AuthorDetails.as_view(), name='author-details'),
]
