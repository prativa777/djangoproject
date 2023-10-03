from django.shortcuts import render, redirect
from tables.models import Student, Product
from crud.models import ClassRoom
from .forms import ClassRoomForm, ClassRoomModelForm

# Create your views here.
def student_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        address = request.POST.get('address')
        bio = request.POST.get('bio')
        Student.objects.create(name=name, email=email, age=age,
                               address=address, bio=bio)
        return redirect ('student')
    return render(request, template_name='forms/student_form.html')



def product_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        Product.objects.create(name=name, price=price, description=description)
        return redirect('product')
    return render(request, template_name='forms/item_form.html')

def classroom(request):
    if request.method == 'POST':
        form = ClassRoomForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            ClassRoom.objects.create(name=name)
            return redirect('forms_classroom')
    form = ClassRoomForm()
    classrooms = ClassRoom.objects.all()
    return render(request, template_name='forms/classroom.html', context={'classrooms':classrooms, 'form':form})

def model_classroom(request):
    if request.method == 'POST':
        form = ClassRoomModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forms_classroom')
    form = ClassRoomModelForm()
    classrooms = ClassRoom.objects.all()
    return render(request, template_name='forms/classroom.html', context={'form':form, 'classrooms':classrooms})