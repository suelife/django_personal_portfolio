from datetime import timezone
from django.db import models
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField("date published", default=timezone.now)

    def __str__(self):
        return self.title
    