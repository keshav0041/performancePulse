from django.urls import path
from home import views

urlpatterns = [
    path('home', views.home,name='home'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('registration',views.registration,name='registration'),
    path('',views.fileupload,name='fileupload'),



  
]