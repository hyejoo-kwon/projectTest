from django.db import models

# Create your models here.

class Posts(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50)
    desc = models.CharField(max_length=100)
    content = models.TextField()
