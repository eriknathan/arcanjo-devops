from django.urls import path
from arcanjo import views

app_name = 'arcanjo'

urlpatterns = [
    path('<int:contact_id>/', views.contact, name='contact'),
    path('', views.index, name='index'),
]
