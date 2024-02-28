# Author: Michelle Frugia
# GitHub username: frugiam
# Date: 02/28/2024
# Description: Project 8c

# Define a class named Employee
class Employee:

    # Define an init method that takes four values and assigns them to the data members
    def __init__(self, name, ID_number, salary, email_address):

        # Use self to refer to the instance attributes
        self.__name = name # Private attribute for name
        self.__ID_number = ID_number # Private attribute for ID number
        self.__salary = salary # Private attribute for salary
        self.__email_address = email_address # Private attribute for email address

    # Define four get methods that return the values of the data members
    def get_name(self):

        return self.__name

    def get_ID_number(self):

        return self.__ID_number

    def get_salary(self):

        return self.__salary

    def get_email_address(self):

        return self.__email_address

# Define a function named make_employee_dict that takes four lists as parameters
def make_employee_dict(names, ID_numbers, salaries, email_addresses):

    # Initialize an empty dictionary named emp_dict
    emp_dict = {}

    # Use a for loop to iterate over the range of the length of any of the lists
    for i in range(len(names)):

        # Create an Employee object using the corresponding values from the four lists as arguments
        emp = Employee(names[i], ID_numbers[i], salaries[i], email_addresses[i])

        # Add the Employee object to the emp_dict with the ID_number as the key and the object as the value
        emp_dict[ID_numbers[i]] = emp

    # Return the emp_dict after the loop ends
    return emp_dict
