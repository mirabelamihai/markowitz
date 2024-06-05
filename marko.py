import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt


def portofolio_return(df, weights):
    """
    Calculate the portfolio return given the stock data and weights.

    Parameters:
    df (DataFrame): The stock data.
    weights (array-like): The weights of each stock.

    Returns:
    float: The portfolio return.
    """
    # Calculate the portfolio return by multiplying the mean of the stock data by the weights
    portofolio = np.dot(df.mean(), weights)
    
    return portofolio

def portofolio_std(df, weights):
    """
    Calculate the portfolio standard deviation given the stock data and weights.

    Parameters:
    df (DataFrame): The stock data.
    weights (array-like): The weights of each stock.

    Returns:
    float: The portfolio standard deviation.
    """
    # Calculate the covariance matrix of the stock data
    cov = df.cov()
    
    # Calculate the portfolio variance by multiplying the covariance matrix by the weights and transpose of weights
    pv = np.dot(np.dot(weights, cov), weights.T)
    
    # Calculate the square root of the portfolio variance to get the standard deviation
    pv = np.sqrt(pv)
    
    return pv

def portofolio_std_anual(df, weights):
    """
    Calculate the annualized portfolio standard deviation given the stock data and weights.

    Parameters:
    df (DataFrame): The stock data.
    weights (array-like): The weights of each stock.

    Returns:
    float: The annualized portfolio standard deviation.
    """
    # Calculate the standard deviation of the portfolio
    pv = portofolio_std(df, weights)

    # Annualize the standard deviation by multiplying it by the square root of the number of trading days in a year (252 for most years)
    pv = pv * np.sqrt(252)

    return pv


def weights_creator(df):
    """
    This function creates random weights for each stock in the dataframe.

    Parameters:
    df (DataFrame): The stock data.

    Returns:
    array-like: The weights of each stock.
    """
    # Create an array of random numbers with the same length as the number of columns in the dataframe
    rand = np.random.random(len(df.columns))
    
    # Normalize the array so that the sum of all weights is 1
    rand /= rand.sum()
    
    return rand


def even(n):
    """
    This function returns a list of all even numbers from 0 to n-1.

    Parameters:
    n (int): The upper limit of the range of numbers to check.

    Returns:
    list: A list containing all the even numbers from 0 to n-1.
    """
    l = []  # Initialize an empty list to store the even numbers
    for i in range(n):  # Iterate over the range of numbers
        if i % 2 == 0:  # Check if the number is even
            l.append(i)  # If even, add it to the list

    return l  # Return the list of even numbers

def markovitz():
    """
    This function downloads stock data, calculates log returns, generates random weights,
    and plots the efficient frontier.
    """
    # Download stock data
    df = yf.download(['AAPL', 'CAT', 'NVDA', 'MSFT', 'TSLA'], 
                     start="2013-12-31", end="2024-06-05")

    # Calculate log returns
    df = np.log(1 + df ['Adj Close'].pct_change())

    # Generate random weights
    weights = weights_creator(df)
    print(weights)

    # Calculate portfolio returns and standard deviations for different weights
    returns = []
    stds = []
    w = []
    for i in range(500):
        weights = weights_creator(df)
        returns.append(portofolio_return(df, weights))
        stds.append(portofolio_std_anual(df, weights))
        w.append(weights)

    # Find the minimum standard deviation
    argmin = stds.index(min(stds))
    print(returns[argmin])
    print(stds[argmin])
    print(w[argmin])

    # Plot the efficient frontier
    plt.scatter(stds, returns, c=returns, cmap='RdYlBu')
    plt.scatter(df.std().iloc[0] * np.sqrt(252), df.mean().iloc[0], c='black')
    plt.scatter(df.std().iloc[1] * np.sqrt(252), df.mean().iloc[1], c='yellow')
    plt.scatter(stds[argmin], returns[argmin], c='red')
    plt.title('Efficient Frontier')
    plt.colorbar(label='expected returns')
    plt.xlabel('expected volatility')
    plt.ylabel('expected returns')
    plt.savefig('ef.png')
    plt.show()
    print(w)

    # Print statistics
    print(min(stds))
    argmin = stds.index(min(stds))
    print(returns[argmin])
    print (w[argmin])



if __name__ == "__main__":
    markovitz()