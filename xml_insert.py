import xml.etree.ElementTree as ET
import os
#------------Inserting XML snippet into big xml---------------------#
def xml_insert( main_xml, xml_snip ):
    '''
NAME:
    xml_insert( main_xml, xml_snip )
FILE:
    python_tools/xml_insert.py
REQUIREMENTS:
    - xml.etree.ElementTree
DESCRIPTION:
    xml_insert
    =======
    This function inserts the xml_snip as the last element of main_xml and writes out a tree of the
    entire xml document. It checks the value of the attribute datasetID in xml_snip and see if it exists
    in main_xml. If the attribute exists in the main_xml, it is replaced with the new
    xml_snip.

    Both main_xml and xml_snip can be either of the following formats for input:
        1. filename and path (as a string) to the main xml document for which the xml_snip will be added.
        OR
        2. xml ElementTree object for the main xml document for which xml_snip will be added.
    main_xml = The main xml document for which the xml_snip will be added.
    xml_snip = The xml snippet to be added to main_xml
RETURNS:
    tree = <xml.etree.ElementTree.ElementTree object>

    This is the ElementTree object for the entire datasets.xml for ERDDAP.
USAGE:
    >>> main_xml='/erddap/content/datasets.xml'
    >>> xml_snip='xml_by_dataset/2020_asset_inventory.xml'
    >>> tree = xml_insert( main_xml, xml_snip)
    >>> print(tree)
    <xml.etree.ElementTree.ElementTree object>
    >>> tree.write('/erddap/content/datasets.xml')
    '''
    ## error checking
    try:
        main_xml
        xml_snip
    except NameError:
        man_xml = None
        xml_snip = None

    if isinstance(main_xml, str):
        # if a filename is provided
        if os.stat(main_xml).st_size==0:
            print('The file %s does not exist.' % main_xml)
            sys.exit()
        print("ingesting %s" % main_xml)
        ## Ingest datasets.xml
        main_tree = ET.parse(main_xml)
        main_root = main_tree.getroot()
    else:
        # if an element tree is provided
        main_tree = main_xml
        main_root = main_tree.getroot()

    if isinstance(xml_snip, str):
        # if a filename is provided
        if os.stat(xml_snip).st_size==0:
            print('The file does not exist.' % xml_snip)
            sys.exit()
        print("ingesting %s" % xml_snip)
        ## Ingest xml snippet
        snip_tree = ET.parse(xml_snip)
        snip_root = snip_tree.getroot()
    else:
        # if an element tree is provided
        snip_root = xml_snip.getroot()

    snip_root.tail='\n'

    ## check for existing id:
    string = "dataset/[@datasetID='%s']"%snip_root.attrib['datasetID']
    for node in main_root.findall(string):
        print("Found existing dataset node for datasetID= %s removing..."\
                % snip_root.attrib['datasetID'])
        main_root.remove(node)

    print("Inserting snippet for datasetID = %s into %s" \
            % (snip_root.attrib['datasetID'],main_xml))
    main_root.append(snip_root)

    return main_tree
