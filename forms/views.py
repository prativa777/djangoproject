from django.shortcuts import render, redirect
from tables.models import Student, Product

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

        