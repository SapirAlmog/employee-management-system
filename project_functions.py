"""============= ADD EMPLOYEES MANUALLY============="""
import pandas as pd

""" 
This function gets employee's information (ID, Name, Phone number, Age) as an input from the user, and saves it into
pandas data frame
"""


def add_employee_manually():
    input_id = input("Enter employee's ID :")
    if input_id.isdigit():
        print("User ID is Number ")
    else:
        print("User ID is invalid ")
        return
    employee_id = input_id
    employee_name = input("Enter employee's name :")
    employee_phone = input("Enter employee's phone number :")
    employee_age = input("Enter employee's age :")
    df = pd.DataFrame(data=[[employee_id, employee_name, employee_phone, employee_age]],
                      columns=["ID", "Name", "Phone", "Age"])
    with open('/Users/sapir/Documents/python/final project- employee attandance log/emplist.csv', 'a') as f:
        df.to_csv(f, header=False, index=False)
    return df


add_employee_manually()

"""============= ADD EMPLOYEES FROM FILE============="""
import pandas as pd

""" 
This function gets employee's information. The user can enter a file path which contains data of employees to add to the 
employees file- "emplist.csv".
"""


def add_employee_csv():
    try:
        path = input(" Enter a file path which contains data of employees to add to the employees file:")
        colnames = ['ID', 'Name', 'Phone', 'Age']
        df = pd.read_csv(path, names=colnames, header=None, index_col=0)
        # Add to employees list existing file
        with open('/Users/sapir/Documents/python/final project- employee attandance log/emplist.csv', 'a') as f:
            df.to_csv(f, header=False)
    except FileNotFoundError:
        print("The path you entered:" + "{path}" + "does not exist")
    return df


add_employee_csv()

"""============= DELETE EMPLOYEES MANUALLY============="""
import os
import csv


def delete_employee_manually():
    """
    This function deletes employees manually. The user enters a name of employee to delete from the employee's file "emplis.csv".
    It delete a row if it has a value of user input '0' in the second column.
    """
    with open('/Users/sapir/Documents/python/final project- employee attandance log/emplist.csv', 'r') as inp, \
            open('/Users/sapir/Documents/python/final project- employee attandance log/new_emplist.csv', 'w') as out:
        writer = csv.writer(out)
        input_name = input("Enter employee's Name to delete :")
        if input_name.isalpha():
            print("Employees name is alphabetic ")
        else:
            print("Invalid employees name ")
            return
        name_to_del = input_name
        for row in csv.reader(inp):
            # if the name entered is not equal to names in the list- rewrite those names- eliminate the equal names
            if row[1] != name_to_del:
                writer.writerow(row)
    os.remove('/Users/sapir/Documents/python/final project- employee attandance log/emplist.csv')
    os.rename('/Users/sapir/Documents/python/final project- employee attandance log/new_emplist.csv',
              '/Users/sapir/Documents/python/final project- employee attandance log/emplist.csv')


delete_employee_manually()

"""============= DELETE EMPLOYEES FROM FILE============="""
import os
import csv


def delete_employee_from_file():
    """
        This function deletes employees from a csv file path. The user can enter a file path that contains information of employees to
         delete from the employee's file "emplis.csv".
        It delete a row if it has the same value ID in a row in "emplist.csv"
        """
    try:
        path = input("Enter employees file path to delete:")
        with open('/Users/sapir/Documents/python/final project- employee attandance log/emplist.csv', 'r') as inp, \
                open('/Users/sapir/Documents/python/final project- employee attandance log/new_emplist.csv',
                     'w') as out, \
                open(path, 'r') as to_del:
            writer = csv.writer(out)
            emps = list(csv.reader(inp))
            to_delete = list(csv.reader(to_del))
            for row in emps:
                if row not in to_delete:
                    writer.writerow(row)
    except FileNotFoundError:
        print("The path you entered:" + "{path}" + "does not exist")
        # if the id in file is not equal to id in the list- rewirte those employees- eliminate the equal employees
    os.remove('/Users/sapir/Documents/python/final project- employee attandance log/emplist.csv')
    os.rename('/Users/sapir/Documents/python/final project- employee attandance log/new_emplist.csv',
              '/Users/sapir/Documents/python/final project- employee attandance log/emplist.csv')


delete_employee_from_file()

"""============= MARK ATTENDANCE============="""
import pandas as pd
import datetime

"""
   This function marks employees attendance. Employee enters his ID and name and attendance is marked. 
   The program gets date and time from computer clock every time the attendance is marked and saves to a csv file  "attandance_log.csv".
   """


