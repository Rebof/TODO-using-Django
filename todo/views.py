from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Task
# Create your views here.
def addtask(request):
    if request.method == 'POST':
        task_in_views = request.POST['addtask']
        Task.objects.create(task=task_in_views)
        return redirect('homepage')

def mark_as_done(request, pk):
    done_task = get_object_or_404(Task, id=pk)
    done_task.is_completed = True
    done_task.save()
    return redirect('homepage')

def mark_as_undone(request, pk):
    completed_task = get_object_or_404(Task, id=pk)
    completed_task.is_completed = False
    completed_task.save()
    return redirect('homepage')

def update(request, pk):
    get_task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        updated_task_not_html_var= request.POST['updated_task']
        get_task.task = updated_task_not_html_var
        get_task.save()
        return redirect('homepage')
    else:
        context = {
            'getting_task' :  get_task,
        }
    return render(request, 'edit.html', context)

def delete(request, pk):
    delete_task = get_object_or_404(Task, id=pk)
    delete_task.delete()
    #get_task.save()
    return redirect('homepage')