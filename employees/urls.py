from django.urls import path
from .views import EmployeeListCreate, EmployeeRetrieveUpdateDestroy, RoleListCreate, RoleRetrieveUpdateDestroy, DashboardStatisticsAPI

urlpatterns = [
    path('employees/', EmployeeListCreate.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroy.as_view(), name='employee-retrieve-update-destroy'),
    path('roles/', RoleListCreate.as_view(), name='role-list-create'),
    path('roles/<int:pk>/', RoleRetrieveUpdateDestroy.as_view(), name='role-retrieve-update-destroy'),
    path('admin/dashboard/', DashboardStatisticsAPI.as_view(), name='admin-dashboard'),
]
