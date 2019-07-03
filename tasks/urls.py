from django.urls import path, re_path
from tasks import views

app_name = 'tasks'

urlpatterns = [
    path('', views.TasksListView.as_view(), name = 'list'),
]
