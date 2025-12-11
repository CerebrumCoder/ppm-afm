from django.urls import path
from pages_ppm.views import home, company_profile

app_name = "pages"

urlpatterns = [
    path("", home, name="home"),
    path("company/", company_profile, name="company_profile"),
]
