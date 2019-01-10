from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.authtoken import views
from .views import (
    EmployeeListView,
    EmployeeCreateView,
    EmployeeDetailView,
    ProjectListView,
    ProjectAddView,
    ProjectDetailView,
    ProjectAssignView,
    # emp_list,
    # emp_detail,
    EmpList,
    EmpDetail,
    UserCreate,
    LoginView,
    )

app_name = 'emp'

urlpatterns = [
    path('all/', EmployeeListView.as_view(), name='employee-list'),
    path('create/', EmployeeCreateView.as_view(), name='employee-create'),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('addproject/', ProjectAddView.as_view(), name='project-create'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('assignproject/', ProjectAssignView.as_view(), name='project-assign'),
    # path('emp_list', emp_list, name='emp_list'),
    path('emp_list', EmpList.as_view(), name='emp_list'),
    # path('emp_detail/<int:pk>/', emp_detail, name='emp_detail'),
    path('emp_detail/<int:pk>/', EmpDetail.as_view(), name='emp_detail'),
    path('users/', UserCreate.as_view(), name='user_create'),
    path('login/', LoginView.as_view(), name='login'),
    path('login2/', views.obtain_auth_token, name='login2'),
]
