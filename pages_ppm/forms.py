from django import forms
from .models import SiteStats, GalleryPhoto

# Style CSS Admin Custom
BASE_INPUT = "w-full rounded-xl border border-slate-300 bg-white px-4 py-2.5 text-sm text-slate-900 shadow-sm focus:border-[var(--nav-link-color-active)] focus:ring-2 focus:ring-[var(--nav-link-color-active)]/50 dark:border-slate-600 dark:bg-slate-900 dark:text-slate-100"
FILE_INPUT = "block w-full text-xs text-slate-500 file:mr-3 file:rounded-full file:border-0 file:bg-[var(--nav-link-color-active)] file:px-4 file:py-1.5 file:text-xs file:font-bold file:text-[var(--primary-color)] hover:file:bg-lime-300 dark:text-slate-400"

class SiteStatsForm(forms.ModelForm):
    class Meta:
        model = SiteStats
        fields = ["dewan_guru", "mahasiswa", "mahasiswi"]
    # ... (method clean biarkan sama)

# --- FORM GALERI ---
class GalleryPhotoForm(forms.ModelForm):
    class Meta:
        model = GalleryPhoto
        fields = ['title', 'category', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': BASE_INPUT, 'placeholder': 'Judul Foto...'}),
            'category': forms.TextInput(attrs={'class': BASE_INPUT, 'placeholder': 'Contoh: OLAHRAGA'}),
            'description': forms.Textarea(attrs={'class': BASE_INPUT, 'rows': 3}),
            'image': forms.FileInput(attrs={'class': FILE_INPUT}),
        }