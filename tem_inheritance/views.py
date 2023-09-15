from django.shortcuts import render

# Create your views here.
def main(request):
    people = [
        {"name": "John", "age": 30, "address": "KTM"},
        {"name": "Alex", "age": 20, "address": "PKR"},
        {"name": "Anne", "age": 17, "address": "BTL"},

    ]
    return render(request, template_name='tem_inheritance/home.html', context={'people': people})

# ANOTHER WAY TO USE CONTEXT
# context={'peoples':people}
# return render(request, template_name='tem_inheritance/home.html', context={'people': people}, context=context)

def link(request):
    links=[
        {"facebook": "sdkjkl", "email":"asd@gmail.com"},
        {"facebook": "sdfvbk", "email":"sdf@gmail.com"},

    ]
    return render(request, template_name='tem_inheritance/link.html', context={"links":links})