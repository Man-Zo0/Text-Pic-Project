from django.db import models
from django.db import models

# Create your models here.
class Images(models.Model):
    img_url = models.CharField(max_length=400)
    posx = models.CharField(max_length=100)
    posy = models.CharField(max_length=100)
    start_size = models.CharField(max_length=100)
    max_width = models.CharField(max_length=100)
    font_family = models.CharField(max_length=100)
    rotate = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    alpha = models.CharField(max_length=100)