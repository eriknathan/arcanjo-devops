from django.urls import path
from arcanjo import views

app_name = 'arcanjo'

urlpatterns = [
    path('', views.index, name='index'),
]
