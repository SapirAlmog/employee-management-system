import pandas as pd
from empsysfunc import (add_emp_manually, add_emp_csv,attandance_log)


# Create a DataFrame object

try:
    df = pd.read_csv('/Users/sapir/Documents/python/final project- employee attandance log/emplist.csv', index_col=0)
    ask_to_enter_emp = input("Do You want to create a new employee? y/n")
    if ask_to_enter_emp == "y":
        ask_manually = input("Do you want to type it? y/n")
        ask_csv = input("Do you want to import employyes from a file? y/n")
        if ask_manually == "y":
            # manually add employee
            input_emp_df = add_emp_manually()
        else:
            print("No data to enter")
            print("Employees aaaaaaInformation", input_emp_df, sep='\n')
        if ask_csv == "y":
            # add employee from csv file
            csv_emp_df = add_emp_csv()
        else:
            print("no data to import")
            print("Employees Information", csv_emp_df, sep='\n')
        if ask_csv == "y" and ask_manually == "y":
            frames = [input_emp_df, csv_emp_df]
            # merge data employeed data frames
            emp_df = pd.concat(frames)
            print("Updated Employees Information", emp_df, sep='\n')
        else:
            print("No new employees")
    else:
        print("OK good bye")
except NameError:
    print("NameError- one or more functions were not in use")

#try:
attandance_df= attandance_log()
#except ValueError:
        #print("ID shoul'd contain numbers ONLY")
#print (attandance_df)





"""
#add employee from csv file
csv_emp_df=add_emp_csv()

#merge data employeed data frames
frames = [input_emp_df, csv_emp_df]
emp_df=pd.concat(frames)

#Mark attandanc function
attandance_df= attandance_log()

print("Employees Information", empdf, sep='\n')



 List of Tuples
employees = [(1111,"Sapir Almog","0547414641" ,31),
            (1112,"Gilad Benatiya","0502555605" ,35)]

def add_emp_manually():
    addemp=(int(input("Enter employee's ID number:")),
            input("Enter Employee's name:"),
            input("Enter Employee's phone number:"),
            input("Enter Employee's Age"))
    return employees.append(addemp)

def add_emp_csv():
    colnames = ['ID', 'Name', 'Phone', 'Age']
    dfcsv = pd.read_csv('/Users/sapir/Documents/python/final project- employee attandance log/emloyeescsv.csv',
                        names=colnames, header=None)
    return dfcsv"""