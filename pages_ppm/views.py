from django.shortcuts import render
from .models import CompanyProfile


def company_profile(request):
    profile = CompanyProfile.objects.first()
    return render(request, "pages/company_profile.html", {"profile": profile})
