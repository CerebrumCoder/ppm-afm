from django.shortcuts import render
from .models import CompanyProfile


def home(request):
    # kalau butuh data tambahan (misal profil ringkas), bisa kamu ambil di sini
    return render(request, "home.html")


def company_profile(request):
    profile = CompanyProfile.objects.first()
    return render(request, "company_profile.html", {"profile": profile})
