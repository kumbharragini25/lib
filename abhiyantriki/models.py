from django.db import models
from tinymce.models import HTMLField
class News5(models.Model):
    news_title=models.CharField(max_length=100,blank=True,null=True)
    news_desc=HTMLField(blank=True,null=True)
    image = models.ImageField(upload_to='images/',blank=True,null=True)
    def __str__(self):
        return self.news_title if self.news_title else self.news_desc
# Create your models here.
