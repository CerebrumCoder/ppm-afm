from django.urls import path
from pages_ppm import views # Pastikan import views dengan benar

app_name = "pages"

urlpatterns = [
    path("", views.home, name="home"),
    path("tentang-afm/", views.company_profile, name="company_profile"),
    path("struktur-pengurus/", views.pengurus_structure, name="pengurus_structure"),
    path("fasilitas/", views.facilities, name="facilities"),

    # Auth
    path("panel/login/", views.afm_login, name="login"),
    path("panel/logout/", views.afm_logout, name="logout"),
    path("panel/password/", views.afm_change_password, name="change_password"),

    # --- ADMIN GALERI ---
    path("manage/gallery/", views.gallery_admin_list, name="gallery_admin_list"),
    path("manage/gallery/create/", views.gallery_admin_create, name="gallery_admin_create"),
    path("manage/gallery/<int:pk>/delete/", views.gallery_admin_delete, name="gallery_admin_delete"),
]