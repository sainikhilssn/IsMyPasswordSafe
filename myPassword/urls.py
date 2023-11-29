from django.urls import path 
from .views import * 

urlpatterns = [
       path('home' , home, name = "home"),
       path('name' , get_name , name = "get_name"),
       path('breached_web' , breached_websites , name = 'breached_websites')
]
