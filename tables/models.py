from django.db import models

# Create your models here.
# database tabels = models in django

class Student (models.Model):
    name= models.CharField(max_length=20)
    email= models.EmailField()
    age=models.IntegerField()
    address=models.CharField(max_length=20)
    bio=models.TextField()

    def __str__(self):
        return self.name
    
# class Item (models.Model):
#     name = models.CharField(max_length=100)
#     price = models.IntegerField()
#     # color = models.CharField(max_length= 20)
#     description = models.TextField()

class Product (models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    # color = models.CharField(max_length= 20)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class StudentProfile(models.Model):
    student=models.OneToOneField(Student, on_delete=models.CASCADE)
    contact=models.CharField(max_length=100)
    roll_no=models.IntegerField()


class ProductDetail(models.Model):
    product=models.OneToOneField(Product, on_delete=models.CASCADE)
    brand=models.CharField(max_length=50)
    quality=models.CharField(max_length=50)

    def __str__(self):
        return self.brand