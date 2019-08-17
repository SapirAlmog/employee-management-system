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
