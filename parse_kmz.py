from zipfile import ZipFile
import requests

base_url = 'https://www.nhc.noaa.gov/gis/best_track/'
file_name = 'al012019_best_track.kmz'
fileobject = requests.get(base_url + file_name)
open(file_name, 'wb').write(fileobject.content)

kmz = ZipFile(file_name, 'r')
kml = kmz.open(file_name.replace('_best_track.kmz', '.kml'), 'r').read()

from lxml import html

doc = html.fromstring(kml)
for pm in doc.cssselect('Folder Placemark Polygon coordinates'):
    tmp = pm.cssselect('track')
    name = pm.cssselect('name')[0].text_content()
    if len(tmp):
        # Track Placemark
        tmp = tmp[0]  # always one element by definition
        for desc in tmp.iterdescendants():
            content = desc.text_content()
            if desc.tag == 'when':
                print(content)
                #do_timestamp_stuff(content)
            elif desc.tag == 'coord':
                print(content)
                #do_coordinate_stuff(content)
            else:
                print("Skipping empty tag %s" % desc.tag)
    else:
        # Reference point Placemark
        coord = pm.cssselect('Point coordinates')[0].text_content()
        print(coord)
        #do_reference_stuff(coord)