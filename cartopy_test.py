import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.offsetbox import AnchoredText


ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([80, 170, -45, 30])

# Put a background image on for nice sea rendering.
ax.stock_img()

# Create a feature for States/Admin 1 regions at 1:50m from Natural Earth
states_provinces = cfeature.NaturalEarthFeature(
    category='physical',
    name='bathymetry_J_1000',
    scale='10m',
    )
#https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/physical/ne_10m_bathymetry_all.zip
SOURCE = 'Natural Earth'
LICENSE = 'public domain'

#ax.add_feature(cfeature.LAND)
#ax.add_feature(cfeature.COASTLINE)
ax.add_feature(states_provinces, edgecolor='gray', facecolor='none')

# Add a text annotation for the license information to the
# the bottom right corner.
#text = AnchoredText(r'$\mathcircled{{c}}$ {}; license: {}'.format(SOURCE, LICENSE),
#                    loc=4, prop={'size': 12}, frameon=True)
#ax.add_artist(text)

plt.show()

