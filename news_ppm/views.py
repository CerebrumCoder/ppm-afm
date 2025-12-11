from django.shortcuts import render, get_object_or_404
from .models import NewsArticle, Category


def article_list(request):
    articles = NewsArticle.objects.filter(is_published=True).order_by("-published_at")
    return render(
        request, "article_list.html", 
        {"articles": articles}
    )

def article_detail(request, pk):
    article = get_object_or_404(
        NewsArticle, pk=pk, is_published=True
    )
    return render(request, "article_detail.html", {"article": article})

def category_list(request, slug):
    category = get_object_or_404(Category, slug=slug, is_active=True)
    articles = NewsArticle.objects.filter(
        is_published=True,
        category=category,
    ).order_by("-published_at")
    data = {
            "category": category, 
            "articles": articles,
        },
    return render(
        request,
        "category_list.html",
        data,
    )
