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
