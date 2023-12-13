from django.http import HttpResponse
from django.shortcuts import render
from .forms import ImageLinkForm


def home(request):
    if request.method == "POST":
        imagelink = request.POST.get("imageLink")
        return HttpResponse(f"<h2>ImageLink: {imagelink}</h2>")
    else:
        imagelinkform = ImageLinkForm()
        return render(request, "home.html", {"form": imagelinkform})