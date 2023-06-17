from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
  path('search/', views.search, name='search'),
  path('', views.index, name='index'),

  path('contact/<int:contact_id>/update', views.update, name='update'),
  path('contact/<int:contact_id>/delete', views.delete, name='delete'),
  path('contact/<int:contact_id>/', views.contact, name='contact'),
  path('contact/create/', views.create, name='create'),

  path('users/register/', views.register, name='register'),
  path('users/update/', views.user_update, name='user_update'),

  path('users/login/', views.login, name='login'),
  path('users/logout/', views.logout, name='logout'),
]
