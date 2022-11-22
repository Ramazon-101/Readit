from rest_framework import serializers
from ..models import Article


class ArticleGEtSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.title', read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'category_id', 'category_name', 'title', 'get_image_url', 'content', 'tag', 'slug',
                  'created_at']


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'category', 'title', 'image', 'content', 'tag', 'slug', 'created_at']
        extra_kwargs = {
            'views': {'read_only': True}

        }
