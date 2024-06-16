# Datele pentru distribuția pe țări
import os
from matplotlib import pyplot as plt


countries = ['Statele Unite', 'Japonia', 'Elveția', 'Norvegia', 'Finlanda', 'Marea Britanie', 'Canada', 'Coreea de Sud', 'China', 'Israel']
percentages_countries = [46.7, 31.1, 12.1, 2.3, 2.2, 1.8, 1.5, 1.1, 1.1, 0.3]

# Crearea graficului de tip pie
plt.figure(figsize=(10, 6))
# plt.pie(percentages_countries, labels=countries, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Distribuția Geografică a ETF-ului BOTZ')
plt.axis('equal')
plt.pie(percentages_countries, labels=countries, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors, pctdistance=0.7, 
        frame=True, 
        # wedgeprops=dict(width=0.7, edgecolor='w')
        )



output_dir = './figures'
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, 'distributie.png'))    
plt.show()


