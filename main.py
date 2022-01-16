import sys
import user_interaction as ui


def main():
    chosen_option = ui.print_options_and_choose()
    while chosen_option != 'D' or chosen_option != 'd':
        chosen_option = ui.print_options_and_choose()
    return 0


if __name__ == '__main__':
    sys.exit(main())
