from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    image = models.ImageField(upload_to='team/')
    facebook = models.URLField(null=True)
    twitter = models.URLField(null=True)
    instagram = models.URLField(null=True)

    def __str__(self):
        return self.name
