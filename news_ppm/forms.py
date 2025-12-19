from django import forms
from django.core.exceptions import ValidationError
from .models import NewsArticle

# --- CSS CLASSES ---
BASE_INPUT_CLASS = (
    "w-full rounded-xl border border-slate-300 bg-white px-4 py-2.5 "
    "text-sm text-slate-900 shadow-sm "
    "focus:border-[var(--nav-link-color-active)] focus:outline-none "
    "focus:ring-2 focus:ring-[var(--nav-link-color-active)]/50 "
    "dark:border-slate-600 dark:bg-slate-900 dark:text-slate-100 placeholder-slate-400 transition-all"
)

# Input tanggal ada icon cursor
DATE_INPUT_CLASS = BASE_INPUT_CLASS + " cursor-pointer"

FILE_INPUT_CLASS = (
    "block w-full text-xs text-slate-500 "
    "file:mr-3 file:rounded-full file:border-0 "
    "file:bg-[var(--nav-link-color-active)] file:px-4 file:py-1.5 "
    "file:text-xs file:font-bold file:text-[var(--primary-color)] "
    "hover:file:bg-lime-300 "
    "dark:text-slate-400"
)

CHECKBOX_CLASS = (
    "h-5 w-5 rounded border-slate-300 text-[var(--nav-link-color-active)] "
    "focus:ring-[var(--nav-link-color-active)] dark:border-slate-600 cursor-pointer"
)


class NewsArticleForm(forms.ModelForm):
    class Meta:
        model = NewsArticle
        fields = [
            "title",
            "content",
            "thumbnail",
            "published_at",
            "author",
            "is_published",
        ]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": BASE_INPUT_CLASS,
                    "placeholder": "Masukkan judul artikel...",
                    "required": True 
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": BASE_INPUT_CLASS + " min-h-[12rem]",
                    "rows": 10,
                    "placeholder": "Tulis konten artikel di sini...",
                    "required": True 
                }
            ),
            # --- PERBAIKAN UTAMA DI SINI ---
            "published_at": forms.DateInput(
                attrs={
                    "class": DATE_INPUT_CLASS, 
                    "type": "date"  # Memicu kalender browser
                },
                format="%Y-%m-%d"   # Format WAJIB agar value terbaca oleh input type="date"
            ),
            "author": forms.Select(
                attrs={"class": BASE_INPUT_CLASS}
            ),
            "is_published": forms.CheckboxInput(
                attrs={"class": CHECKBOX_CLASS}
            ),
            "thumbnail": forms.ClearableFileInput(
                attrs={"class": FILE_INPUT_CLASS}
            ),
        }

    # Validasi Ukuran Gambar (Max 100KB)
    def clean_thumbnail(self):
        image = self.cleaned_data.get('thumbnail')
        if image:
            if hasattr(image, 'size'):
                limit_kb = 100
                if image.size > limit_kb * 1024:
                    raise ValidationError(f"Ukuran gambar terlalu besar. Maksimal {limit_kb} KB.")
        return image