from rest_framework import viewsets

from .models import TagModel, ArticleModel
from .serializers import ArticleSerializer, TagSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = TagModel.objects.all()
    serializer_class = TagSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = ArticleModel.objects.filter(is_public=True)
    serializer_class = ArticleSerializer
    lookup_field = 'slug'