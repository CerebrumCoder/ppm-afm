from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # status default = "new"
            messages.success(request, "Terima kasih, pesan kamu sudah terkirim.")
            return redirect("contact:contact")
    else:
        form = ContactForm()

    return render(request, "contact/contact.html", {"form": form})
