from django.test import TestCase
from .models import Project

# Create your tests here.
class ProjectTestClass(TestCase):

    def setUp(self):
        self.project = Project(title='twitfluence', description='It calculates the twitter score of users')

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))

    def test_save_projects(self):
        self.project.save_projects()
        projects = Project.objects.all()
        self.assertTrue(len(projects)>0)

    def tearDown(self):
        self.project.save_projects()
        Project.objects.all().delete()
