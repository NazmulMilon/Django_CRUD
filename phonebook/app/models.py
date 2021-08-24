from django.db import models

# Create your models here.

class Contact(models.Model):
    objects = None
    name=models.CharField(max_length=20)
    phone=models.IntegerField()
    work_info=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='image', blank=True)

    def __str__(self):
        return self.name



