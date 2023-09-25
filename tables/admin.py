from django.contrib import admin
from .models import Student, Product, StudentProfile, ProductDetail, ClassRoom, Publication, Article

# Register your models here.
admin.site.register(Student)

admin.site.register(Product)

admin.site.register(StudentProfile)

admin.site.register(ProductDetail)

admin.site.register(ClassRoom)

admin.site.register(Publication)

admin.site.register(Article)