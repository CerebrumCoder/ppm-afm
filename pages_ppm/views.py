
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from .models import CompanyProfile, SiteStats
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Untuk halaman depan dan pass data statistik PPM AFM
from .models import SiteStats

def home(request):
    stats, _ = SiteStats.objects.get_or_create(pk=1)
    return render(request, "home.html", {"stats": stats})


def company_profile(request):
    stats, _ = SiteStats.objects.get_or_create(pk=1)
    profile = CompanyProfile.objects.first()  # kalau kamu punya
    return render(request, "company_profile.html", {
        "stats": stats,
        "profile": profile,
    })

def pengurus_structure(request):
    return render(request, "pengurus_structure.html")

def facilities(request):
    return render(request, "facilities.html")

# Untuk login sebagai admin aja
def afm_login(request):
    # Kalo sudah login dan staff, tidak usah lihat form lagi
    if request.user.is_authenticated and request.user.is_staff:
        return redirect("news:article_admin_list")
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        next_url = request.POST.get("next") or request.GET.get("next")

        user = authenticate(request, username=username, password=password)

        # Optional: hanya izinkan user is_staff yang bisa login ke panel ini
        if user is not None and user.is_staff:
            auth_login(request, user)
            if next_url:
                return redirect(next_url)
            return redirect("news:article_admin_list")
        else:
            messages.error(request, "Username atau password salah, atau Anda tidak memiliki hak akses admin.",)
    
    # GET pertama kali atau kalau gagal login
    return render(request, "auth/login.html")
    
# Untuk logout dari admin
def afm_logout(request):
    auth_logout(request)
    return redirect("pages:home")

@login_required
def afm_change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            # Biar tidak logout setelah ubah password
            update_session_auth_hash(request, user)
            messages.success(request, "Password berhasil diubah.")
            return redirect("news:article_admin_list")
        else:
            # form punya error detail, kita tampilkan di template
            messages.error(request, "Gagal mengubah password. Periksa kembali isian kamu.")
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, "auth/change_password.html", {"form": form})