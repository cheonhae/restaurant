from django.db import models

# Create your models here.
class Restaurant(models.Model):
    region = models.CharField(max_length=1000)
    name = models.CharField(max_length = 200)
    stars = models.IntegerField()
    bestMenu = models.CharField(max_length=200)
    reason = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/%Y/%M/%d', blank=True)
    
    def __str__(self):
        return self.name
    