from django.db import models
class myhome(models.Model):
    title=models.CharField(max_length=100,blank=True,null=True)
    image = models.ImageField(upload_to='images/',blank=True,null=True)
    # def __str__(self):
    #     return self.title if self.title
# Create your models here.
