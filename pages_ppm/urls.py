from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    path("company/", views.company_profile, name="company_profile"),
]
