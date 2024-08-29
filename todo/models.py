from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200, verbose_name="ToDo Title")
    date = models.DateTimeField(default=timezone.now)
    done = models.BooleanField(default=False)
    # image = models.ImageField(upload_to='todo/', null=True, blank=True)

    class Meta:
        ordering = ["title"]
