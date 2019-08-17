import csv


def readFile(employees):
    with open('file.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        employees.append(row[0], row[1], row[2:],)
    return



def add_emp_csv():
    colnames = ['ID', 'Name', 'Phone', 'Age']
    df = pd.read_csv('/Users/sapir/Documents/python/final project- employee attandance log/emloyeescsv.csv',
                        names=colnames, header=None)
    return df