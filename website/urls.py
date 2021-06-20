from django.urls import path
from . import views

urlpatterns = [
path("", views.home, name="home"),
path("features", views.features, name="features"),
path("casestudies", views.casestudies, name="casestudies"),
path("company", views.company, name="company"),
path("pricing", views.pricing, name="pricing"),
]
