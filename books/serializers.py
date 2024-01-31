from rest_framework import serializers
from .models import Publisher, Tag, Book, Author, Sale

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Publisher
        fields='__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields='__all__'

class BookSerializer(serializers.ModelSerializer):
    authors = serializers.StringRelatedField(many=True)
    class Meta:
        model=Book
        fields='__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields='__all__'

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sale
        fields='__all__'
