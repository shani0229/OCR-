from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index, name='index'),
    # path('ex1', views.ex1, name='ex1'),
    # path('index', views.index, name='index'),
    
  
]

