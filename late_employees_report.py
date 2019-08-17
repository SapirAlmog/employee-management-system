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
