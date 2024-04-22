from django.db import models

# Create your models here.
class Category(models.Model):
    
    
    name=models.CharField( max_length=50)
    desc=models.CharField( max_length=50,null=True,blank=True)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField( max_length=50)
    quantity=models.IntegerField()
    
    
    def __str__(self):
        return self.name
    
    
class User(models.Model):
    name=models.CharField( max_length=50)
    place=models.CharField( max_length=50)
    age=models.BigIntegerField()
    
    
    def __str__(self):
        return self.name
        
        
        
class Student(models.Model):
    name=models.CharField( max_length=50)
    standard=models.CharField( max_length=50)
    age=models.BigIntegerField()
    
    
    def __str__(self):
        return self.name
        


class ImageTest(models.Model):
    imagename=models.CharField( max_length=50)
    image=models.ImageField(upload_to='Image')
    
    
class Order(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)