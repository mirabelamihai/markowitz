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


# Poziții pentru etichete în jurul hărții
#first negative - vest
label_positions = {
    'United States': (-50, -25),
    'United States of America': (-35, -25),
    'Japan': (25, 0),
    'Switzerland': (-40, -15),
    'Norway': (-20, 0),
    'Finland': (15, 10),
    'United Kingdom': (-35, -15),
    'Canada': (-20, 20),
    'South Korea': (50, 25),
    'China': (50, -25),
    'Israel': (25, 25)
}


# Combinarea setului de date cu harta mondială
world = world.merge(df, how='left', left_on='name', right_on='Country')

# Crearea graficului
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
world.boundary.plot(ax=ax)
world.plot(column='Percentage', ax=ax, legend=True, cmap='OrRd', legend_kwds={'label': "Percentage of Assets", 'orientation': "horizontal"})
# Adăugarea etichetelor pentru țări și procente
# Adăugarea săgeților și a etichetelor pentru țări și procente
for idx, row in world.iterrows():
    if pd.notnull(row['Percentage']):
        xy = (row['geometry'].centroid.x, row['geometry'].centroid.y)
        ax.annotate(text=f"{row['Country']}: {row['Percentage']}%", xy=xy, xytext=(xy[0] + label_positions[row['Country']][0], xy[1] + label_positions[row['Country']][1]),
                    ha='center', fontsize=8, color='black', weight='bold',
                    arrowprops=dict(facecolor='black', arrowstyle='->'))

ax.set_title('Distribuția Geografică a ETF-ului BOTZ')
output_dir = './figures'
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, 'harta_etf.png')) 
plt.show()