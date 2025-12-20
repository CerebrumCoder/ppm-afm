from django.db import models

# Model Statis (Biarkan saja, tidak dipakai di HTML karena hardcode)
class CompanyProfile(models.Model):
    name = models.CharField(max_length=200)
    # ... field lain
    def __str__(self):
        return self.name

class SiteStats(models.Model):
    dewan_guru = models.PositiveIntegerField(default=0)
    mahasiswa = models.PositiveIntegerField(default=0)
    mahasiswi = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Statistik Mahasiswa/i"
        verbose_name_plural = "Statistik Mahasiswa/i"
    
    def __str__(self):
        return "Statistik PPM AFM"
    
    @property
    def total_mahasiswa(self):
        return (self.mahasiswa or 0) + (self.mahasiswi or 0)

# --- [BARU] MODEL GALERI ---
class GalleryPhoto(models.Model):
    title = models.CharField(max_length=100, verbose_name="Judul Kegiatan")
    category = models.CharField(max_length=50, default="KEGIATAN", verbose_name="Kategori (misal: RUTIN)")
    description = models.TextField(blank=True, verbose_name="Deskripsi")
    image = models.ImageField(upload_to='gallery_photos/', verbose_name="Foto")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title