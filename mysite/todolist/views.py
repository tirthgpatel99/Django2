from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required


# from django.urls import reverse
# from django.http import HttpResponseRedirect, HttpResponse
# from django.contrib.auth import authenticate, login, logout
# for login & logout


# Create your views here.
# def todolist(request):
#  return HttpResponse("<h1>Welcome to Task Page</h1>")

# @login_required
# def user_logout(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('index'))


@login_required
def task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, 'Inserted Successfully!!')
        return redirect('todolist:task')
    else:
        all_tasks = Task.objects.all()
        return render(request, 'task.html', context={'all_tasks': all_tasks})

    # context_dict = {'Welcome': "Welcome To Task Page"}
    # all_tasks = Task.objects.all()
    # return render(request, 'task.html', context={'all_tasks': all_tasks})

    # context_dict = {'welcome_task': "Welcome To Task Page"}
    # return render(request, 'task.html', context=context_dict)


def delete_task(request, task_id):
    task_obj = Task.objects.get(pk=task_id)
    task_obj.delete()
    messages.success(request, 'Deleted Successfully!!')
    return redirect('todolist:task')


def insert_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, 'Inserted Successfully!!')
        return redirect('todolist:task')
    else:
        all_tasks = Task.objects.all()
        return render(request, 'insert.html', context={'all_tasks': all_tasks})


def edit_task(request, task_id):
    if request.method == 'POST':
        task_obj = Task.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task_obj)
        if form.is_valid():
            form.save()
        messages.success(request, 'Updated Successfully!!')
        return redirect('todolist:task')
    else:
        task_obj = Task.objects.get(pk=task_id)
        return render(request, 'edit.html', context={'task_obj': task_obj})


def status_task(request, task_id):
    task_obj = Task.objects.get(pk=task_id)
    task_obj.done = not task_obj.done
    task_obj.save()
    return redirect('todolist:task')


def index(request):
    context_dict = {'welcome_home': "Welcome To My Site"}
    return render(request, 'index.html', context=context_dict)


def about(request):
    # context_dict = {'Welcome': "Welcome To About Page"}
    context_dict = {'welcome_about': "Welcome To About Page"}
    return render(request, 'about.html', context=context_dict)
