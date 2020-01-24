from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

# Create your views here.
def login(request):
    return render(request,'userManagement/login.html')


def confirmLogin(request):
    rusername = request.POST['Username']
    rpass = request.POST['Password']
    user = authenticate(username=rusername, password=rpass)
    if user is not None:
        return redirect('/')
    else:
        return render(request,'userManagement/relogin.html')
    

def signUp(request):
    pass

def confirm(signup):
    pass

from django.contrib.auth import authenticate
user = authenticate(username='john', password='secret')
