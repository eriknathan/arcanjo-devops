from django.urls import path
from services import views

app_name = 'services'

urlpatterns = [
    path('project/', views.projects, name='projects'),

    # CRUD
    # path('contact/<int:contact_id>/detail/', views.contact, name='contact'),
    path('project/create/', views.create_project, name='create'),
    # path('contact/<int:contact_id>/update/', views.update, name='update'),
    # path('contact/<int:contact_id>/delete/', views.delete, name='delete'),
]
