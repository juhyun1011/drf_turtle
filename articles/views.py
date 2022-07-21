from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from articles import serializers
from articles.serializers import ArticleSerializer
from articles.models import Article as ArticleModel

# Create your views here.

class Article(APIView):
    def get(self, request):
        articles = ArticleModel.objects.all()
        serializer = ArticleSerializer(articles, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)

    def post(self, request):
        if not request.user.is_authenticated:
            return Response({"message":"로그인 해주세요"}, 401)
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"글 작성 완료!!"})
        else:
            return Response({"message":f'${serializer.errors}'}, 400)


class ArticleDetailView(APIView):
    def get(self, request, pk):
        article = ArticleModel.objects.get(pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    