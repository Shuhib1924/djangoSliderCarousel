from django.db import models


class Slider(models.Model):
    picture = models.ImageField(upload_to='images/', blank=True)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
