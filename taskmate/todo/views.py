from django.shortcuts import render,HttpResponse,redirect
from todo.models import TaskList
from todo.form import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/account/login')
def index(request):
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save(commit=False).manager = request.user
            form.save()
            messages.success(request,('New Task is Added')) 
            return redirect('/todo')
    else:

        data= TaskList.objects.filter(manager = request.user)
        paginator=Paginator(data,2)
        page=request.GET.get('pg')
        data=paginator.get_page(page)
        
    context={
            'data': data
        }
    return render(request,'index.html' , context )

def about(request):                                                                                                                                                     
    return render(request,'about.html' ,{} )

def indexes(request):
    context={
        'data':" welcome to index  pages"
    }
    return render(request,'indexes.html' , context )


def contact(request):
    return render(request,'contact.html' ,{} )

def delete(request, task_id):
    task=TaskList.objects.get(pk=task_id)
    if task.manager==request.user:
        task.delete()
    else:
        messages.error(request,('Access Restricted,You are not allowed '))    
    return redirect('/todo')

def complete(request, task_id):
    task=TaskList.objects.get(pk=task_id)
    if task.manager==request.user:
        task.done = True    
        task.save()
    else:
        messages.error(request,("Access Restricted, You are not allowed"))   
    return redirect('/todo')

def pending(request, task_id):
    task=TaskList.objects.get(pk=task_id)   
    if task.manager==request.user:
        task.done = False    
        task.save()
    else:
        messages.error(request,("Access Restricted, You are not allowed"))   
    return redirect('/todo')

def edit(request, task_id):
    if request.method=='POST':
        task=TaskList.objects.get(pk=task_id)
        form=TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success=(request,('Edited successfully'))
            return redirect('/todo')

    else:
        
        task=TaskList.objects.get(pk=task_id)

        context={
            'task': task
        }
    return render(request,'edit.html', context)




