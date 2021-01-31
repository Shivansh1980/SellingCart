from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login, logout
from .forms import CreateUserForm

# Create your views here.
def registration_form(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        print('working')
        if form.is_valid():
            form.save()
            return redirect('login')
        else :
            print("Form is not valid")
    else:
        form = CreateUserForm()
    return render(request ,'accounts/registration.html',{'form':form})

def login_form(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if(user is not None):
            login(request,user)
            return redirect('ShopHome')
    return render(request, 'accounts/login.html')

def logout_file(request):
    logout(request)
    return redirect('ShopHome')
