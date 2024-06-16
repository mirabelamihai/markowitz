import os
import pandas as pd
import matplotlib.pyplot as plt

# Datele pentru companii și capitalizarea de piață
data = {
    "Ticker": [
        "NVDA", "ABBN SW", "ISRG", "6861 JP", "6273 JP", "6954 JP", "6506 JP", "DT", "CGNX", "6383 JP",
        "6645 JP", "AVAV", "PEGA", "AUTO NO", "PATH", "TECN SW", "CGCBV FH", "454910 KS", "RSW LN", "AI",
        "PRCT", "SYM", "ATS CN", "JBT", "277810 KS", "UPST", "HLX", "2252 HK", "OMCL", "PRO", "APPN", "SOUN",
        "IXTM4 Index", "3993 JP", "6104 JP", "MTRN IT", "HSAI", "6258 JP", "2121 HK", "FARO", "IRBT", "4259 JP", "CRNC"
    ],
    "Market Value ($)": [
        368307870.00, 267720682.24, 244239329.84, 204578766.04, 183616044.86, 118504992.19, 115815978.70,
        115210639.99, 99443754.78, 88756111.59, 85884960.92, 76589064.44, 61063562.50, 61002510.53, 60419043.26,
        58861802.46, 56385757.05, 52668352.80, 46401364.63, 42690106.80, 40180668.24, 39746644.75, 39314435.54,
        38936974.64, 29359715.79, 24370597.01, 19153253.00, 18771035.82, 15863346.25, 15624706.32, 14780882.35,
        11586403.63, 9629760.00, 8942425.09, 7754287.84, 5953517.63, 5613573.03, 5572954.95, 4334433.83,
        3877665.98, 3037835.61, 2264037.74, 1513470.48
    ]
}

df = pd.DataFrame(data)

# Sortarea datelor după valoarea de piață
df_sorted = df.sort_values(by='Market Value ($)')

# Crearea graficului de tip bar orizontal
plt.figure(figsize=(15, 10))

plt.subplots_adjust(right=0.8) #right padding
# plt.subplots_adjust(left=0.1, right=1.1) #wider figure
bars = plt.barh(df_sorted['Ticker'], 
                df_sorted['Market Value ($)'], 
                color='turquoise', 
                # height=0.8
                )
plt.xlabel('Market Value ($)')
plt.ylabel('Ticker')
plt.title('Market Value of Companies in ETF BOTZ (Sorted)')

# Adăugarea valorilor deasupra barurilor
for bar in bars:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f'{bar.get_width():,.2f}', va='center', ha='left', fontsize=8)


output_dir = './figures'
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, 'capitalizare.png'))
plt.show()
