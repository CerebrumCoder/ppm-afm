from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse, HttpResponseNotAllowed

from .models import CompanyProfile, SiteStats, GalleryPhoto
from .forms import SiteStatsForm, GalleryPhotoForm

# --- VIEW HALAMAN DEPAN ---

# --- PUBLIC ---
def home(request):
    stats, _ = SiteStats.objects.get_or_create(pk=1)
    return render(request, "home.html", {"stats": stats})

def company_profile(request):
    # Ambil foto dari database
    photos = GalleryPhoto.objects.all().order_by('-created_at')
    
    # Text lain tetap hardcode di HTML, jadi tidak perlu query model CompanyProfile
    return render(request, "company_profile.html", {
        "photos": photos, 
    })

def pengurus_structure(request):
    return render(request, "pengurus_structure.html")

def facilities(request):
    return render(request, "facilities.html")


# --- VIEW ADMIN GALERI (CUSTOM UI) ---

def staff_required(user):
    return user.is_staff

@login_required
@user_passes_test(staff_required)
def gallery_admin_list(request):
    photos = GalleryPhoto.objects.all().order_by('-created_at')
    return render(request, "gallery_admin_list.html", {"photos": photos})

@login_required
@user_passes_test(staff_required)
def gallery_admin_create(request):
    if request.method == "POST":
        form = GalleryPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("pages:gallery_admin_list")
    else:
        form = GalleryPhotoForm()
    return render(request, "gallery_admin_form.html", {"form": form})

@login_required
@user_passes_test(staff_required)
def gallery_admin_delete(request, pk):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    photo = get_object_or_404(GalleryPhoto, pk=pk)
    photo.delete()
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        return JsonResponse({"ok": True})
    return redirect("pages:gallery_admin_list")


# --- AUTHENTICATION (Kode Lama Anda) ---
def afm_login(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect("news:article_admin_list")
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            auth_login(request, user)
            next_url = request.POST.get("next") or request.GET.get("next")
            return redirect(next_url or "news:article_admin_list")
        else:
            messages.error(request, "Username atau password salah.")
    
    return render(request, "auth/login.html")
    
def afm_logout(request):
    auth_logout(request)
    return redirect("pages:home")

@login_required
def afm_change_password(request):
    # ... (kode lama biarkan saja)
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password berhasil diubah.")
            return redirect("news:article_admin_list")
        else:
            messages.error(request, "Gagal mengubah password.")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, "auth/change_password.html", {"form": form})