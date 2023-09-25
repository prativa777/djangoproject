from django.db import models

# Create your models here.
# database tabels = models in django

class ClassRoom (models.Model):
    name= models.CharField(max_length=20)

class Student (models.Model):
    name= models.CharField(max_length=20)
    email= models.EmailField()
    age=models.IntegerField()
    address=models.CharField(max_length=20)
    bio=models.TextField()
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, 
                                  related_name="classroom_students", null=True, blank=True)

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
    
class Publication(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title
    
class Article(models.Model):
    headline=models.CharField(max_length=20)
    publication = models.ManyToManyField(Publication)

    def __str__(self):
        return self.headline