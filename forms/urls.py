from django.urls import path
from .views import student_view, product_view, classroom, model_classroom

urlpatterns = [
    path('sform/', student_view, name='student-view'),
    path('classroom', classroom, name='forms_classroom'),
    path('model-classroom/', model_classroom, name='model_classroom'),
    path('pform/', product_view, name='product-view')
]