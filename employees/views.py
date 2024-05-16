from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Employee, Role
from .serializers import EmployeeSerializer, RoleSerializer



class EmployeeListCreate(generics.ListCreateAPIView):
    """
    List and create employees.

    - GET: Retrieves a list of all employees.
    - POST: Creates a new employee.

    Expected Input for POST Request:
    - 'name' (string): The name of the employee.
    - 'role' (string): The role of the employee.
    - 'status' (boolean): The status of the employee (true for employed, false for fired).

    Expected Output for POST Request:
    - Returns the newly created employee object.
    """
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        queryset = Employee.objects.all()
        search_query = self.request.query_params.get('search', None)
        if search_query is not None:
            queryset = queryset.filter(name__icontains=search_query)
        return queryset
    
    def get(self, request, *args, **kwargs):
        employees = self.get_queryset()
        serializer = self.serializer_class(employees, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        role_name = request.data.get('role')
        role, _ = Role.objects.get_or_create(name=role_name)
        request.data['role'] = role.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class EmployeeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, and delete an employee.

    - GET: Retrieves the details of the specified employee.
    - PUT: Updates the details of the specified employee.
    - DELETE: Deletes the specified employee.
    """
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        queryset = Employee.objects.all()
        return queryset
    
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        role_name = request.data.get('role')
        role, created = Role.objects.get_or_create(name=role_name)
        request.data['role'] = role.id
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "Employee successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
    
class RoleListCreate(generics.ListCreateAPIView):
    """
    List and create roles.

    - GET: Retrieves a list of all roles.
    - POST: Creates a new role.

    Expected Input for POST Request:
    - 'name' (string): The name of the role.

    Expected Output for POST Request:
    - Returns the newly created role object.
    """
    serializer_class = RoleSerializer

    def get_queryset(self):
        return Role.objects.all()

    def get(self, request, *args, **kwargs):
        roles = self.get_queryset()
        serializer = self.serializer_class(roles, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RoleRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, and delete a role.

    - GET: Retrieves the details of the specified role.
    - PUT: Updates the details of the specified role.
    - DELETE: Deletes the specified role.
    """
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "Role successfully deleted"}, status=status.HTTP_204_NO_CONTENT)

class DashboardStatisticsAPI(APIView):
    """
    API endpoint to retrieve statistics for the admin dashboard.

    Provides the total number of employees and total number of roles.

    Methods:
    - GET: Retrieves statistics for the admin dashboard.

    Expected Output:
    - Returns a JSON response with the following keys:
      - 'total_employees': Total number of employees.
      - 'total_roles': Total number of available roles.
    """
    def get(self, request):
        total_employees = Employee.objects.count()
        total_roles = Role.objects.count()
        return Response({
            'total_employees': total_employees,
            'total_roles': total_roles
        })
