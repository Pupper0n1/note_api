from django.db import models

# Create your models here.
class Note(models.Model):
    email = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=1023, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True, auto_now=True)

    def __str__(self):
        return f"{self.email} made {self.title} at {self.date}"