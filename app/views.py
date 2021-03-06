from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


def index(request):
    tasks = Task.objects.all()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    form = TaskForm()
    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/task_list.html', context)


def updateTask(request, key):
    task = Task.objects.get(id=key)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'tasks/task_update.html', context)


def deleteTask(request, key):
    item = Task.objects.get(id=key)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'tasks/task_delete.html', context)
