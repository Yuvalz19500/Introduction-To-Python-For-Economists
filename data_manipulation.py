from matplotlib import pyplot as plt
from statsmodels.formula.api import ols


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
    plt.figure(figsize=(15, 10))

    plt.rc('xtick', labelsize=14)
    plt.rc('ytick', labelsize=14)

    plt.ylabel('Frequency', fontsize=16)
    plt.xlabel('Positive Returns (Yes/No)', fontsize=16)

    plt.title('Histogram Of Positive Returns', fontsize=20)

    plt.hist(df['pos_returns'], color='blue')
    plt.show()


def handle_option_d(df):
    plt.figure(figsize=(15, 10))

    plt.rc('xtick', labelsize=14)
    plt.rc('ytick', labelsize=14)

    plt.ylabel('Returns', fontsize=16)
    plt.xlabel('Lagged Returns', fontsize=16)

    plt.title('Scatter Plot: Returns vs Lagged Returns', fontsize=20)

    plt.scatter(df['returns'], df['lag_ret'], color='purple')
    plt.show()


def handle_option_e(df):
    return


def handle_option_f(df):
    model = ols(formula='pos_returns', data=df)
    model_res = model.fit()
    print(model_res.summary())


def handle_option_g(df):
    return
