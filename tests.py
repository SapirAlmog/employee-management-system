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
            print("Employees Information", input_emp_df, sep='\n')
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