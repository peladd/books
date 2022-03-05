from django.db import models

# Create your models here.
class Post(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Age = models.IntegerField()
    bvnumber = models.IntegerField(default=20)

    pass

class Profile(models.Model):
    profile = models.OneToOneField(Post, on_delete=models.CASCADE)
    Address = models.CharField(max_length=300)
    Phone_number = models.IntegerField()
    Email = models.EmailField(max_length=254)

class Product(models.Model):
    product= models.OneToOneField(Post, on_delete=models.CASCADE) 
    name = models.CharField(max_length=50)
    price = models.FloatField()
    des = models.TextField()

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    name = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    
    def __str__(self):
        return f'{self.name.First_name} - {self.name.Last_name}'