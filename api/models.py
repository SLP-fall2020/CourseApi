from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=32)
    name = models.CharField(max_length=32, default="")
    notes = models.TextField(max_length=360)












