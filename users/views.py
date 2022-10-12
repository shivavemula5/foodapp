import re
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm

def registration(request):
    if request.method == "POST":
        user_obj = UserCreationForm(request.POST)
        if user_obj.is_valid():
            user_obj.save()
            return thankyou(request)
    else:
        user_obj = UserCreationForm()
    return render(request,'users/registration.html',{'user':user_obj})

def thankyou(request):
    return render(request,'users/thankyou.html',{})