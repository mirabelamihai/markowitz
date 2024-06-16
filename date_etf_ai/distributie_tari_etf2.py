import os
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import pandas as pd

# Datele pentru distribuția pe țări
countries = ['United States', 'Japan', 'Switzerland', 'Norway', 'Finland', 'United Kingdom', 'Canada', 'South Korea', 'China', 'Israel']
percentages_countries = [46.7, 31.1, 12.1, 2.3, 2.2, 1.8, 1.5, 1.1, 1.1, 0.3]

# Crearea unui DataFrame
data = {'Country': countries, 'Percentage': percentages_countries}
df = pd.DataFrame(data)

# Citirea hărții mondiale folosind geopandas
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Alinierea numelor țărilor din setul de date cu numele din harta mondială
df['Country'] = df['Country'].replace({
    'United States': 'United States of America',
    'South Korea': 'Republic of Korea'
})

# Combinarea setului de date cu harta mondială
world = world.merge(df, how='left', left_on='name', right_on='Country')

# Poziții pentru etichete în jurul hărții
label_positions = {
    'United States': (-500, 0),
    'United States of America': (-500, 500),
    'Japan': (155, 45),
    'Switzerland': (40, 47),
    'Norway': (40, 65),
    'Finland': (40, 62),
    'United Kingdom': (15, 55),
    'Canada': (-90, 60),
    'South Korea': (135, 35),
    'China': (110, 30),
    'Israel': (50, 30)
}

# Crearea graficului
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
world.boundary.plot(ax=ax)
world.plot(column='Percentage', ax=ax, legend=True, cmap='OrRd',
           legend_kwds={'label': "Percentage of Assets", 'orientation': "vertical", 'shrink': 0.6, 'location': 'right', 'pad': 0.02})

# Adăugarea săgeților și a etichetelor pentru țări și procente
for idx, row in world.iterrows():
    if pd.notnull(row['Percentage']):
        xy = (row['geometry'].centroid.x, row['geometry'].centroid.y)
        label = f"{row['Country']}: {row['Percentage']}%"
        xytext = label_positions[row['Country']]
        arrow = FancyArrowPatch(posA=xy, posB=xytext, color='black', arrowstyle='-|>')
        ax.add_patch(arrow)
        plt.text(xytext[0], xytext[1], label, fontsize=10, ha='center')

ax.set_title('Distribuția Geografică a ETF-ului BOTZ')

output_dir = './figures'
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, 'harta_etf2.png')) 

plt.show()
