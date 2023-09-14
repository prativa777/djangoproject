from django.urls import path
from .views import home, test, student, portfolio

urlpatterns=[
    path("test/", test),
    path("temp/", student),
    path('portfolio/', portfolio),
    path("", home), #empty path always at last
     
]