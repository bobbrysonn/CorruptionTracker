from django.core.paginator import Paginator
from django.shortcuts import render
from .models import CorruptionStory

# Create your views here.
def corruption(request):
    # Get all corruption stories
    corruption_stories = CorruptionStory.objects.all()

    paginator = Paginator(corruption_stories, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "website/corruption.html", { "page_obj": page_obj })


def corruption_detail(request, id):
    corruption_story = CorruptionStory.objects.get(pk=id)

    return render(request, "website/corruption_detail.html", { "corruption_story" : corruption_story })


def kenyas_loans(request):
    return render(request, "website/kenyas_loans.html")


def land_grabbing(request):
    return render(request, "website/land_grabbing.html")


def stalled_projects(request):
    return render(request, "website/stalled_projects.html")
