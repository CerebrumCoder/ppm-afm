from django.urls import path
from news_ppm.views import article_list, article_detail, category_list

app_name = "news"

urlpatterns = [
    path("", article_list, name="article_list"),
    path("category/<slug:slug>/", category_list, name="category_list"),
    path("<slug:slug>/", article_detail, name="article_detail"),
]
