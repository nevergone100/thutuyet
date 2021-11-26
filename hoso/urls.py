from django.urls import path
from hoso.views import *


app_name = 'hoso'
urlpatterns = [
    path('', index, name='index'),
    
]
