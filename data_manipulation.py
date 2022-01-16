from matplotlib import pyplot as plt


def handle_option_a(df):
    plt.figure(figsize=(15, 10))
    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(120))

    plt.rc('xtick', labelsize=14)
    plt.rc('ytick', labelsize=14)

    plt.ylabel('Price', fontsize=16)
    plt.xlabel('Date', fontsize=16)

    plt.title('The Adjusted Closing Price', fontsize=20)

    plt.plot(df['adjclose'], color='green')
    plt.show()


def handle_option_b(df):
    plt.figure(figsize=(15, 10))
    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(120))

    plt.rc('xtick', labelsize=14)
    plt.rc('ytick', labelsize=14)

    plt.ylabel('Returns', fontsize=16)
    plt.xlabel('Date', fontsize=16)

    plt.title('The Adjusted Closing Price', fontsize=20)

    plt.plot(df['returns'], color='green')
    plt.show()


def handle_option_c(df):
    return


def handle_option_d(df):
    return


def handle_option_e(df):
    return


def handle_option_f(df):
    return


def handle_option_g(df):
    return
