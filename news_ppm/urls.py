from django.urls import path
from news_ppm.views import (article_list, article_detail, category_list, 
                            article_admin_list, article_admin_create, 
                            article_admin_edit, article_admin_delete, 
                            update_stats, article_toggle_publish, article_set_status) 

app_name = "news"

urlpatterns = [
    # Admin URLs
    path("manage/", article_admin_list, name="article_admin_list"),
    path("manage/stats/", update_stats, name="update_stats"),
    path("manage/<int:pk>/status/", article_set_status, name="article_set_status"),

    # Untuk buat artikel baru, edit, hapus
    path("manage/create/", article_admin_create, name="article_admin_create"),
    path("manage/<int:pk>/edit/", article_admin_edit, name="article_admin_edit"),
    path("manage/<int:pk>/delete/", article_admin_delete, name="article_admin_delete"),

    # Untuk toggle publish/unpublish artikel
    path("manage/<int:pk>/toggle/", article_toggle_publish, name="article_toggle_publish"),


    # Publik (bisa dilihat semua orang)
    path("", article_list, name="article_list"),
    path("<int:pk>/", article_detail, name="article_detail"),
]
