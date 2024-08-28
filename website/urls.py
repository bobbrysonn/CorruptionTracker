from django.urls import path

from . import views

urlpatterns = [
    # ex /
    path("", views.corruption, name="corruption"),

    # ex /kenyas_loans/
    path("kenyas-loans/", views.kenyas_loans, name="kenyas_loans"),

    # ex /land_grabbing/
    path("land-grabbing/", views.land_grabbing, name="land_grabbing"),

    # ex /stalled_projects/
    path("stalled-projects/", views.stalled_projects, name="stalled_projects"),
]
