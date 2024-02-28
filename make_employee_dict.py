# Author: Michelle Frugia
# GitHub username: frugiam
# Date: 02/28/2024
# Description: Project 8c

class Employee:
    def __init__(self, name, ID_number, salary, email_address):
        self.name = name
        self.ID_number = ID_number
        self.salary = salary
        self.email_address = email_address

def make_employee_dict(names, ID_numbers, salaries, email_addresses):
    employees = {}
    for i in range(len(names)):
        employee = Employee(names[i], ID_numbers[i], salaries[i], email_addresses[i])
        employees[employee.ID_number] = employee
    return employees