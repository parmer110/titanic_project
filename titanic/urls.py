from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('', views.titanic_list, name='titanic_list'),
    path('passenger/<int:passenger_id>/', views.titanic_detail, name='titanic_detail'),
    path('passenger/new/', views.titanic_create, name='titanic_create'),
    path('passenger/<int:passenger_id>/edit/', views.titanic_update, name='titanic_update'),
    path('passenger/<int:passenger_id>/delete/', views.titanic_delete, name='titanic_delete'),
]
