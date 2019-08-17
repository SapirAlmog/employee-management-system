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
