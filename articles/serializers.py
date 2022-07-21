from rest_framework import serializers
from articles.models import Article as ArticleModel


class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = ArticleModel
        fields = "__all__"