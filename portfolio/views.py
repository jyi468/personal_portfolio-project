from django.shortcuts import render
from .models import Project


# Create your views here.
def home(request):
    # Grab Project objects from the DB. From DB to View
    projects = Project.objects.all()  # Grab all project objects from DB
    return render(request, 'portfolio/home.html', {'projects': projects})
