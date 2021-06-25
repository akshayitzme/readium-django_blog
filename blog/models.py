from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length= 255)
    author=models.CharField(max_length= 50)
    image= models.CharField(max_length=2500)
    tags= models.CharField(max_length= 255)
    date= models.DateField(auto_now_add=True)
    content=models.CharField(max_length= 3000)
    readTime=models.IntegerField(default=0)