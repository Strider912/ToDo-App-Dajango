from django.shortcuts import render,HttpResponse, redirect,HttpResponseRedirect
from users_app.form import CustomRegisterForm
from django.contrib import messages
# Create your views here.

def register(request):

    if request.method=='POST':
        register=CustomRegisterForm(request.POST)
        if register.is_valid():
            print('hello ---------------------------------')
            register.save()
            messages.success(request,('New user account is created'))
        return HttpResponseRedirect('register')         

    else:
        register=CustomRegisterForm()
        context={
            'register':register
        }
        return render(request,'register.html', context)
