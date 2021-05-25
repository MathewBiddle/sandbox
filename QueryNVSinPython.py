#Get the list of vocabularies included in NVS
def sparql(term):
    from SPARQLWrapper import SPARQLWrapper, JSON
    import pandas as pd

    sparql = SPARQLWrapper("http://vocab.nerc.ac.uk/sparql/sparql") #Choose the sparql endpoint you wish
    sparql.setQuery("""
    
    prefix skos:<http://www.w3.org/2004/02/skos/core#>
    prefix owl:<http://www.w3.org/2002/07/owl#>
    prefix dc:<http://purl.org/dc/terms/>
    
    select distinct (?localnam as ?Collection) (?dt as ?Title) (?desc as ?Description) (?crex as ?Governance)  
    where {
    ?x a skos:Collection .
    optional{?x dc:creator ?cre } .
    ?x dc:title ?dt ;dc:description ?desc .BIND(REPLACE(str(?x), "http://vocab.nerc.ac.uk/collection/", "") AS ?localname) BIND(REPLACE(str(?localname), "/current/", "") AS ?localnam) BIND(if(EXISTS{?x dc:creator ?cre},?cre,"") as ?crex)}  
    order by desc(?Rank) 
    offset 0 limit 290
    
    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    df = pd.DataFrame(
        columns=['Collection', 'Title', 'Governance'])
    i=0
    for result in results["results"]["bindings"]:
        print(result["Collection"]["value"],result["Title"]["value"],result["Governance"]["value"],sep="---")
        df = df.append({'Collection': result["Collection"]["value"],
                        'Title': result["Title"]["value"],
                        'Governance': result["Governance"]["value"]},
                       ignore_index=True)

def ReST(term):
    import requests
    import xml.etree.ElementTree as ET
    url_base = 'https://vocab.nerc.ac.uk/'
    url_suffix = 'collection/'

    temp = requests.get(url_base + url_suffix)

    root = ET.fromstring(temp.text)
    return temp.text
#df.to_csv('NVS_collections.csv',index=False,header=True)


