from rest_framework import viewsets

from .models import TagModel, ArticleModel
from .permissions import IsAdminOrReadOnly
from .serializers import ArticleSerializer, TagSerializer
from .paginations import CustomPagination

class TagViewSet(viewsets.ModelViewSet):
    queryset = TagModel.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAdminOrReadOnly, )


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = ArticleModel.objects.filter(is_public=True)
    serializer_class = ArticleSerializer
    permission_classes = (IsAdminOrReadOnly, )
    pagination_class = CustomPagination
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = super().get_queryset()

        tag = self.request.query_params.get('tag', None)
        if tag:
            queryset = queryset.filter(tag=tag)
        
        return queryset