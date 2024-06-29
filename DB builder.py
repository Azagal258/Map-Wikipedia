######## Libraries ########

import xml.etree.ElementTree as ET
from dotenv import load_dotenv
import os
import mysql.connector


######## Functions ########

### Nodes processing ###

def extract_titles(document_xml: str) -> list:
    """ 
    Extract all usefull infos (here : IDs, Namespaces, Titles and Revision IDs) and contatenates them in a list of tuples
    in view of inputting them into the database
    
    Parameters :
    - document_xml (str) : the path to the file

    Outputs :
    - list of tuples : list a list of tuple as (id, ns, title, revision id)

    """
    print("Nodes processing started")
    out_tuples = []
    tree = ET.parse(document_xml)
    root = tree.getroot()
    # Jinsoul: maybe try merge these two "finds" as they're expensive operations
    for page in root.findall('{http://www.mediawiki.org/xml/export-0.10/}page'): #'for variable in root.iter('{le truc xmlns}nom_de_la_balise')' 

        id = page.find('{http://www.mediawiki.org/xml/export-0.10/}id')
        ns = page.find('{http://www.mediawiki.org/xml/export-0.10/}ns')
        titles = page.find('{http://www.mediawiki.org/xml/export-0.10/}title')
        rev_id = page.find('{http://www.mediawiki.org/xml/export-0.10/}revision/{http://www.mediawiki.org/xml/export-0.10/}id')

        out_tuples.append((id.text, ns.text, titles.text, rev_id.text))
    print(out_tuples)
    return out_tuples

def make_db(titles: list):
    """ 
    Make a csv files of all the titles with them as label and lowercase as id 
    
    Parameters :
    - titles (list) : the path to the file
    - nodes_file

    Outputs :
    - a .csv file
    """
    print("Database created")

######## Magic Land ########

### Inputs ###
document_xml = "test_article.xml"
# document_xml = "./Dumps/XML_files/frwiki-20240301-pages-articles-multistream1.xml"


### Code ###
titles = extract_titles(document_xml)
make_db(titles)