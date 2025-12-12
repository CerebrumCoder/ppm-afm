from django.urls import path
from pages_ppm.views import home, company_profile, pengurus_structure, facilities

app_name = "pages"

urlpatterns = [
    path("", home, name="home"),
    path("tentang-afm/", company_profile, name="company_profile"),
    path("struktur-pengurus/", pengurus_structure, name="pengurus_structure"),
    path("fasilitas/", facilities, name="facilities"),

]
