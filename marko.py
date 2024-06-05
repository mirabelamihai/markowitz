import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt


def portofolio_return(df, weights):
    portofolio = np.dot(df.mean(), weights)
    return portofolio

def portofolio_std(df, weights):
    cov = df.cov()
    pv= np.dot(np.dot(weights, cov), weights.T)
    pv = np.sqrt(pv)
    return pv

def portofolio_std_anual(df, weights):
    pv = portofolio_std(df, weights)
    pv = pv * np.sqrt(252)
    return pv

def weights_creator(df):
    rand = np.random.random(len(df.columns))
    rand /= rand.sum()
    return rand

def markovitz():
    df = yf.download(['AAPL', 'CAT', 'NVDA', 'MSFT', 'TSLA'], 
         start="2013-12-31", end="2024-06-05")

    # log returns
    df = np.log(1 + df ['Adj Close'].pct_change())

    print(df)
    # portofolio return
    #print(df.mean() * 252)
    # weights = np.array([0.5, 0.5])
    # df.AAPL
    # portofolio = weights[0] * df.AAPL.mean()  + weights[1] * df.NVDA.mean()

    # portofolio = portofolio_return(df, weights)

    # print(portofolio)

    # cov = df.cov()

    # portofolio variance - covariance
    # pv = weights[0]**2 * cov.iloc[0, 0] + weights[1]**2 * cov.iloc[1, 1] + 2 * weights[0] * weights[1] * cov.iloc[0, 1]

    # pv_std = np.sqrt(pv)

    # pv2= np.dot(np.dot(weights, cov), weights.T)

    weights = weights_creator(df)
    print(weights)

    returns = [] 
    stds = []
    w = []
    for i in range(500):
        weights = weights_creator(df)
        returns.append(portofolio_return(df, weights))
        stds.append(portofolio_std_anual(df, weights))
        w.append(weights)

    print(min(stds))
    argmin = stds.index(min(stds))
    print(returns[argmin])


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

    print(min(stds))
    argmin = stds.index(min(stds))
    print(returns[argmin])
    print (w[argmin])


    # 








    # portofolio volatility
    print(df.cov() * 252)

    # portofolio variance
    print(df.var() * 252)

    # portofolio sharpe ratio  
    print(df.mean() * 252 / df.std() * np.sqrt(252))

    






if __name__ == "__main__":
    markovitz()