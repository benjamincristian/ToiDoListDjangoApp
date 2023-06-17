from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from base.models import Task


class TaskListView(ListView):
    model = Task
    context_object_name = 'all_tasks'


