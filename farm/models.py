from django.db import models
class farm(models.Model):
    Description=models.CharField(max_length=2000)
    image=models.ImageField(upload_to='images2/')

    def __str__(self):
         return self.Description
# Create your models here.
    