def mark_attendance():
    dnt = datetime.datetime.now()
    date_and_time = dnt.strftime("%d/%m/%Y %H:%M:%S")
    input_id = input("Enter your ID :")
    if input_id.isdigit():
        print("Employee ID is Number ")
    else:
        print("Invalid Employee ID ")
        return
    input_name = input("Enter your Name :")
    if input_name.isalpha():
        print("Employees name is alphabetic ")
    else:
        print("Invalid employee name ")
        return
    employee_name = input_name
    employee_id = input_id
    df1 = pd.DataFrame(data=[[date_and_time, employee_id, employee_name]],
                       columns=["Today's Date & Time", "Employee's ID", "Employee's Name"])
    with open('/Users/sapir/Documents/python/final project- employee attandance log/attandance_log.csv', 'a') as f:
        df1.to_csv(f, header=False, index=False)
    return df1


dataf = mark_attendance()
print(dataf)

"""============= EMPLOYEE'S ATTENDANCE REPORT============="""
import csv

"""
    This function generates attendance report for a given employee.
    The user enters a name of employee and a new csv file with his name is generated with all his attendance logs.
    """


def employee_attendance_report():
    empdata = []  # Buffer list
    with open("/Users/sapir/Documents/python/final project- employee attandance log/attandance_log.csv",
              "r") as input_file:
        reader = csv.reader(input_file, )
        input_name = input("Enter Employee's name to generate attendance report:")
        if input_name.isalpha():
            print("Employee name is alphabetic ")
        else:
            print("Invalid employee name ")
            return
        employee_name = input_name
        for row in reader:
            try:
                if row[2] == employee_name:
                    empdata.append(row)
            except IndexError as e:
                print(e)
                pass
    print(empdata)
    with open('{}.csv'.format(employee_name + '_log'), "w+") as to_file:
        writer = csv.writer(to_file)
        for new_row in empdata:
            writer.writerow(new_row)


employee_attendance_report()

"""============= EMPLOYEES  MONTHLY ATTENDANCE REPORT============="""
import datetime
import pandas as pd
import csv

"""
    This function generates attendance report for a chosen month.
    The user enters the month's number and a new csv file with the months number is generated with active employee's
    attendance logs.
    """


def monthly_attendance_report():
    monthly_emps_log = []
    with open("/Users/sapir/Documents/python/final project- employee attandance log/attandance_log.csv",
              "r") as input_file:
        reader = csv.reader(input_file, )
        input_month = input("Enter month number to create log (1-12):")
        if input_month.isnumeric():
            print("Numeric month ")
        else:
            print("Invalid input ")
            return
        int_input_month = int(input_month)
        if int_input_month > 12:
            print("There are only 12 months")
            return
        this_month = int_input_month
        today_date = datetime.datetime.today()
        start = today_date.replace(day=1, month=this_month, hour=00, minute=00)

        if this_month < 12:
            next_month = this_month + 1
        else:
            next_month = 1
        end = today_date.replace(day=1, month=next_month, hour=00, minute=00)
        for row in reader:
            arrive_time = datetime.datetime.strptime(row[0], "%d/%m/%Y %H:%M:%S")
            if start < arrive_time < end:
                monthly_emps_log.append(row)
        path = '{}.csv'.format(str(input_month) + '_monthly_log')
        with open(path, "w+") as to_file:
            writer = csv.writer(to_file)
            for new_row in monthly_emps_log:
                writer.writerow(new_row)

        df = pd.read_csv(path, header=None, index_col=0)
        print(df)


monthly_attendance_report()

"""=============LATE EMPLOYEES ATTENDANCE REPORT============="""
import datetime
import pandas as pd
import csv

"""
    This function generates attendance report for all employees who were late (that arrived after 09:30).

    """


def late_employees_report():
    late_emps_log = []
    with open("/Users/sapir/Documents/python/final project- employee attandance log/attandance_log.csv",
              "r") as input_file:
        reader = csv.reader(input_file, )
        today_date = datetime.datetime.today()
        late_time = today_date.replace(day=29, month=7, hour=9, minute=30)
        for row in reader:
            arrive_time = datetime.datetime.strptime(row[0], "%d/%m/%Y %H:%M:%S")
            if late_time < arrive_time:
                late_emps_log.append(row)
        path = '{}.csv'.format(str(today_date) + '_latelog')
        with open(path, "w+") as to_file:
            writer = csv.writer(to_file)
            for new_row in late_emps_log:
                writer.writerow(new_row)

        df = pd.read_csv(path, header=None, index_col=0)
        print(df)


late_employees_report()
