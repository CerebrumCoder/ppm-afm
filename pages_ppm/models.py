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
