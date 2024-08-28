from django.shortcuts import render

# Create your views here.
def corruption(request):
    return render(request, "website/corruption.html")


def kenyas_loans(request):
    return render(request, "website/kenyas_loans.html")


def land_grabbing(request):
    return render(request, "website/land_grabbing.html")


def stalled_projects(request):
    return render(request, "website/stalled_projects.html")
