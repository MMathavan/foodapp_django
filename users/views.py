from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm     #inbuilt user registration form
from django.contrib import messages                        #is for success message
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required      #decotator for profile page

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():     #is also check the username is not in duplicate..
            form.save()
            username = form.cleaned_data.get('username') #for displaying the name in the success message
            messages.success(request,f'Welcome {username}, your account is created Successfully!')
            return redirect("login")
    else:
        form = RegisterForm()               #in-built user registration form we don't create any forms
    return render(request,'users/register.html',{'form':form})

@login_required                #-----> if the user is particularly logged in so that we see the profile page... it is for only register and login users pages
def profilepage(request):
    return render(request,'users/profile.html')
