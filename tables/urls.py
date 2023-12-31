from django.urls import path
from .views import student_list, product_list, student_profile, classroom

urlpatterns = [
    path('student/', student_list, name='student'),
    path('profile/', student_profile, name='student-profile'),
    path('product/', product_list, name='product'),
    path('classroom/',classroom, name='class-room')
]