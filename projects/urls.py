from django.urls import path, re_path
from projects import views

app_name = 'projects'

urlpatterns = [
    path('create-project/', views.ProjectCreate.as_view(), name = 'create'),
    path('delete-project/<int:pk>/', views.ProjectDelete.as_view(), name = 'delete'),
    path('update-project/', views.ProjectUpdate.as_view(), name = 'update'),
]
