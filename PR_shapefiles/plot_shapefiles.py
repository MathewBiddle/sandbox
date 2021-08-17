import geopandas as gpd
import matplotlib.pyplot as plt

prico = gpd.read_file('p_rico.shp')

stc = gpd.read_file('stc_fin.shp')

stsj = gpd.read_file('stsj_fin.shp')

prico.plot(column='DESCRIPTOR', legend=True, cmap='tab20')
plt.title('Puerto Rico')
stc.plot(column='DESCRIPTOR', legend=True, cmap='tab20')
plt.title('St. Croix, USVI')
stsj.plot(column='DESCRIPTOR', legend=True, cmap='tab20')
plt.title('St. Thomas and St. John, USVI')