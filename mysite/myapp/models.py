from django.db import models

# Create your models here.
class Band(models.Model):
    app_label='myapp'
    name = models.fields.CharField(max_length=100)