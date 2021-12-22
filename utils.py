import sys

valid_options_step_one = ['A', 'B', 'C', 'D', 'a', 'b', 'c', 'd']
date_options = ['A', 'B', 'C', 'a', 'b', 'c']


def print_and_choose_options():
    print("Please choose with which set of data you would like to work with:")
    print("A. NASDAQ 100\tB. S&P 500\tC. Russell 2000\tD. Quit")
    chosen_option = input("Please enter your option: ")
    chosen_option = validate_option(chosen_option)
    handle_option(chosen_option)


def validate_option(option):
    new_option = option
    while not new_option in valid_options_step_one:
        print("\'%s\' is not a valid option." % (new_option))
        new_option = input("Please enter a valid option from the above list: ")

    return new_option


def handle_option(option):
    if option in date_options:
        dates = get_dates()
    else:
        sys.exit()


def get_dates():
    start_date = input("Please choose a starting date (YYYY-MM-DD): ")
    end_date = input("Please choose the final date (YYYY-MM-DD): ")

    return {start_date, end_date}
