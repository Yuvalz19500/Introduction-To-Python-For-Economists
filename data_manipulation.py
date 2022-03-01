from statistics import mode
from matplotlib import pyplot as plt
from statsmodels.formula.api import ols
import numpy as np


def handle_option_a(df):
    # A function that handles index option a
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
    # A function that handles index option b
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
    # A function that handles index option c
    plt.figure(figsize=(15, 10))

    plt.rc('xtick', labelsize=14)
    plt.rc('ytick', labelsize=14)

    plt.ylabel('Frequency', fontsize=16)
    plt.xlabel('Positive Returns (Yes/No)', fontsize=16)

    plt.title('Histogram Of Positive Returns', fontsize=20)

    plt.hist(df['pos_returns'], color='blue')
    plt.show()


def handle_option_d(df):
    # A function that handles index option d
    plt.figure(figsize=(15, 10))

    plt.rc('xtick', labelsize=14)
    plt.rc('ytick', labelsize=14)

    plt.ylabel('Returns', fontsize=16)
    plt.xlabel('Lagged Returns', fontsize=16)

    plt.title('Scatter Plot: Returns vs Lagged Returns', fontsize=20)

    plt.scatter(df['returns'], df['lag_ret'], color='purple')
    plt.show()


def handle_option_e(df):
    # A function that handles index option e
    mean = df["returns"].mean()
    standard_deviation = df["returns"].std()
    coefficient = standard_deviation / mean

    print('The average daily returns: %f' % (mean))
    print('The average daily returns standard deviation: %f' %
          (standard_deviation))
    print('The coefficient of variation of the returns : %f' % (coefficient))


def handle_option_f(df):
    # A function that handles index option f
    model = create_model(df)
    model_res = model.fit()
    print(model_res.summary())


def handle_option_g(df):
    # A function that handles index option g
    model = create_model(df)
    prediction = model.fit().predict(df)
    rounded_prediction = np.where(prediction > 0.5, 1, 0)
    accuracy = np.where(rounded_prediction == df["pos_returns"], 1, 0)
    print("The % of correct predictions is: ", round(np.mean(accuracy), 4))


def create_model(df):
    # A function that creates ols model
    df["temp"] = np.where(df["close"] > df["open"], 1, 0)
    df.head()
    model = ols(formula='pos_returns~lag_ret + temp ', data=df)
    df = df.drop('temp', axis=1)
    return model
