from django.shortcuts import render

from .models import Task


def tasks_list_pending(request):
    tasks_pending = Task.objects.filter(status='pending')
    return render(request, 'tasks/tasks_pending.html',
                  {'tasks_pending': tasks_pending})
