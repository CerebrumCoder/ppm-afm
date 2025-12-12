from django import forms
from .models import SiteStats

class SiteStatsForm(forms.ModelForm):
    class Meta:
        model = SiteStats
        fields = ["dewan_guru", "mahasiswa", "mahasiswi"]

    def _clean_int_or_zero(self, name):
        value = self.cleaned_data.get(name)
        if value is None:
            return 0
        if value < 0:
            raise forms.ValidationError("Tidak boleh negatif.")
        return value

    def clean_dewan_guru(self):
        return self._clean_int_or_zero("dewan_guru")

    def clean_mahasiswa(self):
        return self._clean_int_or_zero("mahasiswa")

    def clean_mahasiswi(self):
        return self._clean_int_or_zero("mahasiswi")
