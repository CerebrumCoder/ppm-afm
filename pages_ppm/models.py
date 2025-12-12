from django.db import models


class CompanyProfile(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    vision = models.TextField(blank=True)
    mission = models.TextField(blank=True)
    address = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True)
    logo = models.ImageField(upload_to="logo/", blank=True, null=True)

    def __str__(self):
        return self.name

# Model untuk munculin statistik mahasiswa/i di halaman depan dan di admin
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