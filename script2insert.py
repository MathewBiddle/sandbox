#!/usr/bin/python

import xml_insert

main_xml = '../erddap/content/datasets.xml'
xml_snip = '../xml_by_dataset/gts_statistics.xml'
tree = xml_insert.xml_insert( main_xml, xml_snip )
tree.write('../erddap/content/datasets.xml',encoding="utf-8", xml_declaration=True) # overwrites existing datasets.xml
