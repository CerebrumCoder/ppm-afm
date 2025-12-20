from django.contrib import admin
from .models import CompanyProfile, SiteStats, GalleryPhoto

# --- Admin CompanyProfile (Perbaikan: Hapus 'email') ---
@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Cukup tampilkan Nama saja

# --- Admin Statistik ---
@admin.register(SiteStats)
class SiteStatsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'total_mahasiswa', 'dewan_guru')

# --- Admin Galeri ---
@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    search_fields = ('title', 'category')
    list_filter = ('created_at',)