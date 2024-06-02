from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('office/create/', views.create_office, name='create_office'),
    path('office/update/<int:id>/', views.update_office, name='update_office'),
    path('office/delete/<int:id>/', views.delete_office, name='delete_office'),
    path('office/list/', views.office_list, name='office_list'),
    path('doctor/delete/<int:id>/', views.delete_doctor, name='delete_doctor'),
]
