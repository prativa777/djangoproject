from django.contrib import admin
from .models import Student, Product, StudentProfile, ProductDetail

# Register your models here.
admin.site.register(Student)

admin.site.register(Product)

admin.site.register(StudentProfile)

admin.site.register(ProductDetail)