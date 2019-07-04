from django.urls import path, re_path
from tasks import views

app_name = 'tasks'

urlpatterns = [
    path('', views.ListTask.as_view(), name = 'list'),
    path('create/', views.CreateTask.as_view(), name = 'create'),
    path('delete/<int:pk>/', views.DeleteTask.as_view(), name = 'delete'),
]
