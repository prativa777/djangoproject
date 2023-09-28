from django.urls import path
from .views import student_view, product_view

urlpatterns = [
    path('sform/', student_view, name='student-view'),
    path('pform/', product_view, name='product-view')
]