from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('blog/', blog, name="blog"),
    path('career/', career, name="career"),
    path('blog/article-<str:article_number>/', article, name="article"),
]
