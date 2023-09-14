from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
#     content="""
# <h1> Hello World! </h1>
# <h2> I am learning python. </h2>
#     """ i did not understand

    # return HttpResponse("Hello World!") 

    # another way to render actual html content

    table_heading= "Student Information"
    peoples_info= [
        {"first_name": "Prativa", "last_name":"Chhantyal", "address":"Kathmandu"},
        {"first_name": "Aasha", "last_name":"Basnet", "address":"Kathmandu"},
        {"first_name": "Neeza", "last_name":"Shrestha", "address":"Sarlahi"},
    ]

    return render(request, template_name='home.html', context={"heading": table_heading, "infos":peoples_info})

def test(request):
    name = request.GET.get("name")
    print(name)
    age= request.GET.get("age")
    
    # We can send query strings/ query parameters in the urls 
    # Everything sent after "?" in the url is querystring
    # Query strings can be multiple and are seperated by ampersand(&).
    return HttpResponse(f"My name is {name}. I'm {age}")

def student(request):
    return render (request, template_name='student.html')

def portfolio(request):
    return render(request, template_name='portfolio.html')