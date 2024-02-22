from django.db import models

# Create your models here.
class Teachers(models.Model):
    name=models.CharField(max_length=80)
    image = models.ImageField(upload_to="media")
    roll=models.CharField(max_length=80)
    face_book=models.CharField(max_length=200)
    instagram=models.CharField(max_length=200)
    twitter=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Classes(models.Model):
    titel=models.CharField(max_length=100)
    image = models.ImageField(upload_to="media")
    user_image = models.ImageField(upload_to="media")
    teac_name=models.CharField(max_length=100)
    position=models.CharField(max_length=100)
    time=models.CharField(max_length=100)
    Capacity=models.CharField(max_length=100)

    def __str__(self):
        return self.titel


class Blog(models.Model):
    blog=models.TextField()
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="media")
    Profession=models.CharField(max_length=50)




    