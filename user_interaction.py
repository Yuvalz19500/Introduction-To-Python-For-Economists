import sys

valid_options_step_one = ['A', 'B', 'C', 'D', 'a', 'b', 'c', 'd']
date_options = ['A', 'B', 'C', 'a', 'b', 'c']
index_options = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                 'H', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


def print_option_and_choose():
    print("Please choose with which set of data you would like to work with:")
    print("A. NASDAQ 100\tB. S&P 500\tC. Russell 2000\tD. Quit")
    chosen_option = input("Please enter your option: ")
    chosen_option = validate_option(chosen_option)
    handle_option(chosen_option, False)


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
    else:
        sys.exit()


def get_dates():
    start_date = input("Please choose a starting date (YYYY-MM-DD): ")
    end_date = input("Please choose the final date (YYYY-MM-DD): \n")

    return {start_date, end_date}


def print_and_choose_index_options():
    print("What would you like to do:")
    print("A. Plot a timeseries of the prices")
    print("B. Plot the timeseries of returns")
    print("C. Plot a histogram of the positive returns")
    print("D. Plot a scatter plot: returns vs. lagged returns")
    print("E. Observe the mean, standard deviation and the coefficient of variation of the returns")
    print("F. Estimate a regression of the returns. Independent variable: lagged returns.")
    print("G. Check the % of correct predictions")
    print("H. Return to choosing the data")
    index_option = input("Please enter your option: ")
    index_option = validate_option(index_option, True)
