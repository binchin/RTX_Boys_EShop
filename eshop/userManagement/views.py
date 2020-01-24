from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    return render(request,'userManagement/login.html')


def confirmLogin(request):
    rusername = request.POST['Username']
    rpass = request.POST['Password']
    user = authenticate(username=rusername, password=rpass)
    if user is not None:
        login(request,user)
        return redirect('/')
    else:
        return render(request,'userManagement/relogin.html')
    

def signUp(request):
    if request.method == 'GET':
        return render(request,'usermanageMent/signup.html')
    else:
        user = User.objects.create_user(username=request.POST['username'],password=request.POST['password'],email=request.POST['email'],first_name)
        user.save()


from django.contrib.auth import authenticate
user = authenticate(username='john', password='secret')
