import sys
import datetime
import data
import data_manipulation as dml

valid_options_step_one = ['A', 'B', 'C', 'D', 'a', 'b', 'c', 'd']
date_options = ['A', 'B', 'C', 'a', 'b', 'c']
index_options = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                 'H', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


def print_options_and_choose():
    # A function that prints all the available inputs to the user and gets his choice
    print("\nPlease choose with which set of data you would like to work with:")
    print("A. NASDAQ 100    B. S&P 500    C. Russell 2000    D. Quit")
    chosen_option = input("Please enter your option: ")
    chosen_option = validate_option(chosen_option, False)
    handle_option(chosen_option)
    return chosen_option


def validate_option(option, is_index_option):
    # A function that validates the chosen input from the user
    new_option = option
    if is_index_option:
        while not new_option in index_options:
            print("\'%s\' is not a valid option." % (new_option))
            new_option = input(
                "Please enter a valid option from the above list: ")
    else:
        while not new_option in valid_options_step_one:
            print("\'%s\' is not a valid option." % (new_option))
            new_option = input(
                "Please enter a valid option from the above list: ")

    return new_option


def handle_option(option):
    # A function that decides what to with the user input
    if option in date_options:
        dates = get_dates()
        df = data.download_data_and_format(option, dates)
        handle_index_option(print_and_choose_index_options(), df)
    else:
        sys.exit()


def get_dates():
    # A function that handles date input from the user
    start_date = "0"
    end_date = "0"

    print("\nPlease provide a starting date and an end date. Please Make sure:")
    print("1. The format is as specified.")
    print("2. The date is valid (not greater than today).")
    print("3. The end date is bigger than the start date.")
    print("Otherwise the program will not continue.\n")
    while not date_validation(start_date) or datetime.datetime.strptime(start_date, '%Y-%m-%d') > datetime.datetime.now():
        start_date = input("Please choose a starting date (YYYY-MM-DD): ")

    while not date_validation(end_date) or datetime.datetime.strptime(end_date, '%Y-%m-%d') > datetime.datetime.now() or datetime.datetime.strptime(end_date, '%Y-%m-%d') < datetime.datetime.strptime(start_date, '%Y-%m-%d'):
        end_date = input("Please choose the final date (YYYY-MM-DD): ")

    return {'start_date': start_date, 'end_date': end_date}


def print_and_choose_index_options():
    # A function that prints and handles index options for a selected ticker
    print("\nWhat would you like to do:")
    print("A. Plot a timeseries of the prices")
    print("B. Plot the timeseries of returns")
    print("C. Plot a histogram of the positive returns")
    print("D. Plot a scatter plot: returns vs. lagged returns")
    print("E. Observe the mean, standard deviation and the coefficient of variation of the returns")
    print("F. Estimate a regression of the returns. Independent variable: lagged returns.")
    print("G. Check the % of correct predictions")
    print("H. Return to choosing the data")
    index_option = input("Please enter your option: ")
    print()
    return validate_option(index_option, True)


def date_validation(date_string):
    # A function that validates a date string
    try:
        datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def handle_index_option(index_option, df):
    # A function that handles the selected index option by the user
    if index_option == 'A' or index_option == 'a':
        dml.handle_option_a(df)
    elif index_option == 'B' or index_option == 'b':
        dml.handle_option_b(df)
    elif index_option == 'C' or index_option == 'c':
        dml.handle_option_c(df)
    elif index_option == 'D' or index_option == 'd':
        dml.handle_option_d(df)
    elif index_option == 'E' or index_option == 'e':
        dml.handle_option_e(df)
    elif index_option == 'F' or index_option == 'f':
        dml.handle_option_f(df)
    elif index_option == 'G' or index_option == 'g':
        dml.handle_option_g(df)
    else:
        print_options_and_choose()
