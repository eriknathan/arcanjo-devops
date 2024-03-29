from django.urls import path
from arcanjo import views

app_name = 'arcanjo'

urlpatterns = [
    path('home/', views.index, name='index'),
    path('search/', views.search, name='search'),

    # CRUD
    path('contact/<int:contact_id>/detail/', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),
    path('contact/<int:contact_id>/update/', views.update, name='update'),
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),

    # CRUD - User
    path('user/create/', views.register, name='register'),
    path('', views.login_view, name='login'),
    path('user/logout/', views.logout_view, name='logout'),
    path('user/update/', views.user_update, name='user_update'),
]
