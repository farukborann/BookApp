from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PublisherViewSet, TagViewSet, BookViewSet, AuthorViewSet

router = DefaultRouter()
router.register(r'publishers', PublisherViewSet)
router.register(r'tags', TagViewSet)
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
