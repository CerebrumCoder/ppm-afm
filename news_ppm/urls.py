from django.urls import path
from news_ppm.views import article_list, article_detail, category_list

app_name = "news"

urlpatterns = [
    path("", article_list, name="article_list"),
    path("<int:pk>/", article_detail, name="article_detail"),
]
