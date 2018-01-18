from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=30)
    web_link  = models.CharField(max_length=50, null=True)
    repo_link = models.CharField(max_length=50, null=True)
    description = models.TextField()
    project_image = models.ImageField(upload_to = 'projects/', null=True)

    def save_projects(self):
        self.save()
