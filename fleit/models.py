from django.db import models


# Create your models here.
class Destination(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='destination_images')
    description = models.CharField(max_length=200, default='Visit today.')

    def __str__(self):
        return str(self.city) + ', ' + str(self.state)

