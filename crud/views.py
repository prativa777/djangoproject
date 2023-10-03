from django.shortcuts import render, redirect
from .models import ClassRoom, Student, StudentProfile

# Create your views here.
def crud_classroom(request):
    if request.method== 'POST':
        name=request.POST.get('name')
        ClassRoom.objects.create(name=name)
        return redirect('crud-classroom')
    else:
        classrooms= ClassRoom.objects.all()
    return render(request, template_name='crud/classroom.html', context={'classrooms':classrooms, 'title':'classroom'})

def classroom_delete(request, id):
    classroom =ClassRoom.objects.get(id=id)
    if request.method == 'POST':
        classroom.delete()
        return redirect('crud-classroom')
    return render(request, template_name='crud/classroom_delete.html', context={'classroom':classroom})

def classroom_update(request,id):
    classroom= ClassRoom.objects.get(id=id)
    if request.method == 'POST':
        name=request.POST.get('name')
        ClassRoom.objects.filter(id=id).update(name=name)
        return redirect('crud-classroom')
    return render(request, template_name='crud/classroom_update.html', context={'classroom': classroom})

def crud_student(request):
    students = Student.objects.all()
    return render(request, template_name='crud/student.html', context={'students':students, "title":"Student"})

def add_student(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        profile_picture = request.FILES.get('pp')
        classroom_name = request.POST.get('classroom_name')
        classroom = ClassRoom.objects.get(name=classroom_name)
        student = Student.objects.create(name=name, email=email, age=age, classroom=classroom)
        sp = StudentProfile.objects.create(address=address, contact=contact, student=student)
        if profile_picture:
            sp.profile_picture = profile_picture
            sp.save()
        return redirect('crud_student')
    classrooms = ClassRoom.objects.all()
    return render(request, template_name='crud/add_student.html', context={'title':"Add Student", "classrooms":classrooms})

def delete_student(request,id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('add_student')
    return render(request, template_name='crud/delete_student.html', context={'student':student})

def student_detail(request, id):
    student = Student.objects.get(id=id)
    return render(request, template_name='crud/student_detail.html', context={'title':'Student Detail', 'student':student})

def update_student(request,id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        profile_picture = request.FILES.get('pp')
        Student.objects.filter(id=id).update(name=name, email=email, age=age)
        sp, _ = StudentProfile.objects.update_or_create(student=student, defaults={'address':address, 'contact':contact})
        # | tuple unpacking ....it returns two things one object and 'true or false' meaning whether student profile has been created or not
        if profile_picture:
            sp.profile_picture = profile_picture
            sp.save()
        return redirect('crud_student')
    return render(request, template_name='crud/update_student.html', context={'student':student, 'title':'Update Student'})