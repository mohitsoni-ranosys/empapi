from django.db import models
from django.urls import reverse


POSITION_CHOICES = (
    ('ASE', 'Associate Software Engineer'),
    ('SE', 'Software Engineer'),
    ('SSE', 'Senior Software Engineer'),
    ('TL', 'Team Lead'),
    ('SA', 'System Analyst'),
    ('PM', 'Project Manager'),
)

TECH_CHOICES = (
    ('PY', 'Python'),
    ('PHP', 'PHP'),
    ('JAVA', 'Java'),
    ('JS', 'JavaScript'),
)


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.project_name

    def get_absolute_url(self):
        return reverse('emp:project-detail', kwargs={'pk': self.pk})


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=3, choices=POSITION_CHOICES)
    tech = models.CharField(max_length=4, choices=TECH_CHOICES)
    on_projects = models.ManyToManyField(Project)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse('emp:employee-detail', kwargs={'pk': self.pk})


class ProjectManagement(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    project_manager = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='pm')
    developer = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='dev')
    start_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.project + " " + self.project_manager
