from django.shortcuts import render
from django.http import HttpResponse
import pyrebase

config = {
    'apiKey': "AIzaSyDc7g7PwmwBRUjmNlXsBC3c1Y7xQV0vJcU",
    'authDomain': "passkeep-ca3b8.firebaseapp.com",
    'databaseURL': "https://passkeep-ca3b8.firebaseio.com",
    'projectId': "passkeep-ca3b8",
    'storageBucket': "passkeep-ca3b8.appspot.com",
    'messagingSenderId': "643919223115"


}

firebase=pyrebase.initialize_app(config)

auth=firebase.auth()

def home(request):
    #return HttpResponse('<h1>HELO LOLFOL</h1>')
    return render(request,'passkeeper/home.html')

def user(request):
    return render(request,'passkeeper/user.html')

def signin(request):
    return render(request,"user.html")