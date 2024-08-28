from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()
    finished_at = models.DateField(null=True, blank=True)