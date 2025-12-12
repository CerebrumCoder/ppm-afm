from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from .models import NewsArticle, Category
from .forms import NewsArticleForm
from django.utils import timezone


# Untuk update statistik mahasiswa/i di halaman depan PPM AFM
from pages_ppm.models import SiteStats
from pages_ppm.forms import SiteStatsForm
from django.http import JsonResponse, HttpResponseNotAllowed


# Untuk menampilkan daftar artikel berita
def article_list(request):
    articles = NewsArticle.objects.filter(is_published=True).order_by("-published_at")
    return render(
        request, "article_list.html", 
        {"articles": articles}
    )

# Untuk menampilkan detail artikel berita
def article_detail(request, pk):
    article = get_object_or_404(
        NewsArticle, pk=pk, is_published=True
    )
    return render(request, "article_detail.html", {"article": article})

# Untuk menampilkan daftar artikel berdasarkan kategori
def category_list(request, slug):
    category = get_object_or_404(Category, slug=slug, is_active=True)
    articles = NewsArticle.objects.filter(
        is_published=True,
        category=category,
    ).order_by("-published_at")
    data = {
            "category": category, 
            "articles": articles,
        },
    return render(
        request,
        "category_list.html",
        data,
    )

# Untuk bisa masuk sebagai admin, view "admin artikel" dengan UI Tailwind CSS
def staff_required(user):
    return user.is_staff

@login_required
@user_passes_test(staff_required)
def article_admin_list(request):
    articles = NewsArticle.objects.all().order_by("-created_at")

    # objek stats TETAP satu, pk=1
    stats, _ = SiteStats.objects.get_or_create(pk=1)

    # form KOSONG (tidak diisi angka lama)
    stats_form = SiteStatsForm()

    return render(
        request,
        "article_admin_list.html",
        {
            "articles": articles,
            "stats": stats,          # buat ditampilkan "saat ini"
            "stats_form": stats_form # dipakai form POST, tapi kosong di GET
        },
    )

# Untuk bisa membuat artikel
@login_required
def article_admin_create(request):
    if request.method == "POST":
        form = NewsArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            if article.author is None:
                article.author = request.user
            article.save()
            form.save_m2m()
            return redirect("news:article_admin_list")
        
    else:
        form = NewsArticleForm()

    return render(request, "article_admin_form.html", {"form": form, "mode": "create"})

# Untuk bisa edit artikel (hanya admin)
@login_required
def article_admin_edit(request, pk):
    article = get_object_or_404(NewsArticle, pk=pk)
    if request.method == "POST":
        form = NewsArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            if article.author is None:
                article.author = request.user
            article.save()
            form.save_m2m()
            return redirect("news:article_admin_list")
        
    else:
        form = NewsArticleForm(instance=article)

    return render(request, "article_admin_form.html", {"form": form, "mode": "edit", "article": article},)

# Untuk isa menghapus artikel
@login_required
@user_passes_test(staff_required)
def article_admin_delete(request, pk):
    article = get_object_or_404(NewsArticle, pk=pk)
    if request.method == "POST":
        article.delete()
        return redirect("news:article_admin_list")
    return render(request, "article_admin_delete_confirm.html", {"article": article})


# ----- View Untuk Update Statistik Mahasiswa/i PPM AFM di Admin -----
@login_required
@user_passes_test(staff_required)
def article_admin_list(request):
    articles = NewsArticle.objects.all().order_by("-created_at")
    stats, _ = SiteStats.objects.get_or_create(pk=1)
    stats_form = SiteStatsForm(instance=stats)

    data = {
        "articles": articles, 
        "stats_form": stats_form
    }

    return render(
        request,
        "article_admin_list.html", 
        data,
    )

@login_required
@user_passes_test(staff_required)
def update_stats(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    stats, _ = SiteStats.objects.get_or_create(pk=1)
    form = SiteStatsForm(request.POST, instance=stats)

    if form.is_valid():
        form.save()
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse({"ok": True})
        messages.success(request, "Statistik mahasiswa berhasil diperbarui.")
    else:
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse({"ok": False, "errors": form.errors}, status=400)
        messages.error(request, "Gagal menyimpan statistik.")
    return redirect("news:article_admin_list")

# Untuk publish/unpublish artikel secara AJAX
@login_required
@user_passes_test(staff_required)
def article_toggle_publish(request, pk):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    article = get_object_or_404(NewsArticle, pk=pk)
    article.is_published = not article.is_published
    if article.is_published and article.published_at is None:
        article.published_at = timezone.now()
    article.save(update_fields=["is_published", "published_at"])

    label = "Published" if article.is_published else "Draft"
    return JsonResponse({"ok": True, "is_published": article.is_published, "label": label})

# Dropdown status Publish / Draft di admin list
@login_required
@user_passes_test(staff_required)
def article_set_status(request, pk):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    status = request.POST.get("status")
    if status not in ("draft", "published"):
        return JsonResponse({"ok": False, "error": "invalid status"}, status=400)

    article = get_object_or_404(NewsArticle, pk=pk)
    article.is_published = (status == "published")
    if article.is_published and article.published_at is None:
        article.published_at = timezone.now()
    article.save(update_fields=["is_published", "published_at"])

    return JsonResponse({"ok": True})



@login_required
@user_passes_test(staff_required)
def article_admin_delete(request, pk):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    article = get_object_or_404(NewsArticle, pk=pk)
    article.delete()

    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        return JsonResponse({"ok": True})
    return redirect("news:article_admin_list")
