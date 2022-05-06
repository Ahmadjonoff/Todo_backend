from django.contrib.auth.models import User
from django.db import models

class Plan(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=(("yangi", "yangi"), ("bajarildi", "bajarildi")))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title