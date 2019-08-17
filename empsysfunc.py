import pandas as pd
import datetime

def add_emp_manually():
    employees = [(1111, "Sapir Almog", "0547414641", 31),
                 (1112, "Gilad Benatiya", "0502555605", 35)]
    try:
        addemp=(int(input("Enter employee's ID number:")),
            input(str("Enter Employee's name:")),
            input("Enter Employee's phone number:"),
            input("Enter Employee's Age"))
    except ValueError:
        print ("Make sure you entered correct information")
    employees.append(addemp)
    df = pd.DataFrame(employees, columns=['ID', 'Name', 'Phone', 'Age'])
    #Add to employees list existing file
    with open('/Users/sapir/Documents/python/final project- employee attandance log/emplist.csv', 'a') as f:
        df.to_csv(f, header=False, index_col=0)
    return df




def add_emp_csv():
    colnames = ['ID', 'Name', 'Phone', 'Age']
    df = pd.read_csv('/Users/sapir/Documents/python/final project- employee attandance log/emloyeescsv.csv',
                        names=colnames, header=None, index_col=0)
    # Add to employees list existing file
    with open('/Users/sapir/Documents/python/final project- employee attandance log/emplist.csv', 'a') as f:
        df.to_csv(f, header=False)
    return df


def attandance_log():

    dnt =  datetime.datetime.now()
    dnt_string = dnt.strftime("%d/%m/%Y %H:%M:%S")
    empid = input("Enter Your ID :")
    empname=input("Enter Your Name :")
    df1 = pd.DataFrame(data=[[dnt_string,empid,empname]],columns=["Today's Date & Time", "Employee's ID", "Employee's Name"])
    with open('/Users/sapir/Documents/python/final project- employee attandance log/attandance_log.csv', 'a') as f:
        df1.to_csv(f, header=False)
    return df1


