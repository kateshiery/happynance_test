from django.shortcuts import render
from django.http import HttpResponse


def index(response):
    return render(response, "website/base.html", {})

def home(response):
    return render(response, "website/home.html", {})

def features(response):
    return render(response, "website/features.html", {})

def casestudies(response):
    return render(response, "website/casestudies.html", {})

def company(response):
    return render(response, "website/company.html", {})

def pricing(response):
    return render(response, "website/pricing.html", {})
