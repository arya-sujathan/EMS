# Employee Management System

A web-based Employee Management System built with Django, allowing CRUD operations on employee records, role assignment, searching, and status updates. Includes an admin dashboard for managing employees and roles.

## Features

- CRUD operations on employee records
- Role assignment (manager, developer, design, scrum master)
- Search functionality by name and ID
- Admin dashboard to manage employees and roles
- Status updates (employed or fired)

## Installation

1. Clone the repository:

git clone https://github.com/your_username/employee-management-system.git


2. Install dependencies:

pip install -r requirements.txt

3. Run migrations:

python manage.py migrate

4. Create a superuser:

python manage.py createsuperuser

5. Start the development server:

python manage.py runserver


## API Documentation

Employee CRUD Operations
1. Create Employee

    URL: /api/employees/
    Method: POST
    Expected Params:
        'name' (string)
        'role' (string) [manager, developer, design, scrum master]
        'status' (boolean) [true for employed, false for fired]
    Sample Request:

        {
            "name": "John Doe",
            "role": "developer",
            "status": true
        }

    Expected Output:
        Returns the newly created employee object.

2. Read Employee List

    URL: /api/employees/
    Method: GET
    Expected Output:
        Returns a list of all employee objects.

3. Read Employee Detail

    URL: /api/employees/<employee_id>/
    Method: GET
    Expected Output:
        Returns the details of the specified employee.

4. Update Employee

    URL: /api/employees/<employee_id>/
    Method: PUT
    Expected Params:
        'name' (string)
        'role' (string) [manager, developer, design, scrum master]
        'status' (boolean) [true for employed, false for fired]
    Sample Request:
        {
            "name": "Jane Doe",
            "role": "manager",
            "status": true
        }
    Expected Output:
        Returns the updated employee object.
5. Delete Employee

    URL: /api/employees/<employee_id>/
    Method: DELETE
    Expected Output:
        Returns status code 204 (No Content) on successful deletion.


## Role Operations

1. Assign Role to Employee

    URL: /api/roles/
    Method: POST
    Expected Params:
        'name' (string)
    Sample Request:

        {
            "name": "developer"
        }
    Expected Output:
        Returns the newly created role object.

2. List All Roles

    URL: /api/roles/
    Method: GET
    Expected Output:
        Returns a list of all roles.


## Search Functionality

1. Search Employees by Name

    URL: /api/employees/?search=<search_query>
    Method: GET
    Expected Output:
        Returns a list of employees matching the search query.

2. Search Employee by ID

    URL: /api/employees/<employee_id>/
    Method: GET
    Expected Output:
        Returns the details of the specified employee.

