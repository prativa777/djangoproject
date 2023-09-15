from django.urls import path
from .views import main, link


urlpatterns = [
    path('link/', link, name='link'),
    path('', main, name='home'),
]