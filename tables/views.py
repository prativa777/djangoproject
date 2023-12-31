from django.shortcuts import render
from .models import Student, Product, StudentProfile, ClassRoom

# Create your views here.
def student_list(request):
    students= Student.objects.all()
    return render(request, template_name='tables/student.html', context={'students':students})

def student_profile(request):
    student_profiles= StudentProfile.objects.all()
    return render (request, template_name='tables/student_profile.html', context={'profiles': student_profiles})

def product_list(request):
    products= Product.objects.all() 
    return render(request, template_name='tables/product.html', context={'products':products})

def classroom(request):
    students= Student.objects.all()
    classrooms = ClassRoom.objects.all()
    return render(request, template_name='tables/classroom.html', context={'classrooms':classrooms, 'students':students})
    