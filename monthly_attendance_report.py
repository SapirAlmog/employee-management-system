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
