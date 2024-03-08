from django.urls import path
from services import views

app_name = 'services'

urlpatterns = [
    path('project/', views.projects, name='projects'),

    # CRUD
    path('project/<int:project_id>/detail/', views.project, name='project'),
    path('project/create/', views.create_project, name='create'),
    path('project/<int:project_id>/update/', views.update, name='update'),
    path('project/<int:contact_id>/delete/', views.delete, name='delete'),
]
