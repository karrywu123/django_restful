from rest_framework import serializers
from .models import Article, Category, Tag

# 模型序列化
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = ('id', 'vum', 'content', 'title')
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = ('id', 'vum', 'content', 'title')
        fields = '__all__'