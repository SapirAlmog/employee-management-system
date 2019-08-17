import pandas as pd


def add_emp_csving():
    colnames = ['ID', 'Name', 'Phone', 'Age']
    df = pd.read_csv('/Users/sapir/Documents/python/final project- employee attandance log/emloyeescsv.csv',
                        names=colnames, header=None)
    with open('/Users/sapir/Documents/python/final project- employee attandance log/emplist.csv', 'a') as f:
        df.to_csv(f, header=False)
    return df

dftry= add_emp_csving()


