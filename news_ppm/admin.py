from django.contrib import admin
from .models import NewsArticle, Category, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "sort_order")
    list_filter = ("is_active",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(NewsArticle)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "author", "is_published", "published_at")
    list_filter = ("is_published", "category", "author")
    search_fields = ("title", "content")
    raw_id_fields = ("author",)
    date_hierarchy = "published_at"
