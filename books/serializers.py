from rest_framework import serializers
from .models import Publisher, Tag, Book, Author

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    publisher = PublisherSerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        model = Author
        fields = '__all__'

        def create(self, validated_data):
            pass
