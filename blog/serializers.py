from rest_framework import serializers

from .models import ArticleModel, TagModel

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = TagModel
        fields = '__all__'


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    tag = TagSerializer(read_only=True, many=True)

    class Meta:
        model = ArticleModel
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }