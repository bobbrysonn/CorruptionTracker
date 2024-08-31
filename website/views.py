from django.shortcuts import render
from .models import CorruptionStory

# Create your views here.
def corruption(request):
    # Get all corruption stories
    corruption_stories = CorruptionStory.objects.all()

    return render(request, "website/corruption.html", {"corruption_stories": corruption_stories})


def kenyas_loans(request):
    return render(request, "website/kenyas_loans.html")


def land_grabbing(request):
    return render(request, "website/land_grabbing.html")


def stalled_projects(request):
    return render(request, "website/stalled_projects.html")
