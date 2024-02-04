from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Task
# Create your views here.
def addtask(request):
    if request.method == 'POST':
        task_in_views = request.POST['addtask']
        Task.objects.create(task=task_in_views)
        return redirect('homepage')