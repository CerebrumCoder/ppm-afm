from django import forms
from .models import NewsArticle

# Satu base class untuk semua input text/select
BASE_INPUT_CLASS = (
    "w-full rounded-xl border border-slate-300 bg-white px-3 py-2 "
    "text-sm text-slate-900 shadow-sm "
    "focus:border-[var(--nav-link-color-active)] focus:outline-none "
    "focus:ring-2 focus:ring-[var(--nav-link-color-active)]/50 "
    "dark:border-slate-600 dark:bg-slate-900 dark:text-slate-50 datetime-wrapper"
)

FILE_INPUT_CLASS = (
    "block w-full text-xs text-slate-900 "
    "file:mr-2 file:rounded-full file:border-0 "
    "file:bg-[var(--nav-link-color-active)] file:px-3 file:py-1 "
    "file:text-xs file:font-semibold file:text-[var(--primary-color)] "
    "hover:file:bg-lime-300 "
    "dark:text-slate-50"
)

CHECKBOX_CLASS = (
    "h-4 w-4 rounded border-slate-300 text-[var(--nav-link-color-active)] "
    "focus:ring-[var(--nav-link-color-active)] dark:border-slate-600"
)


class NewsArticleForm(forms.ModelForm):
    # override field published_at supaya widget + format jelas
    published_at = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(
            attrs={
                "type": "datetime-local",
                "class": BASE_INPUT_CLASS + " text-xs js-datetime-input",
            },
            format="%Y-%m-%dT%H:%M",
        ),
        input_formats=["%Y-%m-%dT%H:%M"],
    )

    class Meta:
        model = NewsArticle
        fields = [
            "title",
            "content",
            "thumbnail",
            "thumbnail_url",
            "category",
            "author",
            "is_published",
            "published_at",
        ]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": BASE_INPUT_CLASS}
            ),
            "content": forms.Textarea(
                attrs={
                    "class": BASE_INPUT_CLASS + " min-h-[10rem]",
                    "rows": 10,
                }
            ),
            "category": forms.Select(
                attrs={"class": BASE_INPUT_CLASS}
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
