import pandas as pd

""" 
This function gets employee's information (ID, Name, Phone number, Age) as an input from the user, and saves it into
pandas data frame
"""


def addemployee():
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


addemployee()
