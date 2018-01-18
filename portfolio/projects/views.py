from django.shortcuts import render
from .models import Project
# Create your views here.
def all_projects(request):
    projects = Project.objects.all()
    title = 'My Projects'
    for project in projects:
        print(project.title)
        print(project.description)
    return render(request, 'projects.html', {"projects":projects, "title":title})
