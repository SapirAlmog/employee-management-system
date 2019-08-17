import pandas as pd
from project_functions import (add_employee_manually, add_employee_csv, mark_attendance, delete_employee_manually,
                               delete_employee_from_file, monthly_attendance_report, late_employees_report)

enter_employee_manually = input("Do You want to create a new employee manually? y/n")
if enter_employee_manually == "y":
    add_employee_manually()
else:
    print("No data to enter manually")

enter_employee_from_file = input("Do you want to import employees from a file? y/n")
if enter_employee_from_file == "y":
    add_employee_csv()
else:
    print("No data to enter from a file")

delete_emp_manually = input("Do you want to delete an employee from database? y/n")
if delete_emp_manually == "y":
    delete_employee_manually()

delete_emp_file = input("Do you want to delete an employee from database through a file? y/n")
if delete_emp_file == "y":
    delete_employee_from_file()

show_employees = input("do you want to print out all the employees information? y/n")
if show_employees == "y":
    df = pd.read_csv("/Users/sapir/Documents/python/final project- employee attandance log/emplist.csv", header=None,
                     index_col=0)
    print("Employees Information", df, sep='\n')

employee_arrived = input("Do you want to enter the shift? y/n")
if employee_arrived == "y":
    mark_attendance()

monthly_attendance = input("Do you want to print monthly attendance report?? y/n")
if monthly_attendance == "y":
    monthly_attendance_report()

late_employees = input("Do you want to print late employees attendance report?? y/n")
if late_employees == "y":
    late_employees_report()
