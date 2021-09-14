import geopandas as gpd
import pandas as pd



def shape2geojson(infile: str):
    try:
        infile.split(".")[-1] != 'shp'

    except:
        return ("Incorrect input file!\n%s is not a shapefile." % infile)

    else:
        try:
            open(infile, 'r')

        except FileNotFoundError:
            return ("File %s not found!" % infile)

        else:
            shpfile = gpd.read_file(infile)
            outfile = infile.replace('.shp', '.geojson')
            shpfile.to_file(outfile, driver='GeoJSON')

            return True


def multishape2geojson(shapefiles: list, outfile: str):
    #folder = Path(path)
    #shapefiles = folder.glob("*.shp")
    gdf = pd.concat([
        gpd.read_file(shp).to_crs("EPSG:4326")
        for shp in shapefiles
    ]).pipe(gpd.GeoDataFrame)# .to_crs("EPSG:3395")

    gdf['geometry'].to_file(outfile, driver='GeoJSON')
