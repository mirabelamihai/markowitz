import matplotlib.pyplot as plt
import os
import numpy as np

# Datele pentru distribuția sectorului
sectors = ['Tehnologia Informației', 'Industriale', 'Sănătate', 'Financiar', 'Energie', 'Bunuri de consum discreționare']
percentages = [43.1, 41.0, 13.8, 1.0, 0.8, 0.4]

# Crearea graficului de tip bar
plt.figure(figsize=(12, 6))

plt.subplots_adjust(left=0.2, right=0.95) #wider figure
# create a colormap with 100 discrete colors
# cmap = plt.get_cmap('viridis', len(percentages))  # create a colormap with len(percentages) discrete colors
# create a normalization object
# norm = plt.Normalize(0, 100)
# create a ScalarMappable object using the colormap and normalization
# scalar_map = plt.cm.ScalarMappable(cmap=cmap, norm=norm)

# generate colors for each percentage
# colors = [scalar_map.to_rgba(p) for p in percentages]

# plot the bars with the corresponding colors
import matplotlib.colors as mcolors

# create random colors for all percentages
colors = [mcolors.to_hex(np.random.rand(3,)) for _ in range(len(percentages))]
plt.barh(sectors, percentages, color=colors)
# for i, p in enumerate(percentages):
#     plt.text(p, i, str('{p:.2f}'.format(p=p)) + '%', va='center', ha='center', color='black')
for i, p in enumerate(percentages):
    plt.text(p, i, str('{p:.2f}'.format(p=p)) + '%', va='center', ha='left', color='black')

# add a colorbar
# plt.colorbar(scalar_map)
# plt.barh(sectors, percentages, color='#FFC107')  # Alege culoarea 'turqoise' pentru 'Tehnologia Informației'
plt.xlabel('Procentaj')
plt.title('Distribuția Sectorială a ETF-ului BOTZ')
output_dir = './figures'
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, 'etf.png'))    
plt.show()
