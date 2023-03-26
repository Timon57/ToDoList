from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm
from django.utils import timezone

# Create your views here.

def task(request):
    tasks = Task.objects.all()
    context = {
        'tasks':tasks
    }
    return render(request,'task/home.html',context)

def addTask(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task_name = form.cleaned_data['task_name']
            description = form.cleaned_data['description']
            date_created = timezone.now
            date_completed = form.cleaned_data['date_completed']
            compeletd = form.cleaned_data['completed']
            task = Task.objects.create(task_name = task_name,description = description, date_created=date_created, date_completed=date_completed,completed=compeletd)
            task.save()
            return redirect('home')

    context = {
        'form':form
    }
    return render(request,'task/addTask.html',context)

def updateTask(request,pk):
    task = Task.objects.get(pk=pk)
    #to display the value in html from
    value = {
            'task_name':task.task_name,
             'description':task.description,
             'date_completed':task.date_completed,
             'completed':task.completed
             }
    form = TaskForm(value)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            #update the value
            task_name = form.cleaned_data['task_name']
            description = form.cleaned_data['description']

            date_completed = form.cleaned_data['date_completed']
            compeletd = form.cleaned_data['completed']
            task = Task(id=task.id,task_name = task_name,description = description, date_created=task.date_created, date_completed=date_completed,completed=compeletd)
            task.save()
            return redirect('home')

    context = {
        'form':form
    }
    return render(request,'task/update.html',context)

def deleteTask(request,pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    return render(request,'task/delete.html')
