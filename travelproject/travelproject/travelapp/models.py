from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=25)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
class food(models.Model):
    state=models.CharField(max_length=25)
    imge=models.ImageField(upload_to='pics')
    descp=models.TextField()
