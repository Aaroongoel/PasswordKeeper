from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="pass-home"),
    path('user/',views.user,name="pass-user")
    
]