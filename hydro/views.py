from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
def index(request):

    return render(request,'hydro/index.html')

def contact(request):

    return render(request,'hydro/contact.html')    

def ourwork(request):

    return render(request,'hydro/ourwork.html')  
  
def projects(request):

    return render(request,'hydro/projects.html')   

def testimonials(request):

    return render(request,'hydro/testimonials.html')  

def login(request):

    return render(request,'registration/login.html')  
    
def dashboard(request):

    return render(request,'hydro/dashboard.html')  
def register(request):
    if request.method == 'POST':
        form =  UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user = authenticate(username=username, password = password)
            login(request,user)
            return redirect('dashboard')     
    else:
        form = UserCreationForm()

    ctx = {'form' : form}
    return render(request,'registration/register.html',ctx)    

