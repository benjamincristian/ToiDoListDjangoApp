from django.urls import path

from base import views
from base.views import TaskListView

urlpatterns = [
    path('', TaskListView.as_view(), name='tasks')
]
