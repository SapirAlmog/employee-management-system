import csv

"""
    This function generates attendance report for a given employee.
    The user enters a name of employee and a new csv file with his name is generated with all his attendance logs.
    """


def employee_attendance_report():
    empdata = []  # Buffer list
    with open("/Users/sapir/Documents/python/final project- employee attandance log/attandance_log.csv",
              "r") as input_file:
        reader = csv.reader(input_file, )
        input_name = input("Enter Employee's name to generate attendance report:")
        if input_name.isalpha():
            print("Employee name is alphabetic ")
        else:
            print("Invalid employee name ")
            return
        employee_name = input_name
        for row in reader:
            try:
                if row[2] == employee_name:
                    empdata.append(row)
            except IndexError as e:
                print(e)
                pass
    print(empdata)
    with open('{}.csv'.format(employee_name + '_log'), "w+") as to_file:
        writer = csv.writer(to_file)
        for new_row in empdata:
            writer.writerow(new_row)


employee_attendance_report()
