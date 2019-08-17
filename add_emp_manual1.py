import pandas as pd
import datetime

""" 
This function gets employee's information (ID, Name, Phone number, Age) as an input from the user, and saves it into
pandas data frame
"""


def add_emp_manually():
    employees = [(1111, "Sapir Almog", "0547414641", 31),
                 (1112, "Gilad Benatiya", "0502555605", 35)]

    addemp = (int(input("Enter employee's ID number:")),
              input(str("Enter Employee's name:")),
              input("Enter Employee's phone number:"),
              input("Enter Employee's Age"))
    employees.append(addemp)
    df = pd.DataFrame(employees, columns=['ID', 'Name', 'Phone', 'Age'])
    # Add to employees list existing file
    with open('/Users/sapir/Documents/python/final project- employee attandance log/emplist.csv', 'a') as f:
        df.to_csv(f,names=['ID', 'Name', 'Phone', 'Age'], header=False, index_col=0)
    return df


add_emp_manually()
