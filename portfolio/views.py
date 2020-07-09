from django.shortcuts import render
from .models import Project, Certificate
# Create your views here.

def home(request):
    projects = Project.objects.all()
    certificates = Certificate.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects, 'certificates':certificates})
