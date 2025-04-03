!wget -r -nH -e robots=off --cut-dirs=1 --no-parent --reject "index.html*" https://ncei.axiomdatascience.com/atn/prod/

import xarray as xr
ds = xr.open_mfdataset('prod/*.nc', 
                       combine='nested', 
                       concat_dim = 'obs',
                       combine_attrs='drop_conflicts',
                       engine='h5netcdf')

time_min = ds['time'].dt.date.values.min()
time_max = ds['time'].dt.date.values.max()

print(f'Time Range: {time_min} - {time_max}')

# remove cf_role attr
if 'cf_role' in ds.animal.attrs.keys():
  del ds.animal.attrs['cf_role']
ds.animal.attrs

ds.to_netcdf('atn_collection.nc', engine='h5netcdf')
