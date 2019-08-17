import pandas as pd

""" 
This function gets employee's information. The user can enter a file path which contains data of employees to add to the 
employees file- "emplist.csv".
"""


def add_emp_csv():
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


add_emp_csv()
