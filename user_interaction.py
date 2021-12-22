import sys
import datetime

valid_options_step_one = ['A', 'B', 'C', 'D', 'a', 'b', 'c', 'd']
date_options = ['A', 'B', 'C', 'a', 'b', 'c']
index_options = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                 'H', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


def print_option_and_choose():
    print("Please choose with which set of data you would like to work with:")
    print("A. NASDAQ 100    B. S&P 500    C. Russell 2000    D. Quit")
    chosen_option = input("Please enter your option: ")
    chosen_option = validate_option(chosen_option, False)
    handle_option(chosen_option)


def validate_option(option, is_index_option):
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
    if option in date_options:
        dates = get_dates()
        handle_index_option(print_and_choose_index_options(), dates)
    else:
        sys.exit()


def get_dates():
    start_date = input("Please choose a starting date (YYYY-MM-DD): ")
    start_date = validate_date(start_date, True)
    end_date = input("Please choose the final date (YYYY-MM-DD): ")
    end_date = validate_date(end_date, False)

    return {start_date, end_date}


def print_and_choose_index_options():
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
    return validate_option(index_option, True)


def date_validation(date_string):
    try:
        datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def validate_date(date_string, is_start):
    if is_start:
        is_start = "starting"
    else:
        is_start = "final"

    while not date_validation(date_string):
        date_string = input(
            "Please choose a valid %s date (YYYY-MM-DD): " % (is_start))

    return date_string


def handle_index_option(index_option, dates):
    return
