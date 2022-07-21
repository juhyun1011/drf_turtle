from django.urls import path
from articles import views


urlpatterns = [
    path('', views.Article.as_view(), name='article_view'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail_view'),
]
