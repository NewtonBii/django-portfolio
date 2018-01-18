from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    article_image = models.ImageField(upload_to = 'articles/', null = True, blank = True)
    def save_projects(self):
        self.save()
