import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os

# Lista simbolurilor bursiere
tickers = ['NVDA', 'SYM', 'HLX', 'AI', 'ATS', 'ISRG', 'PRO', 'BOTZ', '^IXIC', '^TNX']
titles = ['NVDA', 'SYM', 'HLX', 'AI', 'ATS', 'ISRG', 'PRO', 'BOTZ', '^IXIC', '^TNX']
# tickers = ['NVDA', 'SYM', 'HLX', 'AI', 'ATS', 'ISRG', 'PRO', 'BOTZ', '^IXIC', '^TNX']
# tickers = ['AAPL', 'NVDA', 'MSFT']

# Descărcarea datelor de la Yahoo Finance, ajustate pentru split-uri și dividende
data = yf.download(tickers, start="2017-06-01", end="2024-06-01")['Adj Close']

# Verificarea datelor descărcate
print(data.head())

# Redenumirea coloanelor pentru claritate
# data.columns = ['Nvidia', 'SYM', 'Helix', 'C3.ai', 'ATS', 'Intuitive Surgical', 'PROS', 'AI ETF', 'Nasdaq', 'US Bonds']
# data.columns = ['Appsle', 'Nvidia', 'Microsoft']

ticker_to_name = {
    'NVDA': 'Nvidia',
    'SYM': 'SYM',
    'HLX': 'Helix',
    'AI': 'C3.ai',
    'ATS': 'ATS',
    'ISRG': 'Intuitive Surgical',
    'PRO': 'PROS',
    'BOTZ': 'AI ETF',
    '^IXIC': 'Nasdaq',
    '^TNX': 'US Bonds'
}

# Lista culorilor pentru fiecare activ
colors = {
    'NVDA': 'green',
    'AAPL': 'red',
    'MSFT': 'blue',
    'SYM': 'purple',
    'HLX': 'orange',
    'AI': 'blue',
    'ATS': 'brown',
    'ISRG': 'pink',
    'PRO': 'red',
    'BOTZ': 'black',
    '^IXIC': 'cyan',
    '^TNX': 'teal',
    'AI Index': 'yellow'
}


def plot_grid(data, num_rows=2, num_cols=2, offset=0):
    # Setarea figurei și axelor pentru subplots, cu padding între ele
    # Setarea figurei și axelor pentru subplots
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(45, 15))


    # Funcție pentru plotarea graficelor individuale



    for i, ax in enumerate(axs.flatten()):
        # if titles[i] == 'AI Index':
        #     ax.plot(data.index, data[['NVDA', 'SYM', 'HLX', 'AI', 'ATS', 'ISRG', 'PRO', 'BOTZ', '^IXIC', '^TNX']].mean(axis=1), color=colors['AI Index'])
        # else:
        ax.plot(data.index, data[titles[i + offset]], color=colors[titles[i + offset]])
        ax.set_title(ticker_to_name[titles[i + offset]])
        ax.grid(False)  # Eliminarea grid-ului
        ax.set_xlabel('Anul')
        ax.set_ylabel('Prețul')
        ax.xaxis.set_major_locator(mdates.YearLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))   

    # Ajustarea layout-ului pentru a preveni suprapunerea
    plt.tight_layout()
    # plt.subplots_adjust(hspace=0.8)
    output_dir = './figures'
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, 'etf_grid_{}.png'.format(offset)))   
    # plt.show()

plot_grid(data, num_rows=2, num_cols=2, offset=0)
plot_grid(data, num_rows=2, num_cols=2, offset=4)
plot_grid(data, num_rows=2, num_cols=1, offset=8)


def plot_stock(data, title, color):
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data[title], color=color)
    plt.title(f'Evoluția Prețului de Închidere pentru {ticker_to_name[title]}')
    plt.xlabel('Anul')
    plt.ylabel('Prețul de Închidere')
    plt.grid(False)  # Eliminarea grid-ului
    plt.gca().xaxis.set_major_locator(mdates.YearLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    plt.show()


# Plotarea fiecărui activ
# for title in data.columns:
    # plot_stock(data, title, colors[title])
