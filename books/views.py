from .models import Publisher, Tag, Book, Author, Sale
from .serializers import PublisherSerializer, TagSerializer, BookSerializer, AuthorSerializer
from .serializers import PublisherSerializer, AuthorSerializer, SaleSerializer
from .permissions import HasSaleAccess, HasAuthorAccess, HasBookAccess

from rest_framework import generics, status, permissions
from rest_framework.response import Response

class Publishers(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [permissions.IsAdminUser]

class Authors(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [HasAuthorAccess]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class Sales(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [HasSaleAccess]

# class PublishersAPIView(generics.ListCreateAPIView):
#     queryset = Publisher.objects.all()
#     serializer_class = PublisherSerializer

class PublisherDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class Tags(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = TagSerializer


class Books(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [HasBookAccess]

class BookDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [HasBookAccess]

# class AuthorsAPIView(generics.ListCreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

class AuthorDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer